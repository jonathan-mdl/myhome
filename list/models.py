from django.db import models

# Create your models here.
class HomeList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Home(models.Model):
    commentary = models.TextField(max_length=1000)
    homelist = models.ForeignKey(HomeList, on_delete=models.CASCADE)

    def __str__(self):
        return self.commentary