from django.db import models

class CalorieEntry(models.Model):
    date = models.DateField()
    food_name = models.CharField(max_length=255)
    calories = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.food_name} ({self.calories} kcal)"
