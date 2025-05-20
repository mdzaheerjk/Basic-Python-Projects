# This Python code is a Number Guessing Game where the computer randomly selects a number between 1
# and 100, and the player needs to guess that number within a certain number of attempts based on the
# chosen difficulty level (Easy or Hard).

import random
print("""
      
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
""")


print("Welcome To the Number Guessing Game !")
print("computer : I am guessing a number between 1 to 100")
computer_guess=random.randint(0,101)
dificulty=str(input("choose the dificulty level 'Easy' or 'Hard' :\n")).lower()


if dificulty=="easy":
    attempt=10
    game_over=True
    while game_over:
        print(f"you have {attempt} attempt left")
        user_guess=int(input("guess the number between 1 to 100: ? "))
        if user_guess==computer_guess:
            print("you won !")
            game_over=False
        elif user_guess<computer_guess:
            attempt-=1
            print(f"think again the number higher than:{user_guess}")
            if attempt==0:
                print("you lose !")
                game_over=False
        elif user_guess>computer_guess:
            attempt-=1
            print(f"think again the number lower than:{user_guess}")
            if attempt==0:
                print("you lose !")
                game_over=False
            


elif dificulty=="hard":
    attempt=5
    game_over=True
    while game_over:
        print(f"you have {attempt} attempt left")
        user_guess=int(input("guess the number between 1 to 100: ? "))
        if user_guess==computer_guess:
            print("you won !")
            game_over=False
        elif user_guess<computer_guess:
            attempt-=1
            print(f"think again the number higher than:{user_guess}")
            if attempt==0:
                print("you lose !")
                game_over=False
        elif user_guess>computer_guess:
            attempt-=1
            print(f"think again the number lower than:{user_guess}")
            if attempt==0:
                print("you lose !")
                game_over=False
            
        
        
