#This program counts no of letter present in the message
print(" Welcome!")
name = input("What is your name:").title().strip()
print("Hello",name,"!")
print("Will count the no.of letters present in your message.")
print()
message=input("Please enter a message:")
let=input("which letter do you wanna count?:").lower()
message=message.lower()
res=message.count(let)
print(res) 
#Done