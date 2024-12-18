#WAP to create dictionaries for below task and perform all the above operations on it.

#Each student in a school is associated with their Grade.

#Here we create dictionary of Student Name and their Grade.
my_dict = {"Sai Patil" : "A Grade",
           "Neha More" : "O Grade",
            "Rahul Mehra" : "C Grade",
            "Nayana Shah" : "B Grade"
          }

print(my_dict) #It will display all the elements present in the dictionary.

#To print values of particular keys.
x = my_dict["Neha More"] 
print("The student get:",x)

x = my_dict.get("Nayna Shah")
print("The student get:",x)

#To get all the keys present in the dictionary.

y = my_dict.keys()
print("Students Name present in the dictionary:",y)

#To get all the values present in the dictionary.

z = my_dict.values()
print("The values present are:",z)

#To update dictionary element

my_dict.update({"Rahul Mehra":"A Grade"})
print(my_dict)

#To add new key and value in the dictionary
my_dict["Rutuja Salvi"] = "C Grade"
my_dict["Mukesh Patel"] = "D Grade"

print(my_dict)

#To remove element from the dictionary

my_dict.popitem() #It will remove last element from the dictionary
print(my_dict)

#looping over dictionary

for i in my_dict:
        print(i)

#To get all keys from the dictionary

for i in my_dict.keys():
        print(i)

#To get all values from the dictionary

for i in my_dict.values():
        print(i)

#To get both keys and values from the dictionary

for x,y in my_dict.items():
        print(x,y)

#To remove particular element from the dictionary
my_dict.pop("Rutuja Salvi") #It will remove mentioned element from the dictionary
print(my_dict)
