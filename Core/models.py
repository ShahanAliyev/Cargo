from django.db import models


class PhonePrefix(models.Model): # This model might be located in diffirent app 

    # PREFIXES = (
    #     ('+99455','+99455'),
    #     ('+99450','+99450'),
    #     ('+99451','+99451'),
    #     ('+99470','+99470'),
    #     ('+99477','+99477'),
    #     ('+99499','+99499'),
    # ) 
    # since task requires not choice field, I decided to keep it as Charfield. 
    # I think in that way any user could not add new prefixes (they just could use existing ones)  

    prefix = models.CharField(max_length=6)

    def __str__(self):
        return self.prefix 


class WareHouse(models.Model): # This model might be located in diffirent app 


    class Meta:
        verbose_name_plural = "Warehouses"


class Currency(models.Model):

    name = models.CharField(max_length=32)
    sign = models.CharField(max_length=1)
    rate = models.FloatField()

    def __str__(self):
        return f'{self.name} {self.id}' 


    class Meta:
        verbose_name_plural = "Currencies"


from django.contrib.auth import get_user_model

User = get_user_model()


class Wallet(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.first_name}'s {self.currency.name} balance {self.balance}"
    

class Country(models.Model):

    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "Countries"