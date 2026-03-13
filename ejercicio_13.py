"""Register several orders in a cafeteria until the user writes
"exit".
Products:
 coffee = 4000
 cappuccino = 7000
 cake = 6000
Rules:
 if the purchase exceeds 20000, apply 10% discount
 if not, charge normal
Show total per customer and at the end total accumulated of the day.
Practice: simple menu, loops, discounts."""
# Product prices
coffee_price = 4000
cappuccino_price = 7000
cake_price = 6000
# Initialize the accumulator for the total of the day.
total_day = 0
# Enter an infinite loop to register orders until the user decides to exit.
while True:
    # Ask the user for the product they want to buy.
    product = input('Enter the product (coffee, cappuccino, cake) or "exit" to finish: ')
    # If the user wants to exit, break the loop.
    if product.lower() == 'exit':
        break
    # Ask for the quantity of units they want to buy.
    quantity = int(input('Enter the number of units: '))
    # Calculate the total per customer according to the chosen product.
    if product.lower() == 'coffee':
        total_customer = coffee_price * quantity
    elif product.lower() == 'cappuccino':
        total_customer = cappuccino_price * quantity
    elif product.lower() == 'cake':
        total_customer = cake_price * quantity
    else:
        print('Invalid product. Try again.')
        continue
    # Apply discount if the customer's total exceeds 20000 pesos.
    if total_customer > 20000:
        total_customer *= 0.9  # Apply a 10% discount
    # Show the total to pay for the customer.
    print(f"The total to pay for this customer is: {total_customer} pesos.")
    # Accumulate the total of the day with the current customer's total.
    total_day += total_customer
# After finishing the order registration, show the accumulated total of the day.
print(f"The accumulated total of the day is: {total_day} pesos.")
print("Thank you for your purchase. Have a good day!")
print("Come back soon to our cafeteria!")
print("Thank you for choosing our cafeteria! We hope to see you again soon.")