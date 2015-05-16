from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=200)


class Vendor(models.Model):
    name = models.CharField(max_length=200)


class Project(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    cost = models.IntegerField()
