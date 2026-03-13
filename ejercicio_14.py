"""Cinema: room control
Ask for the total capacity of a cinema room and then register how many
people enter.
For each person ask age and classify:
 child
 adult
 senior
At the end show:
 total people entered
 how many children
 how many adults
 how many seniors
 if the room filled or not
Practice: loops with limit, counters."""
# Ask the user for the total capacity of the cinema room.
room_capacity = int(input("Enter the total capacity of the cinema room: "))
# Initialize counters for each age category and a total people counter.
children_counter = 0
adults_counter = 0
seniors_counter = 0
total_people_counter = 0
# Use a loop to register the entry of people until the room capacity is reached.
while total_people_counter < room_capacity:
    # Ask for the age of the entering person.
    age = int(input("Enter the age of the entering person: "))
    # Classify the person according to their age and update the corresponding counters.
    if age < 18:
        children_counter += 1
    elif 18 <= age < 60:
        adults_counter += 1
    else:
        seniors_counter += 1
    # Increment the total people counter.
    total_people_counter += 1
    # Check if the room has filled after each entry.
    if total_people_counter == room_capacity:
        print("The room has filled. No more people can enter.")
        break
# After finishing the people registration, show the results.
print(f"Total people entered: {total_people_counter}")
print(f"Number of children: {children_counter}")
print(f"Number of adults: {adults_counter}")
print(f"Number of seniors: {seniors_counter}")