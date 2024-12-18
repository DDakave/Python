#Que1. WAP to get factorial of a number.

#using recursion function calling itself again and again

def factorial(n):
     # If the number is 0 the factorial is 1
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

n = int(input("please enter number:"))
ans = factorial(n)

# Checking if the number is non-negative
if n > 0:
    # Output the factorial of the number
    print("The factorial of",n,"is:",ans)
else:
    print("Factorial is not defined for negative numbers.")
    
