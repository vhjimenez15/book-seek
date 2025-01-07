from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import BookModel
from .serializers import BookSerializer, AveragePriceSerializer


class BookViewSet(ModelViewSet):
    model = BookModel()
    serializer_class = BookSerializer

    def list(self, request):
        id = request.query_params.get("book_id")
        if id:
            book = self.model.get_one_book(id)
            if not book:
                return Response(
                    {"message": f"ID {id} not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            else:
                serialize = self.serializer_class(book)
                return Response(
                    serialize.data,
                    status=status.HTTP_200_OK
                )
        else:
            books = self.model.get_all_books()
            serialize = self.serializer_class(books, many=True)
            return Response(
                serialize.data,
                status=status.HTTP_200_OK
            )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data_created = serializer.save()
            return Response(data_created, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        book = self.model.get_one_book(id)
        if not book:
            return Response(
                {"message": f"ID {id} not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(
            id, data=request.data, partial=True)
        if serializer.is_valid():
            data_updated = serializer.save()
            return Response(
                data_updated,
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUET)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        book = self.model.get_one_book(id)
        if not book:
            return Response(
                {f"ID {id} not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        self.model.delete_book(id)
        return Response(
            {"message": "Book deleted."},
            status=status.HTTP_204_NO_CONTENT
        )

    @action(detail=False, methods=['GET'], url_path='year', url_name='year')
    def list_average_price(self, request):
        year = request.query_params.get("year")
        if not year:
            return Response(
                {"message": "Param year is required."},
                status=status.HTTP_404_NOT_FOUND
            )
        data = self.model.get_average_price(year)
        average_price = 0
        if len(data) > 0:
            data_elem = data[0]
            serialize = AveragePriceSerializer(data_elem).data
            average_price = serialize["average_price"]
        return Response(
            {"year": year, "average_price": average_price},
            status=status.HTTP_204_NO_CONTENT
        )
