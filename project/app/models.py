from django.db import models


# Create your models here.
class demo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self):
        return self.name
