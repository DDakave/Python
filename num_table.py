#Que4. WAP to get table of a number using function

# Function to print the table of a number
def num_table(n):
    # Loop through numbers 1 to 10 to print the table
    for i in range(1, 11):
        print(num,"x",i,"=",n*i)

# Input from the user
num = int(input("Please enter a number to get its table:"))

# Call the function to print the table
num_table(num)
