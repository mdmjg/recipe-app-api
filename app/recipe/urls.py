from django.urls import path, include
from rest_framework.routers import DefaultRouter

# will automatically generate urls for our viewset

from recipe import views

router = DefaultRouter()
router.register("tags", views.TagViewSet)
router.register("ingredients", views.IngredientViewSet)
router.register("recipes", views.RecipeViewSet)

app_name = "recipe"

urlpatterns = [path("", include(router.urls))]
