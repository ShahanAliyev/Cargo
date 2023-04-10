from django.contrib import admin
from order.models import Status, Declaration

admin.site.register(Status)


@admin.register(Declaration)
class DeclarationAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
