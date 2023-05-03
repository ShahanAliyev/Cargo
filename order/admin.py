from django.contrib import admin
from order.models import Status, Declaration, StatusHistory

admin.site.register(Status)
admin.site.register(StatusHistory)


@admin.register(Declaration)
class DeclarationAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)
        

