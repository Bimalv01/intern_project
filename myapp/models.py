from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name

