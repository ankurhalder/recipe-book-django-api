from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
