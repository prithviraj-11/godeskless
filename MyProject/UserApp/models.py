from django.db import models

# Create your models here.
class User(models.Model):
    userId=models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone_number=models.IntegerField()

