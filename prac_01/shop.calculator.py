"""
Shop Calculator
"""
DISCOUNT_RATE = 0.1  # 10%
PRICE_THRESHOLD_FOR_DISCOUNT = 100
total_price = 0
number_of_item = int(input("Number of items: "))
while number_of_item < 0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of items: "))
for item in range(1, number_of_item+1):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price >= 100:
    discount_amount = total_price * DISCOUNT_RATE
    total_price = total_price - discount_amount
print(f"Total price for {number_of_item} items is ${total_price:.2f}")
