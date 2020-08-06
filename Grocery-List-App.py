print("Welcome!")
print("You have Cheese and Meet in your cart!")
cart = ["Cheese","Meet"]
num=str(input("Enter the items you want to add :"))
prod=[]
cart.append(num)
num1 = str(input("Enter the items you want to add :")).lower()
cart.append(num1)
num2 = str(input("Enter the items you want to add :")).lower()
cart.append(num2)
cart = [data.title() for data in cart]
print("no of items", len(cart))
print("Your cart is with items\n",cart,"\n",sorted(cart))
buy = str(input("item you wanna buy :")).title()
buy1 = str(input("item you wanna buy :")).title()
if buy in cart:
    cart.remove(buy)
    prod.append(buy)
else:
    print(f"item{buy} not present in the list")
    new_buy = str(input("Add new item")).title()
    cart.append(new_buy)
    prod.append(new_buy)

if buy1 in cart:
    cart.remove(buy1)
    prod.append(buy1)
else:
    print(f"item{buy1} not present in the list")
    new_buy1 = str(input("Add new item")).title()
    cart.append(new_buy1)
    prod.append(new_buy1)

print("Your list now contains :"+ str(len(cart))+ "items\n"+ str(cart))
no_food = cart.pop()
print(f"Sorry {no_food} is not present")
new_food= str(input("Add new item :")).title()
prod.append(new_food)
print("Your product list now contains :", len(prod), "items", prod)
