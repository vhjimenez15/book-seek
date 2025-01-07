from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'book', viewset=BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
