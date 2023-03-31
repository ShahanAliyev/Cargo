import factory
from core.models import (
    PhonePrefix, WareHouse,
)
from user.models import User


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
    warehouse = factory.SubFactory(WareHouseFactory)