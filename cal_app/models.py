from django.db import models
#from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

class Venue(models.Model):
    name        =   models.CharField('Venue Name',max_length=100)
    address     =   models.CharField('Event Address',max_length=100)
    zip_code    =   models.CharField('Event zip code',max_length=6)
    phone       =   models.CharField('Phone No',max_length=12)
    web         =   models.URLField('Website')
    email       =   models.EmailField()

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name  =   models.CharField('First Name',max_length=100)
    last_name   =   models.CharField('Last Name',max_length=100)
    user_email  =   models.EmailField('User Email')
    
    def __str__(self):
        return self.first_name +' '+ self.last_name
    

class Event(models.Model):
    name        =   models.CharField('Event Name',max_length=100)
    event_date  =   models.DateTimeField('Event Date',default=timezone.now)
    #venue      =   models.CharField(max_length=100)
    venue       =   models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
    #manager     =   models.CharField(max_length=100) #this is for admin only
    manager     =   models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    description =   models.TextField(blank=True)
    attendees   =   models.ManyToManyField(MyClubUser,blank=True,null=True)

    def __str__(self):
        return self.name


