#Que4. Perform intersection operation on list.

#Create two list

list1 = [23,35,88,65,75,90,87]
print("First List:",list1)
list2 = [67,35,87,23,67,90,77,56]
print("Second List:",list2)

#For intersection of two list
intersection_list = [set(list1) & set(list2)] 

#To print final list.
print("Final List=",intersection_list)
