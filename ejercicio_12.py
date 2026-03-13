"""Register 5 people in a gym.
For each one ask:
 name
 days attended in the week
 average minutes trained per day
Classify:
 less than 3 days → low commitment
 3 to 4 days → medium commitment
 5 or more → high commitment
At the end show how many people fell into each category.
Practice: loops, counters, conditionals."""
# Initialize the counters for each commitment category.
low_commitment = 0
medium_commitment = 0
high_commitment = 0
# Use a loop to register 5 people.
for i in range(5):
    # Ask for the person's name (although it won't be used for classification).
    name = input('Enter the person\'s name: ')
    # Ask for the days attended per week and the average minutes trained per day.
    attended_days = int(input('Enter the days attended in the week: '))
    trained_minutes = int(input('Enter the average minutes trained per day: '))
    # Classify commitment according to attended days.
    if attended_days < 3:
        low_commitment += 1
    elif 3 <= attended_days <= 4:
        medium_commitment += 1
    else:
        high_commitment += 1
# After registering the 5 people, show how many fell into each category
print(f"People with low commitment: {low_commitment}")
print(f"People with medium commitment: {medium_commitment}")
print(f"People with high commitment: {high_commitment}")