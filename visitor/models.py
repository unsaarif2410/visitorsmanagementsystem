from django.db import models

# Create your models here.
class Department(models.Model):
    Department_ID = models.AutoField(primary_key=True, auto_created=True)
    Department_Name=models.CharField(max_length=225)
class Visitor(models.Model):
    Visitor_ID = models.AutoField(primary_key=True, auto_created=True)
    Visitor_Name=models.CharField(max_length=225)
    Visitor_CNIC=models.CharField(max_length=15)
    Visitor_Mobile=models.CharField(max_length=15)
    Visitor_Company=models.CharField(max_length=150)
    Visitor_Address=models.CharField(max_length=150)
    Meeting_With=models.CharField(max_length=15)
    Department_ID= models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    Check_In = models.DateTimeField()
    Check_Out = models.DateTimeField()
    Purpose_Of_Meeting=models.CharField(max_length=15)
    