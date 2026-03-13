"""Parking: vehicle control
Register 8 vehicles in a parking lot.
For each one ask:
 plate
 type: car or motorcycle
 hours parked
Rates:
 car: 4000 per hour
 motorcycle: 2000 per hour
At the end show:
 total collected
 how many cars entered
 how many motorcycles entered
 which vehicle paid more
Practice: loops, maximums, accumulators."""
# Initialize the necessary counters and accumulators for vehicle registration.
total_collected = 0
cars_counter = 0
motorcycles_counter = 0
max_payment = 0
vehicle_highest_payment = ""
# Use a loop to register 8 vehicles.
for i in range(8):
    # Ask for the vehicle's plate.
    plate = input('Enter the vehicle\'s plate: ')
    # Ask for the vehicle type (car or motorcycle).
    type = input('Enter the vehicle type (car or motorcycle): ')
    # Ask for the hours the vehicle was parked.
    parked_hours = int(input('Enter the parked hours: '))
    # Calculate the payment according to the vehicle type and update the counters and accumulators.
    if type.lower() == 'car':
        payment = 4000 * parked_hours
        cars_counter += 1
    elif type.lower() == 'motorcycle':
        payment = 2000 * parked_hours
        motorcycles_counter += 1
    else:
        print('Invalid vehicle type. Try again.')
        continue
    # Accumulate the total collected with the current vehicle's payment.
    total_collected += payment
    # Check if this vehicle paid more than the maximum recorded so far.
    if payment > max_payment:
        max_payment = payment
        vehicle_highest_payment = plate
# After finishing the vehicle registration, show the results.
print(f"Total collected: {total_collected} pesos.")
print(f"Number of cars entered: {cars_counter}")
print(f"Number of motorcycles entered: {motorcycles_counter}")
print(f"The vehicle that paid the most is: {vehicle_highest_payment} with a payment of {max_payment} pesos.")