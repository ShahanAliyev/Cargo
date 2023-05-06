from django.contrib import admin
from core.models import (
    PhonePrefix, LocalWarehouse, Currency, Country,
    ContactUs, ProductType, News, FAQ,
    CategoryFAQ, Discount, Tariff,ForeignWarehouse
    )

admin.site.register(PhonePrefix)
admin.site.register(LocalWarehouse)
admin.site.register(Currency)
admin.site.register(ContactUs)
admin.site.register(News)
admin.site.register(FAQ)
admin.site.register(CategoryFAQ)
admin.site.register(Discount)
admin.site.register(ProductType)
admin.site.register(ForeignWarehouse)


class TariffInline(admin.TabularInline):
    model = Tariff
    extra = 4

class CountryAdmin(admin.ModelAdmin):
    inlines = [TariffInline] # Code enables us to create Country and Tariff for the country simultaniously

admin.site.register(Country, CountryAdmin)
admin.site.register(Tariff)

