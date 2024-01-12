def calculate_discount(original_price, discount_percentage = 10):
    discounted_price = original_price - (original_price*discount_percentage / 100)
    return discounted_price

mixed_data = [10, "apple", 3.14, "orange", 25, 7.5, "banana", 42.0]

original_price = 200
discounted_price = calculate_discount(original_price)

discounted_price = calculate_discount(original_price)

# Decision-making structure based on discounted price
if discounted_price < 50:
    print("Low-cost item.")
elif 50 <= discounted_price <= 100:
    print("Moderate-cost item.")
else:
    print("High-cost item.")

# Loop to iterate through mixed_data
for element in mixed_data:
    print(f"{element} - {type(element)}")
