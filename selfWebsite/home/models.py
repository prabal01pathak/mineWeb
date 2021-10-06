from django.db import models

# Create your models here.


class HomePage(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Mobile = models.CharField(max_length=200)
    Message = models.TextField()

    def __str__(self):
        return self.name
