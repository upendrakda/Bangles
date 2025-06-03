import random
import os
def get_num():
    digits = list("0123456789")
    random.shuffle(digits)
    num = ''.join(digits[:3])
    return num

def play():
    secret = get_num
    print("#New Game\nI have thought up a number. You have 10 guesses to get it.")
    i=0
    while i<10:
        print("Guess #",i+1)
        i+=1

def help():
    print("#Help\nHow to Play: Bagels")
    print("----------------------------------------------------------")
    print("Guess the secret 3-digit number (no repeated digits).\nClues after each guess:")
    print("Fermi - Right digit in right place \nPico - Right digit in wrong place \nBagels - No correct digits")
    print("Use logic to find the number. Good luck!")
    print("----------------------------------------------------------")

def home():
    os.system('cls')
    print("--Welcome to Bangles Game--")
    print("1. New Game \n2. Help \n3. Exit ")
    choice=int(input("Enter Your Choice:"))
    print("----------------------------------------------------------")
    match choice:
        case 1:
            play()
        case 2: 
            help()
        case 3:
            exit()
        case _:
            print("Enter a valid number!!")
    

print(get_num())
home()