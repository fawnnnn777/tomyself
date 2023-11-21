
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    biography = models.TextField(blank=True, max_length=124)

class Thought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    datetime = models.CharField(max_length=64)
    text = models.TextField(max_length=640)
    likes = models.ManyToManyField(User, blank=True, related_name="thought")

    def __str__(self):
        return f"User: {self.user}, Thought: {self.text}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)


# Create your models here.
