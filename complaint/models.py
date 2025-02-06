from django.db import models

# Create your models here.
class Complaint(models.Model):
    name = models.CharField(max_length=200)
    DNI = models.CharField(max_length=200)
    age = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=300)
    email = models.CharField(max_length=500)
    parents = models.CharField(max_length=200)
    service = models.CharField(max_length=100)
    description = models.TextField()
    complaintType = models.CharField(max_length=100)
    complaintDetail = models.TextField()

    def __str__(self):
        return self.title