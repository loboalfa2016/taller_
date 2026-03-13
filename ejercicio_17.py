"""Hair Salon: attention schedule
A hair salon serves 7 clients per day.
For each client ask:
 name
 requested service: cut, brushing, dyeing
 value paid
At the end show:
 total of the day
 number of clients per service
 most requested service
Practice: counters, accumulators, comparisons."""
# Initialize the necessary counters and accumulators for client registration.
total_day = 0
cut_counter = 0
brushing_counter = 0
dyeing_counter = 0
# Use a loop to register 7 clients.
for i in range(7):
    # Ask for the client's name (although it won't be used for classification).
    name = input('Enter the client\'s name: ')
    # Ask for the requested service and the value paid.
    service = input('Enter the requested service (cut, brushing, dyeing): ')
    value_paid = float(input('Enter the value paid: '))
    # Accumulate the total of the day with the value paid by the current client.
    total_day += value_paid
    # Count the number of clients per service according to the user input.
    if service.lower() == 'cut':
        cut_counter += 1
    elif service.lower() == 'brushing':
        brushing_counter += 1
    elif service.lower() == 'dyeing':
        dyeing_counter += 1
    else:
        print('Invalid service. Try again.')
# After registering the clients, show the total of the day and the number of clients per service.
print(f"Total of the day: {total_day} pesos.")
print(f"Number of clients for cut: {cut_counter}")
print(f"Number of clients for brushing: {brushing_counter}")
print(f"Number of clients for dyeing: {dyeing_counter}")
# Determine which service was the most requested.
if cut_counter > brushing_counter and cut_counter > dyeing_counter:
    most_requested_service = 'cut'
elif brushing_counter > cut_counter and brushing_counter > dyeing_counter:
    most_requested_service = 'brushing'
elif dyeing_counter > cut_counter and dyeing_counter > brushing_counter:
    most_requested_service = 'dyeing'
else:
    most_requested_service = 'tie between services'
# Show which service was the most requested.
print(f"The most requested service is: {most_requested_service}.") 