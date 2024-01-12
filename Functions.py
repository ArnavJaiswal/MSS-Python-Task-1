def calculate_discount(original_price, discount_percentage = 10):
    discounted_price = original_price - (original_price*discount_percentage / 100)
    return discounted_price


original_price = 100   
discounted_price = calculate_discount(original_price)

print(f"Original Price: {original_price}")
print(f"Discounted Price (10% discount): {discounted_price}")    
