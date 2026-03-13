"""Pet store: food by animal type
Ask for the type of pet:
 dog
 cat
 rabbit
Then show a food recommendation according to the animal.
Practice: text comparisons."""

# Ask for pet type from the user
pet = input("Enter the type of pet (dog, cat, rabbit): ").lower()
# Show food recommendation according to pet type
if pet == "dog":
    print("Recommendation: Food for dogs.")
elif pet == "cat":
    print("Recommendation: Food for cats.")
elif pet == "rabbit":
    print("Recommendation: Food for rabbits.")
else:
    print("Invalid pet type. Please enter a valid pet type.")