from django.db import models

class login1(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    option = models.CharField(max_length=50)

    objects = models.Manager()

class data(models.Model):
    name = models.CharField(max_length=30)
    task = models.CharField(max_length=30)
    asignto = models.CharField(max_length=50)
    review = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50)

    objects = models.Manager()
