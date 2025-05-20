# This Python code is a password generator program. Here's a breakdown of what the code does:
import random

numbers_1=[1,2,3,4,5,6,7,8,9,0]
symbols_1=["!","@","#","$","%","&","*"]
letters_3=["z","x","c","v","b","n","m","a","s","d","f","g","h","j","k","l","q","w","e","r","t","y","u","i","o","p"]
letters_4=["Z","X","C","V","B","N","M","A","S","D","F","G","H","J","K","L","Q","W","E","R","T","Y","U","I","O","P"]

print("welcome to the pypassoworrd generator")

letters=int(input("How many small letters you would like in your passoword? : \n"))
symbols=int(input("how many symbols would you like in your passoword? :\n"))
numbers=int(input("How many numbers you would like in your passoword? :\n"))
letters_2=int(input("How many Captil letters you would like in your passoword? :\n"))

passoword=[]
for i in range(letters):
    letteers_5=random.choice(letters_3)
    passoword+=letteers_5
for i in range(letters_2):
    letteers_6=random.choice(letters_4)
    passoword+=letteers_6
for i in range(symbols):
    symbols_2=random.choice(symbols_1)
    passoword+=symbols_2
for i in range(numbers):
    numbers_2=random.choice(numbers_1)
    passoword+=str(numbers_2)


print(f"your passoword with shuffle in list = {passoword}")
random.shuffle(passoword)
print(f"your passoword with suffle in list = {passoword}")
joint_passoword="".join(passoword)
print(f"your passoword with shuffle is = {joint_passoword}")
