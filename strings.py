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
