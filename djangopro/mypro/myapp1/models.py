from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
    password= models.CharField(max_length=15)
   

    def __str__(self):
        return self.name