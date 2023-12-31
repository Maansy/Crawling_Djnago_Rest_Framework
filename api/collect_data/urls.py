from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='article')


urlpatterns = [
    path('', include(router.urls)),
]