from django.db import models
from django.contrib.auth.models import User #C
from django.utils import timezone

class IRecord(models.Model):
    time_raised = models.DateTimeField(default=timezone.now, editable=False)
    reference = models.CharField(unique=True, max_length=20)
    description = models.TextField()


class Instrument(models.Model):
    action = models.TextField()
    data = models.TextField()
    reply = models.TextField()
    order = models.ForeignKey(User, on_delete=models.CASCADE, related_name="instrument")

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title

class Card(models.Model):
    cardnumber = models.CharField(max_length=17) 
    expire_on = models.DateTimeField()
    cvv = models.CharField(max_length=17) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="merchant")

    def __str__(self):
        return self.title

# Create your models here.
