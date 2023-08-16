
# @ jbj_zeehad

#for loop

for x in range(5):
    print(x)
   
friends = ['Taylor','Alex','Pat','Eli']
for friend in friends:
    print("Hi "+ friend)
  
values = [23,52,59,37,48]
sum = 0
length = 0
for value in values:
    sum += value
    length +=1
print("Total sum: "+ str(sum) + " , Average: " + str(sum/length))

product = 1
for x in range(1,10):
    product = x * product
print(product)

def to_celsius(a):
    return (a-32)*5/9
for c in range (0,101,10):
    print(c,to_celsius(c))
    
for d in [25]:
    print(d)

    
# This code demonstrates the outer and inner loop iterations of a pair 
# of nested for loops. Click "Run" to see the results. The outer loop
# will run twice for the range pointer positions [0, 1] in range(2).
# The inner loop will run 4 times for the range pointer positions 
# [0, 1, 2, 3] in range(3+1) or range(4) each time the outer loop runs.
# So, the inner loop will execute 8 times in total.

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")

# Recursion 

def factorial (n):
    if n < 2:
        return 1
    return n * factorial(n-1) # recursive case

#def recursive_function(parameters):
#    if base_case_condition(parameters):
#        return base_case_value
#    recursive_function(modified_parameters)

# use a for loop with the range() function with the end of range value included in the range

def count_by_10(end):
    for number in range(0,end+1,10):
        count += str(number) + " "
    return count.strip()
print(count_by_10(100)) # output : 0 10 20 30 40 50 60 70 80 90 100

# use a set of nested for loops with the range() function to create a matrix of numbers
# include the upper range value in the range() function using end + 1

def matrix(initial_number, end_of_first_row):
    n1 = initial_number 
    n2 = end_of_first_row+1
    
    for column in range(n1, n2):
        for row in range(n1, n2):
            print(column*row, end=" ")
    print()
matrix(1,4)
# output : 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

# predict the final value of a nested for loop with range() function

for outer_loop in range(10):
    for inner_loop in range(outer_loop):
        print(inner_loop)
        
# use a while loop to print a sequence of numbers

while starting_number >= 0:
    print(starting_number, end=" ")
    starting_number -= 3 # output : 18 15 12 9 6 3 0 
    
# use a while loop to count the number of digits in a numerical value

def X_figure(salary):
    tally = 0
    if salary == 0:
        tally += 1
    while salary >= 1:
        salary = salary/10
        tally += 1
    return tally

print("The CEO has a " + str(X_figure(2300000)) + "-figure salary.")

# use a function to accept two variable integers
# use nested if else statements and while loops to count up or count down from the first variable to the second variable

def elevator_floor(enter, exit):
    floor = enter
    elevator_direction = ""
    if enter > exit:
        elevator_direction = "Going down: "
        while floor >= exit:
            elevator_direction += str(floor)
            if floor > exit:
                elevator_direction += " | "
            floor -= 1
    else:
        elevator_direction = "Going up: "
        while floor <= exit:
            elevator_direction += str(floor)
            if floor < exit:
                elevator_direction += " | "
            floor += 1
    return elevator_direction
print(elevator_floor(1,4)) # Going up: 1 | 2 | 3 | 4
print(elevator_floor(6,2)) # Going down: 6 | 5 | 4 | 3 | 2
