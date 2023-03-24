from django.contrib import admin
from .models import User, News, Wallet

admin.site.register(User)
admin.site.register(Wallet)
admin.site.register(News)