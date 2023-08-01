# @ jbj_zeehad

# use the assignment operator = to assign values to variables
# use basic arithmetic operators with variables to create expressions
# use explicit conversion to change a data type from float to string

hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total / room_guests

print("Each person needs to pay: " + str(share_per_person))

# output multiple string variables on a single line to form a sentence
# use the plus connector or a comma to connect strings in a print() function
# Create spaces between variables in a print() function

salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D"

print(
    salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix
)
print(salutation, first_name, middle_name, last_name, ",", suffix)

# Resolve typeError caused by a data type mismatch issue
# Use an explicit conversion function

print("5 * 3 = " + str(5 * 3))

# Resolve a ZeroDivisionError caused by an attempt to divide by 0

numerator = 7
denominator = 0
result = numerator / denominator
print(result)
