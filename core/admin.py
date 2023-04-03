from django.contrib import admin
from core.models import (
    PhonePrefix, WareHouse, Currency, Country, 
    ContactUs, News, FAQ, CategoryFAQ, Discount
    )

admin.site.register(PhonePrefix)
admin.site.register(WareHouse)
admin.site.register(Currency)
admin.site.register(Country)
admin.site.register(ContactUs)
admin.site.register(News)
admin.site.register(FAQ)
admin.site.register(CategoryFAQ)
admin.site.register(Discount)

