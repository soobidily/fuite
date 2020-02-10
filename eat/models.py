"""
Food Log Database
------------------------------

When retrieving, search each database for any items on a given date or meal.

:param date: DateTime - Date/Time of consumption.
:param meal_name: String - name of meal eg. 'Breakfast'.
:param food_id: ID - id of item in the catalogue.
"""
from django.db import models
from login.models import Users

class EatLog(models.Model):
    date = models.DateField("Meal Date")
    meal_name = models.CharField("Meal", max_length=9)
    food_id = models.IntegerField()
    # Many-to-one log.
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE
    )
