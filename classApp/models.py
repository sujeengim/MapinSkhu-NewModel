from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Classes(models.Model):
    kind = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    class_name = models.CharField(max_length=300)
    prof = models.CharField(max_length=100)

    room = models.CharField(max_length=100, null=True)
    date1 = models.CharField(max_length=5, null=True)
    date2 = models.CharField(max_length=5, null=True)
    start = models.CharField(max_length=10, null=True)
    end = models.CharField(max_length=10, null=True)
    kwan_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.id/self.class_name}'

class Kwan(models.Model):
    kwan_num = models.SmallIntegerField(
        validators=[
            MinValueValidator(1), MaxValueValidator(13)
            ]
    ) 
    kwan_name = models.CharField(max_length=50, null=True)
    kwan_image = models.ImageField(upload_to='images/kwan', null=True, blank=True)

    def __str__(self):
        return f'{self.kwan_name}'

class Room(models.Model):
    kwan_name = models.CharField(max_length=50)
    room = models.CharField(max_length=100)
    floor = models.SmallIntegerField(
        validators=[
            MinValueValidator(1), MaxValueValidator(10)
            ]
    ) 
    room_image = models.ImageField(upload_to='images/room', null=True, blank=True)

    def __str__(self):
        return f'{self.room}'