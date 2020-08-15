import cmath 
print("Welcome!")

print("Quadratic Equation is always in the format ax^2 + bx + c = 0 \nYour Solution might be in Real or Complex numbers \nA complex numbers has two parts a +bj \nWhere a is the real portion, bj is the imaginary portion. \n ")
times = int(input("How many equations would you like to Solve??: "))
for i in range(times):
    print(f"\nSolving Equation#{i+1}\n")
    a = float(input("\nPlease enter your value of a (co-efficient of x^2): "))
    b = float(input("\nPlease enter your value of a (co-efficient of x): "))
    c = float(input("\nPlease enter your value of a (co-efficient): "))
    print(f"the solutions to ({a} x^2) + ({b} x) + ({c}) = 0  are:")
    root1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    root2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
    print(f"\n \t root1 = {root1} \n \t root2 = {root2}")
    
