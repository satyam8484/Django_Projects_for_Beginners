from django.db import models

# Create your models here.

class Todo_Item(models.Model):
    content = models.TextField(max_length=200)
