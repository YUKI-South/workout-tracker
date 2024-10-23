from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
)

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True)

    def __str__(self):
        return self.username



class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    exercise_type = models.CharField(max_length=100)
    weight = models.FloatField(null=True, blank=True)
    reps = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.exercise_type} on {self.date}'