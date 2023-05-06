from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.api.serializers import GetForeignWarehouseSerializer
from rest_framework import status

from core.models import ForeignWarehouse


@api_view(['GET'])
def get_warehouses(request):
        if request.method == 'GET':
            warehouses = ForeignWarehouse.objects.all()
            serializer = GetForeignWarehouseSerializer(warehouses, many=True)
            for data in serializer.data:
                data['address_for_user'] = f'{serializer.data[0]["address_header"]} {request.user.first_name} {request.user.last_name} {request.user.client_code} {serializer.data[0]["address"]}'
                data['name_surname'] = f'{request.user.first_name} {request.user.last_name}'
                data['client_code'] = int(request.user.client_code)
                return Response(data)


@api_view(['GET'])
def get_warehouse(request, warehouse_id):
    try:
        warehouse = ForeignWarehouse.objects.get(id=warehouse_id)
        serializer = GetForeignWarehouseSerializer(warehouse)
        data = serializer.data
        data['address_for_user'] = f'{serializer.data["address_header"]} {request.user.first_name} {request.user.last_name} {request.user.client_code} {serializer.data["address"]}'
        data['name_surname'] = f'{request.user.first_name} {request.user.last_name}'
        data['client_code'] = int(request.user.client_code)
        return Response(data)
    except ForeignWarehouse.DoesNotExist:
        return Response({'message': 'Warehouse not found'}, status=status.HTTP_404_NOT_FOUND)