#Que4. WAP to accept basic salary from user and give 10% of DA on basic salary, 12% HRA on basic salary to employee if the salary is more than 50000.
#Calculate total salary.

#Take salary as input from user.
salary = int(input("Please enter your salary:"))

if(salary > 50000):#Condition to check salary is greater than 50000 or not.

    #if salary is greater than 50000.
    da = (salary*10)/100 #formula to calculate da on basic salary.
    
    hra = (salary*12)/100 #formula to calculate hra from basic salary.
    
    total_salary = salary+da+hra #Formula to calculate total salary

    print("Your total salary is:Rs",total_salary)

else:
    print("Your salary is not more than 50000.") #If condition is false then display this statement.
