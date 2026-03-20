from django.db import models
from django.contrib.auth.models import AbstractUser
from bson import ObjectId


def generate_object_id():
    return str(ObjectId())


class Team(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=generate_object_id)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(AbstractUser):
    _id = models.CharField(max_length=24, primary_key=True, default=generate_object_id)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

    def __str__(self):
        return self.username


class Activity(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=generate_object_id)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.type}"


class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=generate_object_id)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.score}"


class Workout(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, default=generate_object_id)
    name = models.CharField(max_length=200)
    description = models.TextField()
    schedule = models.CharField(max_length=100, blank=True, default='')
    max_attendance = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
