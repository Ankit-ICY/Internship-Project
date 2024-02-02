from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
       return self.name



class Quotes(models.Model):
    writer = models.CharField(max_length = 50)
    quote = models.CharField(max_length = 150)





