from django.db import models

# Create your models here.

class verification_model(models.Model):
    email = models.EmailField()
    verification_code = models.CharField(max_length=100)
