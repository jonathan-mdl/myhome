from django.db import models

# Create your models here.

class HomeList(models.Model):
    name = models.CharField(max_length=200)

    def __str_(self):
        return self.name

class Item(models.Model):
    homelist = models.ForeignKey(HomeList, on_delete=models.CASCADE)
    commentary = models.CharField(max_length=1000)
    complete = models.BooleanField()

    def __str__(self):
        return self.commentary