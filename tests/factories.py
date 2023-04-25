import factory
from core.models import (
    PhonePrefix, WareHouse, Country,
    ProductType, Discount, Tariff
)
from order.models import Declaration, Status
from django.contrib.auth import get_user_model
User = get_user_model()


class PhonePrefixFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = PhonePrefix
    
    prefix = '+99470'


class WareHouseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = WareHouse
    
    name = "Random Warehouse"


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


class StatusFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Status
    
    name = "Created"
    order = 1


class CountryFactory(factory.django.DjangoModelFactory):

    class Meta:

        model = Country
    
    name = "Turkey"


class ProductTypeFactory(factory.django.DjangoModelFactory):

    class Meta:

        model = ProductType
    
    name = "Clothes"


class DiscountFactory(factory.django.DjangoModelFactory):

    class Meta:

        model = Discount
    
    amount = "50"
    reason = Discount.DiscountReason.YOUNG


class TariffFactory(factory.django.DjangoModelFactory):

    class Meta:

        model = Tariff
    
    min_weight = "0.5"
    max_weight = "0.6"
    country = factory.SubFactory(CountryFactory)
    base_price = '2.8'


class DeclarationFactory(factory.django.DjangoModelFactory):

    class Meta:

        model = Declaration

    product_price = "1200"
    country = factory.SubFactory(CountryFactory)
    product_type = factory.SubFactory(ProductType)
    shop_name = "Koton"
    weight = "0.600"
