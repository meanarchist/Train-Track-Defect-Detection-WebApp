from django.db import models


# Create your models here.

class Employee(models.Model):
    UPLOAD_IMAGE = (models.ImageField(upload_to='images/'))

    def __str__(self):
        return str(self.UPLOAD_IMAGE)
