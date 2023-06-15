from django.db import models


class Contact(models.Model):
    email_address = models.EmailField()
    message = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    ip_address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
