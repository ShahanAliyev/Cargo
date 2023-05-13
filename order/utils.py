import random
import string
from core.models import Discount

def generate_tracking_code():
    return ''.join(random.choices(string.digits, k=13))

def apply_discount(discount, cost):
    if discount.constant_or_percentage == Discount.DiscountType.PERCENTAGE:
        return cost - (cost * discount.amount) / 100
    elif discount.constant_or_percentage == Discount.DiscountType.CONSTANT:
        return cost - discount.amount

def calculate_discounted_cost(obj, *args, **kwargs):
    # the function applies all discounts and selects the one 
    # with the highest benefit until all discounts are over
    if obj.weight and obj.discounts:
        excluded_ids = []
        discounts = obj.discounts.all()
        our_cost = float(obj.cost)
        loop = True

        while discounts and loop:
            main_result = 0
            main_result_couse_discount = None
            course_discount_form = None

            for discount in discounts:
                discount.amount = float(discount.amount)
                result = apply_discount(discount, our_cost)

                if not result <= 0 and result > main_result:
                    main_result = result
                    main_result_couse_discount = discount.amount
                    course_discount_form = discount.constant_or_percentage
                    
                    if course_discount_form == 'constant':
                        our_cost -= main_result_couse_discount
                    elif course_discount_form == 'percentage':
                        our_cost = our_cost - (our_cost * main_result_couse_discount) / 100

                    excluded_ids.append(discounts.filter(amount=main_result_couse_discount).values_list('id', flat=True).first())
                    discounts = obj.discounts.all().exclude(id__in=excluded_ids)

                elif result <= 0:
                    our_cost = 0
                    loop = False
                    break
    return our_cost