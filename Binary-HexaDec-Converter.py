print("Welcome to Binary-HexaDecimal Converter App!")

max_val = int(input("\n Compute the Binary and Hexa-Decimal values upto the following decimal numbers: "))
decimal = list(range(1,max_val+1))
binary = []
hexaDec = []
for num in decimal:
    binary.append(bin(num))
    hexaDec.append(hex(num))

print("The portion of the list you would like to access?")
low_range = int(input("Starting value? "))
max_range = int(input("End value? "))
print("\nDecimal Values")
for num in decimal[low_range+1:max_range]:
    print(num)
print("\nBinary Values")
for num in binary[low_range+1:max_range]:
    print(num)
print("\nHexa-Decimal Values")
for num in hexaDec[low_range+1:max_range]:
    print(num)

input("\nPress Enter to print all the values from 1 to "+str(max_val)+".")

#print(f"{decimal} \t {binary} \t {hexaDec}")

for d,b,h in zip(decimal,binary,hexaDec):
    print("Decimal \t Binary \t HexaDecimal")
    print(d,"\t\t",b,"\t\t",h)

