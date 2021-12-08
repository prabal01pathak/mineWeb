from django.db import models

# Create your models here.


class Image(models.Model):
    Image = models.ImageField(upload_to='images/')

class HomePage(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Mobile = models.CharField(max_length=200)
    Message = models.TextField()

    def __str__(self):
        return self.name

class OtherThing(models.Model):
    Heading = models.CharField(max_length=200,default="none",blank=True)
    Title = models.CharField(max_length=200,blank=True)
    File = models.FileField(upload_to="files/",blank=True)
    any_other_html = models.TextField(blank="True",default="none")
    any_image = models.ImageField(blank=True,upload_to="images/")

class Certificates(models.Model):
    certificate_html = models.TextField()
