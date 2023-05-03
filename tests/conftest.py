import django
django.setup()

from pytest_factoryboy import register
from tests.factories import (
    PhonePrefixFactory, UserFactory,WareHouseFactory,
    CountryFactory, CurrencyFactory, ProductTypeFactory,
    StatusFactory, DiscountFactory, TariffFactory, 
    DeclarationFactory
    )

register(PhonePrefixFactory)
register(UserFactory)
register(WareHouseFactory)
register(CountryFactory)
register(CurrencyFactory)
register(ProductTypeFactory)
register(StatusFactory)
register(DiscountFactory)
register(TariffFactory)
register(DeclarationFactory)