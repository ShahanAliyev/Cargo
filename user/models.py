from core.models import PhonePrefix, LocalWarehouse, Currency
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import re
from django.core.exceptions import ValidationError
from user.managers import UserManager
from user.utils import generate_unique_digit


class User(AbstractBaseUser, PermissionsMixin):

    GENDERS = (
        ("M", "Male"),
        ("F", "Female"),
    )

    GOV_PREFIX = (
        ("AZE", "AZE"),
        ("AA", "AA"),
        ("MYI", "MYI"),
        ("DYI", "DYI"),
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDERS, max_length=1)
    phone_prefix = models.ForeignKey(PhonePrefix, on_delete=models.CASCADE, null=True,blank=True)
    phone = models.CharField(
        max_length=7, validators=[RegexValidator(r'^\d{7}$',
        message="Please enter your valid phone number")], unique=True
        )
    gov_prefix = models.CharField(choices=GOV_PREFIX, max_length=3)
    gov_id = models.CharField(max_length=8, unique=True)
    fin_code = models.CharField(
        unique=True, max_length=8 ,validators = [RegexValidator(r'^[0-9A-Za-z]{7}$',
        message="Fin Code has to be 7 characters with letters and digits")]
        )
    client_code = models.CharField(max_length=8, null=True, blank=True, unique=True)
    monthly_expences = models.DecimalField(null=True,blank=True,default=0,max_digits=5, decimal_places=2)
    birth_date =  models.DateField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default = False)  
    date_joined = models.DateTimeField(auto_now_add=True)
    warehouse = models.ForeignKey(LocalWarehouse, on_delete=models.CASCADE, null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
    
    # def clean(self):
    #     if self.gov_prefix == "AZE" and len(self.gov_id) !=8:
    #         raise ValueError("Gov id must be exactly 8 digits")
    #     elif self.gov_prefix == "AA" and len(self.gov_id) !=7:
    #         raise ValueError("Gov id must be exactly 7 digits")
    #     elif (self.gov_prefix == "MYI" or self.gov_prefix == "DYI") and (len(self.gov_id) !=5 or len(self.gov_id) !=6):
    #         raise ValueError("Gov id must be either 5 or 6 digits")
    #     elif not self.gov_id.isdigit():
    #         raise ValueError("Gov id must contain only digits")

    def clean(self):
        super().clean()
        if self.gov_prefix == "AZE" and not re.match(r'^\d{8}$', self.gov_id):
            raise ValidationError("Gov id must be exactly 8 digits")
        elif self.gov_prefix == "AA" and not re.match(r'^\d{7}$', self.gov_id):
            raise ValidationError("Gov id must be exactly 7 digits")
        elif (self.gov_prefix == "MYI" or self.gov_prefix == "DYI") and not re.match(r'^\d{5,6}$', self.gov_id):
            raise ValidationError("Gov id must be either 5 or 6 digits")
        elif not self.gov_id.isdigit():
            raise ValidationError("Gov id must contain only digits")

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.client_code:
            while True:
                code = generate_unique_digit()
                if not User.objects.filter(client_code=code).exists():
                    self.client_code = code
                    break
        super(User, self).save(*args, **kwargs)

        
# @receiver(post_save, sender=User)
# def generate_client_code(sender,instance,created,**kwargs):
#     if  not instance.client_code:
#         instance.client_code = generate_unique_digit()
#         instance.save()


class Wallet(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.first_name}'s {self.currency.name} balance {self.balance}"
