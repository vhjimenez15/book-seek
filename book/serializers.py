from rest_framework import serializers
from .models import BookModel


class BookSerializer(serializers.Serializer):
    id = serializers.CharField(source='_id', read_only=True)
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    published_date = serializers.CharField(max_length=100)
    genre = serializers.CharField(max_length=50)
    price = serializers.IntegerField()

    def create(self, validated_data):
        book_id = BookModel().create_book(validated_data)
        data_created = {"id": str(book_id)}
        data_created.update(validated_data)
        del data_created["_id"]
        return data_created

    def update(self, instance, validated_data):
        BookModel().update_book(
            instance,
            validated_data
        )
        data_updated = {"id": instance}
        data_updated.update(validated_data)
        return data_updated


class AveragePriceSerializer(serializers.Serializer):
    average_price = serializers.IntegerField()
