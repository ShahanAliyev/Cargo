import random
import string

def generate_tracking_code():
    return ''.join(random.choices(string.digits, k=13))

def apply_discount(discount, cost):
    if discount.constant_or_percentage == 'percentage':
        return cost - (cost * discount.amount) / 100
    elif discount.constant_or_percentage == 'constant':
        return cost - discount.amount

def calculate_discounted_cost(obj, *args, **kwargs):
    # the function applies all discounts and selects the one 
    # with the highest benefit until all discounts are over
    if obj.weight and obj.discount:
        excluded_ids = []
        discounts = obj.discount.all()
        our_cost = float(obj.cost)

        while discounts:
            main_result = 0
            main_result_couse_discount = 0
            course_discount_form = 0

            for discount in discounts:
                discount.amount = float(discount.amount)
                result = apply_discount(discount, our_cost)
                if result > main_result:
                    main_result = result
                    main_result_couse_discount = discount.amount
                    course_discount_form = discount.constant_or_percentage

            if course_discount_form == 'constant':
                our_cost -= main_result_couse_discount
            elif course_discount_form == 'percentage':
                our_cost = our_cost - (our_cost * main_result_couse_discount) / 100

            excluded_ids.append(discounts.filter(amount=main_result_couse_discount).values_list('id', flat=True).first())
            discounts = obj.discount.all().exclude(id__in=excluded_ids)

    return our_cost