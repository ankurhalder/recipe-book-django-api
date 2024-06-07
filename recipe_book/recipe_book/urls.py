from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/", include("recipes.urls")
    ),  # Include API URL patterns from the 'recipes' app
]
