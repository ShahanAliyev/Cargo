import pytest
from contextlib import nullcontext as does_not_raise
from django.core.exceptions import ValidationError
import math


@pytest.mark.django_db
class TestDeclarationModel:
    pytestmark = pytest.mark.django_db

    @pytest.fixture
    def get_country(self, country_factory):
        country = country_factory()
        return country
    
    @pytest.fixture
    def get_tariff(self, tariff_factory, get_country):
        return tariff_factory(country = get_country)
    
    @pytest.fixture
    def get_azn(self, currency_factory):
        return currency_factory(name = "AZN", sign = "₼", rate = 0.58)
    
    @pytest.fixture
    def get_usd(self, currency_factory):
        return currency_factory(name = "USD", sign = "$", rate = 1)
    
    @pytest.fixture
    def get_discount(self, discount_factory):
        discount = discount_factory()
        return discount
    
    @pytest.mark.parametrize(
        "example_input, expectation",
        [
        (3.5, does_not_raise()),
        (3, pytest.raises(AssertionError)),  
        ],
    )

    def test_declaration_cost(self, declaration_factory, expectation, example_input, get_country, get_tariff, get_azn, get_usd):
        declaration = declaration_factory(country = get_country)

        with expectation:
            assert declaration.cost == example_input

    @pytest.mark.parametrize(
        "example_input, expectation",
        [
        ((3.5 / 0.58), does_not_raise()),
        (3, pytest.raises(AssertionError)),  
        ],
    )

    def test_declaration_cost_azn(self, declaration_factory, expectation, example_input, get_country, get_tariff, get_azn, get_usd):
        declaration = declaration_factory(country = get_country)
        with expectation:
            assert math.isclose(declaration.cost_azn, example_input)


    @pytest.mark.parametrize(
        "example_input, expectation",
        [
        ((3.5/2), does_not_raise()),
        (3, pytest.raises(AssertionError)),  
        ],
    )

    def test_discounted_cost(self, declaration_factory, expectation, example_input, get_country,get_discount, get_tariff, get_azn, get_usd):
        declaration = declaration_factory(country = get_country)
        
        declaration.discount.add(get_discount)
        declaration.save()
        with expectation:
            assert declaration.discounted_cost == example_input


    @pytest.mark.parametrize(
        "example_input, expectation",
        [
        ((3.5/0.58/2), does_not_raise()),
        (3, pytest.raises(AssertionError)),  
        ],
    )

    def test_discounted_cost_azn(self, declaration_factory, expectation, example_input, get_country,get_discount, get_tariff, get_azn, get_usd):
        declaration = declaration_factory(country = get_country)
        declaration.discount.add(get_discount)
        declaration.save()
        with expectation:
            assert math.isclose(declaration.discounted_cost_azn, example_input)