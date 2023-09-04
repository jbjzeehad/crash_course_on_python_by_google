# @ jbj_zeehad

name = "Sasha"
color = 'gold'
place = 'cambridge'
peter = "" # empty string
pet = "effffffffffffffffrgrgrgr" 
print("Name: " + name + ", Favorite color: " + color) #concatening
print("example" * 3)
print(len(pet))

# string indexing
# start from 0
print(name[1])
print(name[0])
print(name[4])
# print(name[6])
# string index out of range
text = "Random string with a lot of characters"
print(text[-1])
print(text[-2])
# reverse output : s r
# slice : the portion of a string that can contain more than one character also sometimes called substring

color = "orange"
print(color[1:4]) # output: ran ([1:4] from index 1 to 3 )
fruit = "pineapple"
print(fruit[:4]) # output : pine ([:4] from index 0 to 3)
print(fruit[4:]) #output : apple ([4:] from index 4 to end)

# strings in python are immutable
message = "A kong string with a silly typo"
# message[2]="l"
# print(message) Output: doesn't support item assignment
new_message = message[0:2] + "l" + message[3:]
print(new_message) 
# out: A long story with a silly typo

# methods: a function associated with a specific class
pets="Cats & Dogs"
print(pets.index("&"))
print(pets.index("s")) #out: first s which is 3
# print(pets.index("k")) out: substring not found 
# in >> True or False
print("Dragons" in pets) # out: false 
print("Cats" in pets) # out: True

# a real world example
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email