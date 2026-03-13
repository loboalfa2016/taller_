"""Cafeteria: total of a simple purchase
In a cafeteria they sell:
 coffee = 4000
 tea = 3500
 juice = 5000
Ask the user what drink they want and how many units they want to buy.
Then show the total to pay.
Practice: conditionals, variables, multiplication."""

# Drink prices
coffee_price = 4000
tea_price = 3500
juice_price = 5000

# Ask for drink and quantity from the user
drink = str(input("Enter the drink you want to buy (coffee, tea, juice): ")).lower()
quantity = int(input("Enter the number of units you want to buy: "))
# Calculate the total to pay according to the selected drink
if drink == 'coffee':
    total = coffee_price * quantity
elif drink == 'tea':
    total = tea_price * quantity
elif drink == 'juice':
    total = juice_price * quantity
else:
    total = 0
    print("Invalid drink. Please enter a valid drink.")
# Show the total to pay
if total > 0:
    print(f"The total to pay for {quantity} units of {drink} is: {total} pesos.")   
