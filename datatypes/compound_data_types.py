
#List, can be modified

list = ["Fernando", "I'm FRQ23", True, 1.75]
print(list[0])

#Modifies the first element.

list[0] = "Not Fernando"
print(list[0])

#tuples, can't be modified

tuple =("Fernando", "I'm FRQ23", True, 1.75)

#just for explaining, uncomment and see the error.

#list[3] = 1.90 
print(tuple[3])


#Creating a set (conjunto in spanish)
#Same properties of a set in maths
#can't call the elements using an index and doesn't store duplicated elements
set = {"Fernando", "I'm FRQ23", True, 1.75}



#Creating a dictionary

dictionary = {
    'name' : "Fernando",
    'who_you_are' : "I'm FRQ23",
    'excited' : True,
    'height' : 1.75,
    'duplicated_data' : "I'm FRQ23"
}

print(dictionary['name'])