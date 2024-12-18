#WAP to create dictionaries for below task and perform all the above operations on it.

#Each customer ID in a company associated with a customer name.

#Here we create dictionary of Customer ID and Customer Name.
my_dict = {"K101": "Sai Patil",
           "P123" : "Neha More",
           "P658" : "Rahul Mehra",
           "S741" : "Nayana Shah"
          }

print(my_dict) #It will display all the elements present in the dictionary.

#To print values of particular keys.
x = my_dict["P123"] 
print("Customer name is:",x)

x = my_dict.get("S741")
print("Customer name is:",x)

#To get all the keys present in the dictionary.

y = my_dict.keys()
print("Customer ID present in the dictionary:",y)

#To get all the values present in the dictionary.

z = my_dict.values()
print("The Customer Name present in the dictionary:",z)

#To update dictionary element

my_dict.update({"P658":"Rohit Mehra"})
print(my_dict)

#To add new key and value in the dictionary
my_dict["T789"] = "Rutuja Salvi"
my_dict["K813"] = "Mukesh Patel"

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
my_dict.pop("P123") #It will remove mentioned element from the dictionary
print(my_dict)
