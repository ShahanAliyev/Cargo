import factory
from core.models import (
    PhonePrefix, LocalWarehouse, Currency, Country,
    ProductType, Discount, Tariff
)
from user.models import User
from order.models import Declaration, Status


class PhonePrefixFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = PhonePrefix
    
    prefix = '+99470'


class WareHouseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LocalWarehouse
    
    name = "Random Warehouse"
    address = "Random address"
    longitude = "123.45678"
    latitude = "123.45678"


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
    
    email = "my.email@gmail.com"
    first_name = "Shahan"
    last_name = "Aliyev"
    password = "123456789ss"
    # gender = factory.Iterator([choice[0]] for choice in User.GENDERS)
    gender = "M"
    phone_prefix = factory.SubFactory(PhonePrefixFactory)
    phone = "8341321"
    gov_prefix = "AZE"
    # gov_prefix = factory.Iterator([choice[0] for choice in User.GOV_PREFIX])
    gov_id = "18092345"
    fin_code = "7BB3DDM"
    client_code = "12345678"
    warehouse = factory.SubFactory(WareHouseFactory)


class CurrencyFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Currency
    
    name = "TL"
    sign = "₺"
    rate = 0.051


class CountryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Country
    
    name = "Turkey"


class ProductTypeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ProductType
    
    name = "Dress"

    
class StatusFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Status
    
    name = "Created"


class DiscountFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Discount
    
    amount = "50"
    reason = Discount.DiscountReason.YOUNG  


class TariffFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Tariff
    
    min_weight = 0.5
    max_weight = 0.6
    country = factory.SubFactory(CountryFactory)
    base_price = 3.50


class DeclarationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Declaration

    product_price = 1200.50
    product_currency = factory.SubFactory(CurrencyFactory)
    country = factory.SubFactory(CountryFactory)
    product_type = factory.SubFactory(ProductTypeFactory)
    shop_name = "Koton"
    status = factory.SubFactory(StatusFactory)
    user = factory.SubFactory(UserFactory)
    weight = 0.58
