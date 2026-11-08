# Module 11 Lab 1: Customer Dictionary


print( "--- Exercise 1 ---" )
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400.00
}

print(customer["name"])  # Output: Alice
print(customer["email"])  # Output: alice@example.com
print(customer["tier"])  # Output: gold
print(customer["ytd_spend"])  # Output: 12400.00

print( "--- Exercise 2 ---" )
customer["phone"] = "555-5555" 
print(customer)
customer['tier'] = "platinum"
print(customer)
del customer["email"]
print(customer)


print(customer.get('ytd_spend', 0))
      

print( "--- Exercise 3 ---" )
print(customer.get("email", "Email not found"))

print( "--- Exercise 4 ---" )
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

print( "--- Exercise 5 ---" )
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
purchase = 200
discount = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount)
print(f"Tier; {customer['tier']}")
print(f"Discount: {discount * 100}%")
print(f"Final Price: ${final_price:.2f}")
#Reflection
#1. .get() is more efficient than using the [] because it is human readable. It also makes it easy to change if necessary. You will use .get() if you need to change prices/discounts. Bracket notation is more efficient if you are just looking for a value and not changing it.