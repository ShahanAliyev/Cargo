import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cargo.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cargo.test_settings'

from pytest_factoryboy import register
from .factories import PhonePrefixFactory, UserFactory, WareHouseFactory

register(PhonePrefixFactory)
register(UserFactory)
register(WareHouseFactory)



# import os
# import django
# from django.conf import settings
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cargo.settings')
# django.setup()
# # Without upper codes terminal pops up error

# pytestmark = [pytest.mark.django_db(databases=["tests_db"])]