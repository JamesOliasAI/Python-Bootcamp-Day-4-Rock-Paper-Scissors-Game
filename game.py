import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

symbols = [rock, paper, scissors]

user_choice = input("select 1 for rock, 2 for paper or 3 for scissors")
convert_choice = int(user_choice) - 1

comp_choice = random.randint(0,2)

print(f"You chose...\n{symbols[convert_choice]}")
print(f"Computer chose...\n{symbols[comp_choice]}")
if convert_choice == comp_choice:
    print("It's a draw")
elif convert_choice == 0 and comp_choice == 2:
    print("You Win!")
elif convert_choice == 1 and comp_choice == 0:
    print("You Win!")
elif convert_choice == 2 and comp_choice == 1:
    print("You Win!")
else:
    print("You lose")
