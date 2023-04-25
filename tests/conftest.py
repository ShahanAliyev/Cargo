import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cargo.settings")
django.setup()
from pytest_factoryboy import register

from tests.factories import (PhonePrefixFactory, WareHouseFactory, CountryFactory,
                             ProductTypeFactory, DiscountFactory, TariffFactory,
                             DeclarationFactory, StatusFactory)

register(PhonePrefixFactory)
register(WareHouseFactory)
register(CountryFactory)
register(ProductTypeFactory)
register(DiscountFactory)
register(TariffFactory)
# register(DeclarationFactory)
register(StatusFactory)