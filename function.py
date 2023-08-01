# @ jbj_zeehad

# use a function that accepts multiple parameters
# Return a result value


def find_total_days(years, months, days):
    my_days = (years * 365) + (months * 30) + days
    return my_days


print(find_total_days(2, 5, 23))

# use a function to return the result of a measurement conversion
# use arithmetic operators to perform a calculation
# combine text with a function call within a print() statement
# convert the return value from a float data type to a string for the print() function
# call the function and perform a calculation on the return value within a print() statement


def convert_volume(fluid_ounce):
    ml = fluid_ounce * 29.5
    return ml


print("The volume in millimeters is " + str(convert_volume(2)))
print("The volume in millimeters is " + str(convert_volume(2) * 2))
