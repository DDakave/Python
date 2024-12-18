# Que 1: WAP to calculate simple interest

#Take principle amount and number of years from user 
principle_amount= int(input("Please enter principle amount: "))
years = int(input("Please enter Number of Years: "))

#Rate of interest is constant
rate_of_interest = 12

#Formula To calculate simple interest
simple_interest = (principle_amount*years*rate_of_interest)/100

##Display Simple interest i.e total amount user need to pay
print('You need to pay RS.',simple_interest)
