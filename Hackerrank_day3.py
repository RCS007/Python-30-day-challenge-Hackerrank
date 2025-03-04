# Task:-

# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
# and  tax percent (the percentage of the meal price being added as tax) for a meal,
# find and print the meal's total cost. Round the result to the nearest integer.


# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100  
    total = meal_cost + tip + tax 
    round(total) 
    print(str(round(total)))
    
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
