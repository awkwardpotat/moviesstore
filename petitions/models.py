from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Petition(models.Model):
    id = models.AutoField(primary_key=True) #automatically increments val for each new record added
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='petition_images/') #images will be stored in petition_images
    reason = models.TextField()
    yes_votes = models.PositiveIntegerField(default=0)
    no_votes = models.PositiveIntegerField(default=0)
    #need to keep track of who's voted already
    voted_users = models.ManyToManyField(User, blank=True)
    def __str__(self):
        return str(self.id) + ' - ' + self.name #to string --> id and name