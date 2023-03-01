from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=50)

    def __str__(self):
        return self.name
    
class Artist(models.Model):
    name = models.CharField("Artist Name", max_length=50)
    work = models.ManyToManyField("Work", verbose_name="Work")

    def __str__(self):
        return self.name

class Work(models.Model):
    LINK_CHOICES = [
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    ]
    link = models.URLField("Link", max_length=200)
    work_type = models.CharField(max_length=2, choices=LINK_CHOICES) 

    def __str__(self):
        return self.work_type