"""Recreational club: membership control
Register several people in a club.
For each one ask:
 name
 age
 plan type: basic, premium, family
Rules:
 basic = 50000
 premium = 90000
 family = 130000
Additionally:
 if the person is under 18, show "youth registration"
 if they are 60 or more, show "senior benefit"
At the end show:
 total collected
 number of people per plan
 most sold plan
Practice: conditionals, counters, accumulators."""
# Initialize the necessary counters and accumulators for membership registration.
total_collected = 0
basic_counter = 0
premium_counter = 0
family_counter = 0
# Use a loop to register several people. In this case, 10 people will be registered, but it can be adjusted as necessary.
for i in range(10): 
    # Ask for the person's name, age and plan type.
    name = input('Enter the person\'s name: ')
    age = int(input('Enter the person\'s age: '))
    plan_type = input('Enter the plan type (basic, premium, family): ')
    # Check the plan type and update the counters and accumulators accordingly.
    if plan_type.lower() == 'basic':
        total_collected += 50000
        basic_counter += 1
    elif plan_type.lower() == 'premium':
        total_collected += 90000
        premium_counter += 1
    elif plan_type.lower() == 'family':
        total_collected += 130000
        family_counter += 1
    else:
        print('Invalid plan type. Try again.')
        continue
    # Check if the person is under 18 years old or 60 or more years old to show the corresponding messages.
    if age < 18:
        print('Youth registration')
    elif age >= 60:
        print('Senior benefit')
# After registering the people, show the results.
print(f"Total collected: {total_collected} pesos.")
print(f"Number of people with basic plan: {basic_counter}")
print(f"Number of people with premium plan: {premium_counter}")
print(f"Number of people with family plan: {family_counter}")
# Determine which plan was the most sold.
if basic_counter > premium_counter and basic_counter > family_counter:
    most_sold_plan = 'basic'
elif premium_counter > basic_counter and premium_counter > family_counter:
    most_sold_plan = 'premium'
elif family_counter > basic_counter and family_counter > premium_counter:
    most_sold_plan = 'family'
else:
    most_sold_plan = 'tie between plans'
# Show which plan was the most sold.
print(f"The most sold plan is: {most_sold_plan}.")
