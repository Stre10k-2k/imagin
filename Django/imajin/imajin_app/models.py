from django.db import models

class Contact(models.Model):
    name = models.CharField()
    email = models.CharField()
    phone = models.IntegerField()
    company = models.CharField()
    msg = models.TextField()