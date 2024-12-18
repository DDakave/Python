#Que1. WAP to get Area of Rectangle.

def area_rect(length,breadth):
    area = length*breadth
    print("Area of the rectangle is:",area)


length = int(input("Please enter the length:"))
breadth = int(input("Please enter the breadth:"))

#to call the function
area_rect(length, breadth)
