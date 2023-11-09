from django.db import models

class student(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField(max_length=50)
    phone=models.CharField(max_length=50)
    cours=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    def __str__(self):
        return self.name