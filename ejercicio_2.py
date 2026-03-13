"""Gym: access by age
A gym offers classes according to age:
 under 13 → cannot enter
 13 to 17 → youth class
 18 to 59 → general class
 60 or more → senior class
Ask for a person's age and show which group they belong to.
Practice: if, elif, else."""

# Ask for age from the user
age = int(input("Enter the person's age: "))
# Determine the class group according to age
if age < 13:
    print("Cannot enter the gym.")
elif 13 <= age <= 17:
    print("Belongs to the youth class.")
elif 18 <= age <= 59:
    print("Belongs to the general class.")
else:
    print("Belongs to the senior class.")