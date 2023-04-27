import django
django.setup()

from pytest_factoryboy import register
from .factories import PhonePrefixFactory, UserFactory, WareHouseFactory

register(PhonePrefixFactory)
register(UserFactory)
register(WareHouseFactory)