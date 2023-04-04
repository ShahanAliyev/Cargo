from django.contrib import admin
from core.models import (
    PhonePrefix, WareHouse, Currency, Country,
    ContactUs, ProductType, News, FAQ,
    CategoryFAQ, Discount, Tariff,
    )

admin.site.register(PhonePrefix)
admin.site.register(WareHouse)
admin.site.register(Currency)
admin.site.register(ContactUs)
admin.site.register(News)
admin.site.register(FAQ)
admin.site.register(CategoryFAQ)
admin.site.register(Discount)
admin.site.register(ProductType)


class TariffInline(admin.TabularInline):
    model = Tariff
    extra = 4

class CountryAdmin(admin.ModelAdmin):
    inlines = [TariffInline] # Code enables us to create Country and Tariff for the country simultaniously

admin.site.register(Country, CountryAdmin)
admin.site.register(Tariff)

