# 1. Sales Bonus

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

below_threshold_bonus_rate = 0.10
above_threshold_bonus_rate = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * below_threshold_bonus_rate
    else:
        bonus = sales * above_threshold_bonus_rate
    print(f"Your bonus is ${bonus}")
    sales = float(input("Enter sales: $"))
print("You have entered an invalid negative number.")
