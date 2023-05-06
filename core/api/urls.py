from django.urls import path
from core.api.views import get_warehouse, get_warehouses

urlpatterns = [
    path('warehouses/', get_warehouses, name="warehouses" ),
    path('warehouses/<int:warehouse_id>/', get_warehouse, name="warehouse"),
]