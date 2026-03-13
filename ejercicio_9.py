"""Spa: available service
In a spa there are these services:
 massage
 facial
 manicure
Ask the user what service they want and show a message confirming
if it exists or not.
Practice: conditionals with text."""
# Ask for service from the user
service = input('Enter the service you want (massage, facial, manicure): ').lower()
# Check if the service exists and show confirmation message
if service == "massage":
    print("Massage service available. Enjoy your experience!")
elif service == "facial":
    print("Facial service available. Enjoy your experience!")
elif service == "manicure":
    print("Manicure service available. Enjoy your experience!")
else:
    print("Service not available. Please choose a valid service.")
print("Thank you for your visit.")
print("Have a good day!")
print("Come back soon!")
print("Thank you for choosing our spa!")
print("We hope to see you again soon!")
print("Enjoy your day at our spa!")
