# Que1. Create dynamic list where you will ask user to enter 5 elements in it and perform
# insert new element and delete an element operation on it.

#Here we create empty list.
list1 = []

#Number of elements as input
print("Please enter 5 elements in list:")

#Here we use for loop for iteration till the range
for i in range(0, 5):
        elements = int(input())
        # To add the elements we use append() function.
        list1.append(elements)

#To print the current list
print("List=",list1)

#To perform insert operation

insert_value = input("Please enter value to insert:")
insert_position = int(input("Please enter position to insert the value(0 to{len(list1)}):"))
list1.insert(insert_position,insert_value)
print("List after insertion:",list1)

#To perform delete operation
delete_value = int(input("Please enter value to delete:"))

list1.remove(delete_value)
print("List after deletion:",list1)

