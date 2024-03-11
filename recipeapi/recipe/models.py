from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    title=models.CharField(max_length=30)
    cuisine=models.CharField(max_length=30)
    meal_type=models.CharField(max_length=20)
    ingredients=models.TextField()
    instructions=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"Review by {self.user.username} on {self.recipe.title}"

