print("Welcome")
name= input("Hello, what is your name:\n").strip()
num= float(input("enter the number you want to work with:\n"))
print("Simple Table")
for i in range(1,11):
    res=num*i
    print(f"{num}*{i}=",round(res,2))
print("Exponent Table")
for j in range(1,11):
    rest=num**j
    print(f"{num}**{j}=",round(rest,2))
    
print(f"{name} Math is fun!\n")
print(f"{name} Math is fun!\n".lower())
print(f"{name} Math is fun!\n".title())
print(f"{name} Math is fun!\n".upper())