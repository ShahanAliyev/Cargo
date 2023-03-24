import os
import django
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cargo.settings')
django.setup()
# Without upper codes terminal pops up error

from pytest_factoryboy import register
from .factories import PhonePrefixFactory, UserFactory, WareHouseFactory

register(PhonePrefixFactory)
register(UserFactory)
register(WareHouseFactory)