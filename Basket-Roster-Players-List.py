
print("Welcome!")
res = {}
Point_Guard = str(input("Enter your point guard name: ")).title()
res["Point_Guard"] = Point_Guard
Shooting_Guard = str(input("Enter your Shooting_Guard name: ")).title()
res["Shooting_Guard"] = Shooting_Guard
Small_Forward = str(input("Enter your Small_Forward name: ")).title()
res["Small_Forward"] = Small_Forward
Power_Forward = str(input("Enter your Power_Forward name: ")).title()
res["Power_Forward"] = Power_Forward
Center = str(input("Enter your Center name: ")).title()
res["Center"] = Center

for key,values in res.items():
    print(f"{key} : {values}")

injured = (list(res)[1])
print(injured)
print(f"Oh! No {injured} is injured!")
print("you only have 4 rosters now: ")
replace = str(input(f"Who will take{injured} place now :")).title()
res[injured]=replace
for key, values in res.items():
    print(f"{key} : {values}")
