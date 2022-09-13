from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import TagViewSet, IngredientViewSet

router = DefaultRouter()
router.register('tags', TagViewSet, basename='tag')
router.register('ingredients', IngredientViewSet, basename='ingredient')

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
