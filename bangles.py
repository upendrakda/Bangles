import random
import os

def get_num():
    digits = list("0123456789")
    random.shuffle(digits)
    num = ''.join(digits[:3])
    return num

def get_clues(secret, guess):
    if guess == secret:
        return ["You got it!"]
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues.append("Fermi")
        elif guess[i] in secret:
            clues.append("Pico")

    if not clues:
        return ["Bagels"]
    
    clues.sort()
    return clues

def play():
    secret = get_num()
    print("\n# New Game\nI have thought up a number. You have 10 guesses to get it.\n")

    for i in range(1, 11):
        while True:
            guess = input(f"Guess #{i}: ")
            if len(guess) == 3 and guess.isdigit() and len(set(guess)) == 3:
                break
            else:
                print("Enter a 3-digit number with no repeating digits.")

        clues = get_clues(secret, guess)
        print(" ".join(clues))

        if guess == secret:
            break
    else:
        print(f"Out of guesses! The number was {secret}.")

    input("\nPress Enter to return to the main menu...")
    home()

def help():
    print("# Help\nHow to Play: Bagels")
    print("----------------------------------------------------------")
    print("Guess the secret 3-digit number (no repeated digits).")
    print("Clues after each guess:")
    print("- Fermi  : Right digit in the right place")
    print("- Pico   : Right digit in the wrong place")
    print("- Bagels : No correct digits")
    print("Use logic to figure out the number. You have 10 guesses.")
    print("----------------------------------------------------------")
    input("\nPress Enter to return to the main menu...")
    home()

def home():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-- Welcome to Bagels Game --")
    print("1. New Game \n2. Help \n3. Exit")
    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        choice = 0
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
            input("Press Enter to continue...")
            home()

home()