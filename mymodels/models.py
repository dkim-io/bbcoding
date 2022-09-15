from django.db import models

# Create your models here.
class Item(models.Model):
    object_id = models.CharField(max_length=50)
    data = models.JSONField()
