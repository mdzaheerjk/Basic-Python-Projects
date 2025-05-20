    # The line `print("you choose scissor and computer choose scissor  'you won'!")` is displaying a
    # message indicating that the user chose "scissor" and the computer also chose "scissor",
    # resulting in a win for the user. However, there seems to be a mistake in the message because it
    # should actually be a draw when both the user and the computer choose the same option.
import random
rock="""   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""  
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissor="""     
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_input=input("what do you choose rock paper or scissor!\n")
if user_input=="rock":
    print(f"you choose rock :\n{rock}")
elif user_input=="paper":
    print(f"you choose paper :\n{paper}")
elif user_input=="scissor":
    print(f"you choose scissor :\n{scissor}")
else:
    print("enter the correct input")

computer_guess=random.randint(1,3)
if computer_guess==1:
    print(f"computer choose rock: \n{rock}")
elif computer_guess==2:
    print(f"computer choose paper: \n{paper}")
elif computer_guess==3:
    print(f"computer choose scsissor: \n{scissor}")

if user_input=="rock" and computer_guess==1:
    print("you choose rock and computer choose rock match 'draw' !")
elif user_input=="paper" and computer_guess==2:
    print("you choose paper and computer choose paper match 'draw' !")
elif user_input=="scissor" and computer_guess==3:
    print("you choose scissor and computer choose scissor match 'draw' !")
elif user_input=="rock" and computer_guess==2:
    print("you choose rock and computer choose paper 'you lose' !")
elif user_input=="rock" and computer_guess==3:
    print("you choose rock and computer choose scissor 'you won' !")
elif user_input=="paper" and computer_guess==1:
    print("you choose paper and computer choose rock 'you won' !")
elif user_input=="paper" and computer_guess==3:
    print("you choose paper and computer choose scissor 'you lose' !")
elif user_input=="scissor" and computer_guess==1:
    print("you choose scissor and computer choose scissor 'you lose' !")
elif user_input=="scissor" and computer_guess==2:
    print("you choose scissor and computer choose scissor  'you won'!")