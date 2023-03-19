from django.db import models


class PhonePrefix(models.Model): # This model might be located in diffirent app 
    ...


class WareHouse(models.Model): # This model might be located in diffirent app 
    ...

class Currency(models.Model):

    name = models.CharField(max_length=32)
    sign = models.CharField(max_length=1)
    rate = models.FloatField()

    def __str__(self):
        return f'{self.name} {self.id}'
    
