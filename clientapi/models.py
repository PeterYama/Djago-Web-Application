from django.db import models

# Models the data structure
class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name