# here we create our database tables

# once the tables are ready use the command line to migrate
# python manage.py makemigrations
# it will create a migration file on this specific app
# them
# python manage.py migration
# that will create the table on the project database

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    # relation with User
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # relation with Topic
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # "-" means descendente, without means ascendent
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
        
class Message(models.Model):
    # relation with User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # relation with Room
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
