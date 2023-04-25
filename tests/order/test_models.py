# class TestDeclarationModel:

#     def test_cost(self, declaration_factory, discount_factory):

#         discount = discount_factory()
#         declaration = declaration_factory()
#         declaration.discount.add(discount)

#         assert declaration.cost == '2.8'

class TestSomeModels:

    def test_cost(self, discount_factory):

        discount = discount_factory()

        assert discount.constant_or_percentage == "percentage"