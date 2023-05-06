from rest_framework import serializers
from core.models import ForeignWarehouse


class GetForeignWarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForeignWarehouse
        fields = ['client_code', 'address_for_user', 'country', 'name_surname', 'address_header', 'address']