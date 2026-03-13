'''Parking: charge per hours
Ask how many hours a car was in the parking lot.
Rules:
 first hour = 5000
 each additional hour = 3000
Show the total to pay.
Practice: conditionals and operations.'''

# Ask for hours from the user
hours = int(input('Enter the number of hours the car was in the parking lot: '))
# Calculate the total to pay according to the entered hours
if hours <= 1:
    total = 5000
else:
    total = 5000 + (hours - 1) * 3000
# Show the total to pay
print(f"The total to pay for {hours} hours in the parking lot is: {total} pesos.")
print("Thank you for your visit.")
print("Have a good day!")
print("Come back soon!")
print("Thank you for choosing our parking lot!")