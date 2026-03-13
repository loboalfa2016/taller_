"""Hair Salon: Day Shift
Ask for the client's arrival time in integer format from 0 to 23.
Show:
 morning if between 6 and 11
 afternoon if between 12 and 17
 night if between 18 and 22
 out of hours in any other case
Practice: ranges with conditionals."""

# Ask for the arrival time from the user
hour = int(input('Enter the client\'s arrival time (0-23): '))
# Determine the day shift based on the entered hour
if 6 <= hour <= 11:
    shift = "morning"
elif 12 <= hour <= 17:
    shift = "afternoon"
elif 18 <= hour <= 22:
    shift = "night"
else:
    shift = "out of hours"
# Show the day shift to the user
print(f"The day shift for hour {hour} is: {shift}.")
print("Thank you for your visit.")
print("Have a good day!")
print("Come back soon!")
print("Thank you for choosing our hair salon!")