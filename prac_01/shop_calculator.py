# 4. Shop Calculator

"""
Pseudocode:

total price = 0
discount rate = 0.10

get number of items
while number of items < 0
    print Invalid
    get number of items
for each item in number of items
    get price of item
    total price = total price * price of item
if total price > 100
    total price = total price * (1 - discount rate)
print number of items, total price

"""
total_price = 0
discount_rate = 0.10

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > 100:
    total_price = total_price * (1-discount_rate)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")


