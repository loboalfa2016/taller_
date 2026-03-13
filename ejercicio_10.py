"""Dance academy: attendance
Ask for the number of classes attended by a student in a month.
Rules:
 less than 5 → low attendance
 between 5 and 8 → medium attendance
 9 or more → high attendance
Practice: classification by ranges."""

# Ask for the number of classes attended from the user
attended_classes = int(input('Enter the number of classes attended by the student in a month: '))
# Classify attendance according to the established rules
if attended_classes < 5:
    attendance = "low"
elif 5 <= attended_classes <= 8:
    attendance = "medium"
else:
    attendance = "high"
# Show the attendance classification to the user
print(f"The student's attendance is: {attendance}.")
print("Thank you for your participation.")
print("Have a good day!")
print("Come back soon!")
print("Thank you for choosing our dance academy!")
print("We hope to see you again soon!")