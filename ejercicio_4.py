"""Entry according to age
The entry price changes like this:
 children under 12 → 8000
 adults from 12 to 59 → 12000
 seniors over 60 → 9000
Ask for the client's age and show how much they must pay.
Practice: conditionals."""

# Ask for age from the user
age = int(input("Enter the client's age: "))
# Determine the entry price according to age
if age < 12:
    price = 8000
elif 12 <= age <= 59:
    price = 12000
else:
    price = 9000
# Show the price to pay
print(f"The client must pay: {price} pesos.")
print("Thank you for your purchase.")
print("Enjoy your visit!")