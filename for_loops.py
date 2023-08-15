
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