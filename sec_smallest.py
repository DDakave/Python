#Que3. WAP to find second smallest element in the list.

#Create one list

list1 = [78,69,44,58,36,78,44,27]

#To sort the list we need to remove duplicate values from list.
#For removing duplicate values we need to convert list into set.

remove_dup = (list(set(list1)))
print("The final list is=",remove_dup)

#To sort the list
sorted_list = sorted(remove_dup)
print("The sorted list is=",sorted_list)

#To find second smallest element from the sorted list.

sec_smallest = sorted_list[1]
print("The second smallest element from the given list is:",sec_smallest)


