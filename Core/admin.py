from django.contrib import admin
from .models import (
    PhonePrefix, WareHouse, Currency, Wallet, Country, ContactUs
    )

admin.site.register(PhonePrefix)
admin.site.register(WareHouse)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Country)
admin.site.register(ContactUs)
