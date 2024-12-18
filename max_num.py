#Que2. WAP to find maximum among two number.

# Function to find the maximum of two numbers
def maximum_num(num1, num2):
    if num1 > num2:
       return num1
    else:
        return num2

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#To display the output
print("The maximum number between",num1,"and",num2,"is:",maximum_num(num1,num2))
