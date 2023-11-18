"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
"""
1. Sales Bonus
"""
SALES_BONUS_THRESHOLD = 1000
LOW_THRESHOLD_DISCOUNT_RATE = 0.10  # 10%
HIGH_THRESHOLD_DISCOUNT_RATE = 0.15  # 15%
sales = float(input("Enter Sales: $ "))
while sales >= 0:
    if sales < SALES_BONUS_THRESHOLD:

        discount_rate = LOW_THRESHOLD_DISCOUNT_RATE
    else:
        discount_rate = HIGH_THRESHOLD_DISCOUNT_RATE
    bonus = sales * discount_rate
    print(f"Bonus: ${bonus}")
    sales = float(input("Enter Sales: $ "))
