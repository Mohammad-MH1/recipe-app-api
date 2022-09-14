from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import TagViewSet, IngredientViewSet, RecipeViewSet

router = DefaultRouter()
router.register('tags', TagViewSet, basename='tag')
router.register('ingredients', IngredientViewSet, basename='ingredient')
router.register('recipes', RecipeViewSet, basename='recipe')

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
