# implement a dictionary named customer_info
customer_info = {
    'name': 'Arnav',
    'age': 19,
    'purchase_history': ['Iphone', 'Surface360', 'RogG18']
}

# retrieve and print the customer's name
customer_name = customer_info['name']
print(f"Customer's name: {customer_name}")

# retrieve and print the customer's second purchase from the purchase history
second_purchase = customer_info['purchase_history'][1]
print(f"Customer's second purchase: {second_purchase}")
