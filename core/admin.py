from django.contrib import admin
from core.models import (
    PhonePrefix, WareHouse, Currency, Country, ContactUs, News
    )

admin.site.register(PhonePrefix)
admin.site.register(WareHouse)
admin.site.register(Currency)
admin.site.register(Country)
admin.site.register(ContactUs)
admin.site.register(News)

