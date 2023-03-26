import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

pytestmark=pytest.mark.django_db


class TestUserModel:

    def test_str_return(self, user_factory):
        user = user_factory(email="shah@gmail.com")
        assert user.__str__() == "shah@gmail.com"
    
    def test_valid_phone(self,user_factory):
        try:
            user = user_factory(phone="0000000")
        except Exception as e:
            pytest.fail(f"Exeption raised {type(e).__name__}")
    
    def test_invalid_phone1(self, user_factory):
        with pytest.raises(Exception):
            user = user_factory(phone="+994700000")

    def test_invalid_phone2(self, user_factory):
        with pytest.raises(Exception):
            user = user_factory(phone="shahan")
    
    def test_valid_fin_code(self, user_factory):
        try:
            user = user_factory(fin_code="AAAAAAA")
        except Exception as e:
            pytest.fail(f"Exeption raised {type(e).__name__}")

    def test_invalid_fin_code(self, user_factory):
        with pytest.raises(Exception):
            user = user_factory(fin_code="AAA")
    
    def test_valid_aze_gov_id(self, user_factory):
        try:
            user = user_factory(gov_prefix="AZE", gov_id="12345678")
        except Exception as e:
            pytest.fail(f"Exeption raised {type(e).__name__}")

    def test_invalid_aze_gov_id(self,user_factory):
        with pytest.raises(Exception):
            user = user_factory(gov_prefix="AZE", gov_id="")

    def test_valid_aa_gov_id(self, user_factory):
        try:
            user = user_factory(gov_prefix="AA", gov_id="1234567")
        except Exception as e:
            pytest.fail(f"Exeption raised {type(e).__name__}")

    def test_invalid_aa_gov_id(self,user_factory):
        with pytest.raises(Exception):
            user = user_factory(gov_prefix="AA", gov_id="123456")

    def test_valid_myi_or_dyi_gov_id(self, user_factory):
        try:
            user = user_factory(gov_prefix="DYI", gov_id="123456")
        except Exception as e:
            pytest.fail(f"Exeption raised {type(e).__name__}")

    def test_invalid_myi_or_dyi_gov_id(self,user_factory):
        with pytest.raises(Exception):
            user = user_factory(gov_prefix="MYI", gov_id="1234")


#  pytest -p no:pytest-sugar --ignore=postgres_data  shold be used to run tests