from django.db import models

# Create your models here.
class Account(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    ph_no=models.IntegerField()
    mail_id=models.CharField(max_length=250)
    address=models.TextField()
    district=models.CharField(max_length=250)
    branch=models.CharField(max_length=250)
    ac_type=models.CharField(max_length=250)
    materials=models.CharField(max_length=250)