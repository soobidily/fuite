"""
Exercise Log Database
------------------------------

:param exercise_id: ID - ID of exercise in exercise catalogue.
"""
from django.db import models
from login.models import Users

# Create your models here.
class GymLog(models.Model):
    date = models.DateField("Exercise Date")
    sets = models.IntegerField()
    reps = models.IntegerField()
    exercise_id = models.IntegerField()
    # Many-to-one log.
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE
    )
