# @ jbj_zeehad

#while loops

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(5)

def count_down( start_number):
    current = 5
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")
count_down(3)

#prints the multiples of 5 between 1 and 50

multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")

#initialize a variable
#use a while loop that runs while a specific condition is true
#ensure the while loop will not be an infinite loop
#increment a value within a while loop

def count_factors(given_number):
    factor = 1
    count = 1
    if given_number == 0:
        return 0
    while factor < given_number:
        if given_number % factor == 0:
            count += 1
        factor += 1
    return count
print(count_factors(0))
print(count_factors(3))
print(count_factors(10))
print(count_factors(24))

#initialize variables to assign data types before they are used in a while loop
#use the break keyword as an exit point for a while loop

def addition_table(given_number):
    iterated_number = 1
    my_sum = 1
    while iterated_number <= 5:
        my_sum = given_number + iterated_number
        if my_sum > 20:
            break
        print(str(given_number),"+",str(iterated_number),"=",str(my_sum))
        iterated_number +=1
addition_table(5)
addition_table(17)
addition_table(30)

