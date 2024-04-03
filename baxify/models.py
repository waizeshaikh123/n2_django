from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length = 102)
    password = models.CharField(max_length = 10)