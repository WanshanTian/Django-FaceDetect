from django.db import models
# Create your models here.
class faceDet(models.Model):
    img = models.ImageField()
    def __str__(self):
        return self.img.name