#Que3. WAP to find maximum among two number.

#Function to check if a person can vote
def vote_eligibility(age):
    if age >= 18:
        return True
    else:
        return False

# Input from the user
age = int(input("Please enter your age: "))

# Check if the person can vote and display the result
if vote_eligibility(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
