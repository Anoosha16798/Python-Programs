
import math as m
print("Welcome")
a=float(input("Enter first leg of a triangle\n"))
b=float(input("Enter second leg of a triangle\n"))
hyp=m.sqrt((a**2)+(b**2))
area=(a*b)/2
print("Hypotenuse of a right angle triangle",round(hyp,2))
print("Area of a right angle triangle",round(area,2))