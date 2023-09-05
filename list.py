
# @ jbj_zeehad

# list

x =["now","we","are","cooking!"]
print(type(x))
print(x)
print(x[1]) # if not found index errror
print(len(x))
print("are" in x)
print("today" in x)
print(x[1:3])  
print(x[:3])  
print(x[2:])  
# append method
fruits=["pineapple","Banana","Apple","Melon"]
fruits.append("kiwi")
print(fruits)
# insert method
fruits.insert(0,"orange")
print(fruits)
fruits.insert(25,"peach")
print(fruits)
# remove method
fruits.remove("Apple")
print(fruits)
fruits.pop(3)
print(fruits)
# fruits.remove("lemon")
# print(fruits) # error
