n = int(input("Please enter number:"))
rev = 0
while(n>0):
    rem = n%10
    rev = rev*10+rem
    n = n//10


print("The reversed number is: ",rev)