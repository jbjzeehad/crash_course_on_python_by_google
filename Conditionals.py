# @ jbj_zeehad

# ==, =!, <, >, <=, >= return Boolean results.

print(5 + 10 == 6 + 7)

print(10 - 4 != 10 + 4)

print(9 / 3 != 3 * 1)

my_variable = 3 * 5
print(my_variable)
print(my_variable == 3 * 5)

print(11 > 3 * 3)

print(4 / 2 > 8 - 4)

print(4 / 2 < 8 - 4)

print(11 < 3 * 3)

print(12 * 2 >= 24)

print(18 / 2 >= 15)

print(12 * 2 <= 30)

print(15 <= 18 / 2)

# comparison operator with Strings

print("a string" == "a string")

print("4 + 5" == 4 + 5)

print("rabbit" != "frog")

event_city = "shanghai"
print(event_city != "shanghai")

print("three" == 3)

print("Lima" < "Lima")

# print("Five" < 6)

var1 = "my computer" >= "my chair"
var2 = "Spring" <= "Winter"
var3 = "pineapple" >= "pineapple"
print('Is "my computer" greater than or equal to "my chair"? Result: ', var1)
print('Is "Spring" less than or equal to "Winter"? Result: ', var2)
print('Is "pineapple" less than or equal to "pineapple"? Result: ', var3)

# comparison with logical operators

print((6 * 3 >= 18) and (9 + 9 <= 36 / 2))

print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")

print((15 / 3 < 2 + 4) or (0 >= 6 - 7))

country = "USA"
city = "New York City"
print(country == "New York City" or city == "New York City")

print(16 <= 4**2 or 9 ** (0.5) != 3)
print("A_name" > "B_name" or "B_name" > "C_name")
x = 2 * 3 > 6

print("The value of x is:")
print(x)
print("")
print("The inverse value of x is:")
print(not x)

today = "Monday"
print(not today == "Tuesday")

# comparison with if, elif, else block

# Use an if statement to calculate a return value
# Use conditional operators
# Recall the arithmetic operators // and %


def round_up(number):
    xx = 10
    whole_number = number // xx
    remainder = number % xx
    if remainder >= 5:
        return xx * (whole_number + 1)
    return xx * whole_number


print(round_up(35))

# Use an if-elif-else statement with:
# comparison operators
# logical operators

number = 25
if number <= 5:
    print("The number is 5 or smaller.")
elif number == 33:
    print("The number is 33.")
elif number < 32 and number >= 6:
    print("The number is less than 32 and greater than 6.")
else:
    print("The number is " + str(number))

# Use a function with the def() keyword
# Pass a parameter to the function
# Use an if-elif-else statement
# Assign strings to variables
# Use conditional operators
# Return a value


def translate_error_code(error_code):
    if error_code == "401 Unauthorized":
        translation = "Server received an unauthenticated request"
    elif error_code == "404 Not Found":
        translation = "Requested web page not found on server"
    elif error_code == "408 Request Timeout":
        translation = "Server request to close unused connection"
    else:
        translation = "Unknown error code"
    return translation


print(translate_error_code("404 Not Found"))

# Use a comparison operator with numbers
# Use a comparison operator to alphabetize strings

print(10 * 4 > 14 + 23)
print("tall" < "short")
