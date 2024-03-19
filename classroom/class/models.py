from django.db import models

# Create your models here.
class Course(models.Model):
    serial = models.AutoField(primary_key=True, null=False)
    tutor = models.CharField(max_length=233)
    description = models.CharField(max_length=1098)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    caption1 = models.CharField(max_length=233, null=True, blank=True)
    video1 = models.FileField(upload_to='media/')
    caption2 = models.CharField(max_length=233, null=True, blank=True)
    video2 = models.FileField(upload_to='media/')
    caption3 = models.CharField(max_length=233, null=True, blank=True)
    video3 = models.FileField(upload_to='media/')