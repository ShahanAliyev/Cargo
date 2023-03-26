from django.db import models
from django.core.validators import RegexValidator


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

    class Meta:
        verbose_name_plural = "Phone Prefixes"

class WareHouse(models.Model): # This model might be located in diffirent app 

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
    
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



class Country(models.Model):

    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class SingletonModel(models.Model):

    def save(self,*args,**kwargs):
        self.pk = 1

        super().save(*args, **kwargs)


class ContactUs(SingletonModel):

    email = models.CharField(max_length=64)
    phone_prefix = models.ForeignKey(PhonePrefix, on_delete=models.CASCADE, null=True,blank=True)
    phone = models.CharField(
        max_length=7, validators=[RegexValidator(r'^\d{7}$',
        message="Please enter valid phone number")]
        )
    working_hours = models.CharField(max_length=16)

    def __str__(self):
        return "Contact Us details"
    
    class Meta:
        verbose_name = "Contact US"
        verbose_name_plural = "Contact US"
