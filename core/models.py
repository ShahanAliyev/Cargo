from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.db.models import JSONField


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

class LocalWarehouse(models.Model): # This model might be located in diffirent app 

    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Local Warehouses"


class Currency(models.Model):

    name = models.CharField(max_length=32)
    sign = models.CharField(max_length=1)
    rate = models.DecimalField(max_digits=6, decimal_places=4)

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


class ForeignWarehouse(models.Model):

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    airwaybill_address = models.CharField(max_length=32)
    address_header = models.CharField(max_length=32)
    client_code = models.CharField(max_length=8, null=True, blank=True)
    name_surname = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=128)
    flexible_data = JSONField(null=True, blank=True)
    address_for_user = models.CharField(max_length=256, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.address_for_user = f"{self.address_header} "

        super(ForeignWarehouse, self).save(*args, **kwargs)

    def __str__(self):
        return f" Warehouse in {self.country.name}"
    

class CategoryFAQ(models.Model):

    name = models.CharField(max_length=32, unique=True)

    class Meta:

        verbose_name = "FAQ Category"
        verbose_name_plural = "FAQ Categories"

    def __str__(self):
        return self.name
    

class FAQ(models.Model):

    question = models.CharField(max_length=256)
    answer = RichTextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey(CategoryFAQ, on_delete=models.CASCADE, related_name="questions")
    order = models.IntegerField(default=0) # to display decent queue of questions

    class Meta:

        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question    
    
    
class Tariff(models.Model):

    class FixedPerGram(models.IntegerChoices):
        FIXED = 1, _('Fixed')
        PER_GRAM = 2, _('Per Gram')

    class LiquidOrNot(models.IntegerChoices):
        LIQUID = 1, _('Liquid')
        NOT_LIQUID = 0, _('Not Liquid')

    min_weight = models.DecimalField(max_digits=6, decimal_places=3)
    max_weight = models.DecimalField(max_digits=6, decimal_places=3)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='tariffs')
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    fixed_or_per_gram = models.IntegerField(choices=FixedPerGram.choices, default=FixedPerGram.PER_GRAM)
    is_liquid = models.IntegerField(choices=LiquidOrNot.choices, default=LiquidOrNot.NOT_LIQUID)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"From {self.min_weight} to {self.max_weight} for {self.country.name}"


class Discount(models.Model):

    class DiscountType(models.TextChoices):
        CONSTANT = 'constant', _('Constant')
        PERCENTAGE = 'percentage', _('Percentage')

    class DiscountReason(models.TextChoices):
        FEMALE = 'female', _('Female')
        YOUNG = 'young', _('Young')
        SUPERUSER = 'superuser', _('Superuser')

    constant_or_percentage = models.CharField(
        max_length=10, choices=DiscountType.choices, default=DiscountType.PERCENTAGE)
    amount = models.DecimalField(max_digits=4, decimal_places=2)
    reason = models.CharField(max_length=32, choices=DiscountReason.choices)

    def __str__(self):
        discount_type = self.get_constant_or_percentage_display()
        reason = self.get_reason_display()
        return f"{self.amount} {discount_type} for {reason}"
    

class ProductType(models.Model):
    
    name = models.CharField(max_length=32)
    parent_type = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
