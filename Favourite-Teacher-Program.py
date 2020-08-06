print("Welcome")
rank = []
rank.append(input("Enter the list of Teachers\n"))
rank.append(input("Enter the list of Teachers\n"))
rank.append(input("Enter the list of Teachers\n"))
rank.append(input("Enter the list of Teachers\n"))
rank.append(input("Enter the list of Teachers\n"))

print("This is your present rank of teachers:\n", rank)
print("This is your sorted list of teachers: \n", sorted(rank))
print("Your first two fav teachers: ", rank[:2])
print("Your first next two fav teachers: ", rank[2:4])
print("Your last fav teachers: ", rank[-1])

rank.insert(0,input("\nOpps"+rank[0]+"is no longer you fav teacher, Who is your fav teacher??"))
print(rank)
