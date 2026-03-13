"""Pet store: sales by category
Register sales of a pet store.
Categories:
 food
 toy
 accessory
Ask for 10 sales. In each sale:
 category
 purchase value
At the end show:
 how much was sold per category
 which category generated more money
Practice: separate accumulators."""
# Initialize the accumulators for each sales category.
total_food = 0
total_toy = 0
total_accessory = 0
# Use a loop to register 10 sales.
for i in range(10):
    # Ask for the sales category and the purchase value.
    category = input('Enter the sales category (food, toy, accessory): ')
    purchase_value = float(input('Enter the purchase value: '))
    # Accumulate the total sold per category according to the user input.
    if category.lower() == 'food':
        total_food += purchase_value
    elif category.lower() == 'toy':
        total_toy += purchase_value
    elif category.lower() == 'accessory':
        total_accessory += purchase_value
    else:
        print('Invalid category. Try again.')
# After registering the sales, show how much was sold per category.
print(f"Total sold in food: {total_food} pesos.")
print(f"Total sold in toy: {total_toy} pesos.")
print(f"Total sold in accessory: {total_accessory} pesos.")
# Determine which category generated more money.
if total_food > total_toy and total_food > total_accessory:
    category_highest_sale = 'food'
elif total_toy > total_food and total_toy > total_accessory:
    category_highest_sale = 'toy'
elif total_accessory > total_food and total_accessory > total_toy:
    category_highest_sale = 'accessory'
else:
    category_highest_sale = 'tie between categories'
# Show which category generated more money.
print(f"The category that generated more money is: {category_highest_sale}.")

