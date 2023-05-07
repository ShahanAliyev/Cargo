from django.db import models
from core.models import Currency, Country, Discount, ProductType, Tariff
from django.contrib.auth import get_user_model
from order.utils import calculate_discounted_cost
from django.db.models import Q
from decimal import Decimal
from django.db.models import Max
from django.core.exceptions import ValidationError


User = get_user_model()


class Status(models.Model):

    name = models.CharField(max_length=32)
    next_status = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name


class Declaration(models.Model):

    __status = None

    tracking_code = models.CharField(max_length=13, unique=True, blank=True, null=True)

    cost = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,)
    discounted_cost = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,)
    cost_azn = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,)
    discounted_cost_azn = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True,)

    product_price = models.DecimalField(max_digits=7, decimal_places=2)
    product_currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, related_name='declarations', null=True, blank=True,)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='declarations')
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_DEFAULT, default=1, related_name='declarations')
    is_liquid = models.BooleanField(default=False)
    shop_name = models.CharField(max_length=64)
    image = models.ImageField(null=True, blank=True, upload_to='images/declaration/')
    quantity = models.PositiveSmallIntegerField(default=1)

    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, related_name='declarations')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='declarations', blank=True, null=True)
    discount = models.ManyToManyField(Discount, related_name='declarations', blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    penalty_status = models.BooleanField(default=False)
    penalty = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.status:
            self.__status = self.status.id
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        
        azn_rate = Currency.objects.filter(name="AZN").values_list('rate', flat=True).first()
        usd_rate = Currency.objects.filter(name="USD").values_list('rate', flat=True).first()

        if self.id and self.status:
            if self.status.id != self.__status:
                new_status_history = StatusHistory.objects.create(declaration = self, old_status = self.__status, new_status = self.status.id)
                new_status_history.save()

        if not self.status:
            self.status = Status.objects.filter(order = 0).first()

        if self.weight and not self.cost:
            price_list =  Tariff.objects.filter(Q(max_weight__gt=self.weight) 
                & Q(min_weight__lte=self.weight) 
                & Q(country=self.country)).values_list('base_price', flat=True).all()
            
            if len(price_list) == 0:
                raise ValidationError("There is no assigned price for this weight range")

            elif len(price_list) ==  1:
                price = price_list.first()
                self.cost = price
                self.cost_azn = price / azn_rate
            
            elif len(price_list) > 1:
                price = price_list.aggregate(Max('base_price'))['base_price__max']
                self.cost = price
                self.cost_azn = price / azn_rate

        if self.cost and self.pk and self.discount:
            discounted_cost = calculate_discounted_cost(self)
            if discounted_cost > 0:
                self.discounted_cost = discounted_cost
                self.discounted_cost_azn = Decimal(discounted_cost) / usd_rate / azn_rate
            else:
                self.discounted_cost = 0
                self.discounted_cost_azn = 0

        super(Declaration, self).save(force_insert, force_update, *args, **kwargs)
        self.__status = self.status.id

    def __str__(self):
        return str(self.tracking_code)


class StatusHistory(models.Model):

    declaration = models.ForeignKey(Declaration, on_delete=models.CASCADE, null=True, blank=True, related_name="histories")
    old_status = models.IntegerField(null=True, blank=True)
    new_status = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.declaration}"
