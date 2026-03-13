"""Sports store: count expensive products
Ask for the price of 6 sports products.
At the end indicate how many cost more than 100000.
Practice: loop, counter, conditional."""

# Initialize counter for expensive products
expensive_counter = 0
# Ask for prices of 6 products from the user
for i in range(6):
    price = float(input(f'Enter the price of product {i + 1}: '))
    # Check if the product costs more than 100000
    if price > 100000:
        expensive_counter += 1
# Show the number of expensive products to the user
print(f"The number of products that cost more than 100000 is: {expensive_counter}.")
print("Thank you for your visit.")
print("Have a good day!")
print("Come back soon!")
print("Thank you for choosing our sports store!")
print("We hope to see you again soon!")