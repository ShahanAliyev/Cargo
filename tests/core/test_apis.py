import pytest
from rest_framework.test import APIClient
from contextlib import nullcontext as does_not_raise
client = APIClient()


pytest.mark.django_db
class TestForeignWarehouseApi:
    pytestmark = pytest.mark.django_db

    @pytest.fixture
    def get_user(self, user_factory):
        user = user_factory(first_name="Shahan", last_name="Aliyev", client_code=12345678)
        return user
    
    @pytest.fixture
    def get_foreign_warehouse(self, foreign_factory):
        warehouse = foreign_factory()
        return warehouse
    
    @pytest.mark.parametrize(
        "client_code, full_name, expectation",
        [
        (12345678, "Shahan Aliyev", does_not_raise()),
        (12345678, "Aliyev Shahan", pytest.raises(KeyError)),
        (12344321, "Aliyev Shahan", pytest.raises(KeyError)),
        ],
    )
    
    def test_foreign_warehouse(self, get_user, get_foreign_warehouse, client_code, full_name, expectation):
        client.force_authenticate(user=get_user)
        response = client.get("/api/core/warehouses/1/")
        with expectation:    
            assert response.data['client_code'] == client_code
            assert response.data['name_surname'] == full_name
