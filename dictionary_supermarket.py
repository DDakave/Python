#WAP to create dictionaries for below task and perform all the above operations on it.

#Each product in a supermarket is associated with its prize.

#Here we create dictionary of products and their prize.
my_dict = {"Rice" : "Rs.350",
           "Wheat" : "Rs.200",
            "Eggs":"Rs.70",
            "Milk" : "Rs.45"
          }

print(my_dict) #It will display all the elements present in the dictionary.

#To print values of particular keys.
x = my_dict["Wheat"] 
print("The price of the wheat is:")

x = my_dict.get("Rice")
print("The price of the Rice is:")

#To get all the keys present in the dictionary.

y = my_dict.keys()
print("The Products present in the dictionary:",y)

#To get all the values present in the dictionary.

z = my_dict.values()
print("The values present are:",z)

#To update dictionary element

my_dict.update({"Rice":"Rs.150"})
print(my_dict)

#To add new key and value in the dictionary
my_dict["Bread"] = "Rs.35"
my_dict["Chocolates"] = "Rs.100"

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
my_dict.pop("Eggs") #It will remove mentioned element from the dictionary
print(my_dict)
