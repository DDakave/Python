n= int(input("Please enter number: "))
temp = n  #to store number
rev = 0

while(n>0):
    rem = n%10
    rev = rev*10+rem
    n = n//10

if(rev==temp):
    print("it is palindrome number")

else:
        print("it is not palindrome number")
