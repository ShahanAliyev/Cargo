from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify


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



class ContactUs(models.Model):

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
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super(ContactUs, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        pass  # prevent deletion of instance


from django.contrib.auth import get_user_model
User = get_user_model()


class News(models.Model):

    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="media/images/news", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True) if needed
    # tags = models.ForeignKey(Tags, on_delete=models.CASCADE, null=True, blank=True) if needed

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'News'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.user.id}")
        super().save(*args, **kwargs)


class Tariff(models.Model):

    FIXED = 1
    PER_GRAM = 2

    FIXED_PER_GRAM = (
        (FIXED, 'Fixed'),
        (PER_GRAM, 'Per Gram')
    )

    LIQUID = 1
    NOT_LIQUID = 0

    LIQUID_OR_NOT = (
        (LIQUID, 'Liquid'),
        (NOT_LIQUID, 'Not Liquid')
    )

    min_weight = models.DecimalField(max_digits=4, decimal_places=1)
    max_weight = models.DecimalField(max_digits=4, decimal_places=1)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='tarifs')
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    fixed_or_per_gram = models.IntegerField(choices=FIXED_PER_GRAM, default=PER_GRAM)
    is_liquid = models.IntegerField(choices=LIQUID_OR_NOT, default=NOT_LIQUID)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"From {self.min_weight} to {self.max_weight} for {self.country.name}"

