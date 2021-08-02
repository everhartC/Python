from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.CharField(max_length=100)
    servings = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Recipe: {self.name} \nIngredients: {self.ingredients} \nServings: {self.servings}"
    
