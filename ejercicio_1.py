"""An ice cream shop wants to register 5 orders.
For each customer, the program must ask for the chosen flavor:
 vanilla
 chocolate
 strawberry
At the end it must show how many times each flavor was ordered.
Practice: loops, conditionals, counters."""

# Initialize counters
vanilla_counter = 0
chocolate_counter = 0
strawberry_counter = 0

# Register orders
for i in range(5):
    flavor = input("enter the chosen flavor (vanilla, chocolate, strawberry): ").lower()
    if flavor == "vanilla":
        vanilla_counter += 1
    elif flavor == "chocolate":
        chocolate_counter += 1
    elif flavor == "strawberry":
        strawberry_counter += 1
    else:
        print("Invalid flavor. Please enter a valid flavor.")

# Show results
print(f"Number of vanilla orders: {vanilla_counter}")
print(f"Number of chocolate orders: {chocolate_counter}")
print(f"Number of strawberry orders: {strawberry_counter}")
