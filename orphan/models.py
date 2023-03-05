from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Orphan(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=30)
    guardian = models.CharField(max_length=50)
    education_status = models.CharField(max_length=50)
    current_donor = models.CharField(max_length=50)

class Help(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    help_offered = models.CharField(max_length=30)
    
    
    def __str__(self):
        return 'Name: {},Id: {}'.format(self.name,self.id)

    
   
    
   
    
    def __str__(self):
        return 'first_name: {},Id: {}'.format(self.first_name,self.id)


