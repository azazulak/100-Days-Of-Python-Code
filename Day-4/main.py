import random

options = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

options_name = ["Rock", "Paper", "Scissors"]

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

enemy_choice = random.randint(0, 2)

print(f'''
You:
{options[choice]}

Computer:
{options[enemy_choice]}
''')

if choice - enemy_choice in [-2, 1]:
  print("You win!")
elif choice - enemy_choice == 0:
  print("Draw.")
else:
  print("You lose.")