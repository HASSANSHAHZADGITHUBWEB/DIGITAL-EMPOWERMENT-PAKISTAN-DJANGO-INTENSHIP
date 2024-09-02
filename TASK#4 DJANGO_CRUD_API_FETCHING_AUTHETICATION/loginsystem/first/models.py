from django.db import models

class user(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=10)
    phno=models.BigIntegerField()
    dob=models.DateField()


# Create your models here.
