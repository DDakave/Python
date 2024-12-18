#Que1. WAP to find greatest amomg two numbers.

#Take two numbers from user as input
num1 = int(input("Please enter first number:"))
num2 = int(input("Please enter second number:"))

#Compairing given numbers 
if(num1 > num2): #condition to check num 1 is greatest or not
    print("The greatest number is:",num1) #if condition is true it will print this statement.

#if given condition is false then print below statement
else:
    print("The greatest number is:",num2)
