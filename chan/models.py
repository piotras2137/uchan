from django.db import models
from django.db.models.deletion import CASCADE

class Board(models.Model):
    name  = models.CharField(max_length=128)
    description = models.TextField()
    link = models.CharField(max_length=32, unique=True)
    cover = models.ImageField(blank=True, null=True, upload_to='')

class Thread(models.Model):
    name  = models.CharField(max_length=128, default='ANONYMOUS')
    title = models.CharField(max_length=128)
    text  = models.TextField(null=True, blank=True)
    date  = models.DateTimeField(auto_now_add=True) 
    photo = models.ImageField(null=True, upload_to='')
    board = models.ForeignKey(Board, on_delete=CASCADE, null=True)


class Respone(models.Model):
    name  = models.CharField(max_length=128, default='ANONYMOUS')
    text  = models.TextField(null=True,blank=True)
    date  = models.DateTimeField(auto_now_add=True)
    t_id  = models.ForeignKey(Thread, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True, upload_to='')

