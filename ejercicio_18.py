"""Language center: student evaluation
Register several students from an English course.
For each one ask:
 name
 speaking grade
 listening grade
 reading grade
Calculate simple average and classify:
 less than 60 → low
 60 to 79 → medium
 80 or more → high
At the end show:
 group general average
 best student
 how many stayed in each level
Practice: averages, maximums, counters."""

# Initialize the necessary counters and accumulators for student registration.
total_students = 0
sum_averages = 0
low_counter = 0
medium_counter = 0
high_counter = 0
best_student = ""
best_average = 0
# Use a loop to register students. The loop will stop when the user decides not to enter more students.
while True:
    # Ask for the student's name.
    name = input('Enter the student\'s name: ')
    # Ask for the speaking, listening and reading grades.
    speaking_grade = float(input('Enter the speaking grade: '))
    listening_grade = float(input('Enter the listening grade: '))
    reading_grade = float(input('Enter the reading grade: '))
    # Calculate the simple average of the three grades.
    average = (speaking_grade + listening_grade + reading_grade) / 3
    # Accumulate the total of averages to calculate the group general average later.
    sum_averages += average
    total_students += 1
    # Classify the student according to their average and update the corresponding counters.
    if average < 60:
        low_counter += 1
    elif 60 <= average < 80:
        medium_counter += 1
    else:
        high_counter += 1
    # Check if this student has the best average recorded so far.
    if average > best_average:
        best_average = average
        best_student = name
    # Ask the user if they want to enter another student.
    continue_input = input('Do you want to enter another student? (y/n): ')
    if continue_input.lower() != 'y':
        break
# After finishing the student registration, calculate the group general average and show the results.
general_average = sum_averages / total_students if total_students > 0 else 0
print(f"Group general average: {general_average:.2f}")
print(f"Best student: {best_student} with an average of {best_average:.2f}")
print(f"Number of students with low level: {low_counter}")
print(f"Number of students with medium level: {medium_counter}")
print(f"Number of students with high level: {high_counter}")