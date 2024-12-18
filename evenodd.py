#Que3. WAP to check wheather the number is even or not

#Take number as input from user

num = int(input("Please enter number:"))

if(num%2 == 0): #Condition to check given number is even or not.
    print(num,"is an even number.") #If condition is true then it display this statement.

else:
    print(num,"is not an even number.") #If condition is false then it display this statement.
