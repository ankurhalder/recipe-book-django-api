from django.urls import path
from . import api

urlpatterns = [
    path("recipes/", api.RecipeListCreateAPIView.as_view(), name="recipe-list-create"),
    path(
        "recipes/<int:pk>/",
        api.RecipeRetrieveUpdateDestroyAPIView.as_view(),
        name="recipe-detail",
    ),
]
