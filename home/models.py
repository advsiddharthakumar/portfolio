from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    subject = models.TextField()
    message = models.TextField()
    date = models.DateField()
    






