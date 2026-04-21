# def calculate_total(price, tax_rate=0.20, discount=0, tip=0.12):
#     subtotalb4tip = price - discount
#     subtotal = (subtotalb4tip * tip) + subtotalb4tip
#     tax = subtotal * tax_rate
#     total = subtotal + tax 
#     return total

# # Test cases
# print(f"£{calculate_total(100):.2f}")
# print(f"£{calculate_total(100, 0.1):.2f}")
# print(f"£{calculate_total(100, 0.08, 10):.2f}")


def grade_calculator(homework_score, test_score):
    return (homework_score * 0.30) + (test_score * 0.70)

print(f"Grade is {grade_calculator(80,90):.2f}")