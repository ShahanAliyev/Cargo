import pytest
from django.core.exceptions import ValidationError
from django.db.utils import DataError

pytestmark=pytest.mark.django_db


class TestUserModel:

    def test_str_return(self, user_factory):
        user = user_factory(email="shah@gmail.com")
        assert user.__str__() == "shah@gmail.com"
    
    def test_valid_phone(self,user_factory):
        user = user_factory(phone="0000000")
        user.full_clean()
    
    def test_invalid_phone1(self, user_factory):
        with pytest.raises(DataError):
            user = user_factory(phone="+994700000000")
            user.full_clean()

    def test_invalid_phone2(self, user_factory):
        with pytest.raises(ValidationError):
            user = user_factory(phone="shahan")
            user.full_clean()
    
    def test_valid_fin_code(self, user_factory):
        user = user_factory(fin_code="AAAAAAA")
        user.full_clean()

    def test_invalid_fin_code(self, user_factory):
        with pytest.raises(ValidationError):
            user = user_factory(fin_code="AAA")
            user.full_clean()
    
    def test_valid_aze_gov_id(self, user_factory):
        user = user_factory(gov_prefix="AZE", gov_id="12345678")
        user.full_clean()

    def test_invalid_aze_gov_id(self,user_factory):
        with pytest.raises(ValidationError):
            user = user_factory(gov_prefix="AZE", gov_id="") # If either less than 8 digits or charfields is used ValidationError rises
            user.full_clean()

    def test_valid_aa_gov_id(self, user_factory):
        user = user_factory(gov_prefix="AA", gov_id="1234567")
        user.full_clean()

    def test_invalid_aa_gov_id(self,user_factory):
        with pytest.raises(ValidationError):
            user = user_factory(gov_prefix="AA", gov_id="123456")
            user.full_clean()

    def test_valid_myi_or_dyi_gov_id(self, user_factory):
        user = user_factory(gov_prefix="DYI", gov_id="123456")
        user.full_clean()

    def test_invalid_myi_or_dyi_gov_id(self,user_factory):
        with pytest.raises(ValidationError):
            user = user_factory(gov_prefix="MYI", gov_id="1234")
            user.full_clean()

#  pytest -p no:pytest-sugar --ignore=postgres_data  shold be used to run tests