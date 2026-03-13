"""Ice cream shop: invoice for several customers
An ice cream shop wants to register several customers until the user
decides to exit.
Products:
 cone = 3000
 cup = 4000
 banana split = 9000
For each customer:
 ask for product
 ask for quantity
 calculate total
At the end show:
 total sold
 how many customers were served
 which product was ordered most times
Practice: loops, accumulators, counters."""

# Initialize counters and accumulators before starting to process data.
# `total_sold` will store the sum of all sales in pesos.
# `customer_counter` will keep count of how many customers were served.
# The following three counters will store how many units of each product were sold.
total_sold = 0
customer_counter = 0
cone_counter = 0
cup_counter = 0
banana_split_counter = 0

# Enter an infinite loop that will only break when the user writes "exit".
# This cycle represents serving customers one by one.
while True:
    # Ask the user for the type of product they want to buy.
    product = input('enter the product (cone, cup, banana split) or "exit" to finish: ')
    # If the user wants to finish, exit the loop.
    if product.lower() == 'exit':
        break
    # For any other value, ask for the quantity of units.
    quantity = int(input('enter the quantity: '))
    # According to the chosen product, calculate the price and update the counters.
    if product.lower() == 'cone':
        # Each cone costs 3000 pesos.
        total_sold += 3000 * quantity
        cone_counter += quantity
    elif product.lower() == 'cup':
        # Each cup costs 4000 pesos.
        total_sold += 4000 * quantity
        cup_counter += quantity
    elif product.lower() == 'banana split':
        # Each banana split costs 9000 pesos.
        total_sold += 9000 * quantity
        banana_split_counter += quantity
    else:
        # If the product is not recognized, notify and ask again.
        print('Invalid product. Try again.')
        continue
    # Count one more customer served (only if the product was valid).
    customer_counter += 1

# Once the customer registration is finished, decide which product was ordered most times.
if cone_counter > cup_counter and cone_counter > banana_split_counter:
    most_ordered_product = 'cone'
elif cup_counter > cone_counter and cup_counter > banana_split_counter:
    most_ordered_product = 'cup'
elif banana_split_counter > cone_counter and banana_split_counter > cup_counter:
    most_ordered_product = 'banana split'
else:
    # If there is a tie between two or more products, indicate that there is no clear winner.
    most_ordered_product = 'none, there is a tie'

# Finally show the summary of the day to the user.
print(f"Total sold: {total_sold} pesos.")
print(f"Number of customers served: {customer_counter}.")
print(f"Most ordered product: {most_ordered_product}.")
print("Thank you for your participation.")
print("Have a good day!")
print("Come back soon!")
print("Thank you for choosing our ice cream shop!")
print("We hope to see you again soon!")