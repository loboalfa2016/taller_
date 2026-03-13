"""Sports clothing store: critical inventory
Register 10 products.
For each product ask:
 name
 available quantity
Classify:
 0 → out of stock
 1 to 5 → low stock
 6 or more → normal stock
At the end show:
 how many are out of stock
 how many have low stock
 how many are normal
Practice: classification by ranges, loop."""
# Initialize the counters for each stock category.
out_of_stock_counter = 0
low_stock_counter = 0
normal_stock_counter = 0
# Use a loop to register 10 products.
for i in range(10):
    # Ask for the product name (although it won't be used for classification).
    product_name = input('Enter the product name: ')
    # Ask for the available quantity of the product.
    available_quantity = int(input('Enter the available quantity: '))
    # Classify the stock according to the available quantity.
    if available_quantity == 0:
        out_of_stock_counter += 1
    elif 1 <= available_quantity <= 5:
        low_stock_counter += 1
    else:
        normal_stock_counter += 1
# After registering the products, show how many are out of stock, have low stock and are normal.
print(f"Out of stock products: {out_of_stock_counter}")
print(f"Products with low stock: {low_stock_counter}")
print(f"Products with normal stock: {normal_stock_counter}")   
