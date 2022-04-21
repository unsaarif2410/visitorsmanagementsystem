from django.db import models

# Create your models here.
class Newuser(models.Model):
    User_ID = models.AutoField(primary_key=True, auto_created=True)
    Username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
