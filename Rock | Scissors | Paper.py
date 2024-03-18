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


import random

print("Welcome to the Rock, Paper, Scissors game! \n")
computer = random.randint(0, 2)

player = int(input("Type 0 for Rock | 1 for Paper | 2 for Scissors \n"))

# Draws
if (player == 0 and computer == 0):
    print(rock)
    print(f"computer choosed: {rock} \n It's a draw!")

if (player == 1 and computer == 1):
    print(paper)
    print(f"computer choosed: {paper} \n It's a draw!")

if (player == 2 and computer == 2):
    print(scissors)
    print(f"computer choosed: {scissors} \n It's a draw!")

# MY WINS
if player == 0 and computer == 2:
    print(rock)
    print(f"Computer choice: {scissors} \n You win!")
if player == 1 and computer == 0:
    print(paper)
    print(f"Computer choice: {rock} \n You win!")
if player == 2 and computer == 1:
    print(scissors)
    print(f"Computer choice: {paper} \n You win!")

# Computer WINS
if player == 2 and computer == 0:
    print(scissors)
    print(f"Computer choice: {rock} \n You loose!")
if player == 0 and computer == 1:
    print(rock)
    print(f"Computer choice: {paper} \n You loose!")
if player == 1 and computer == 2:
    print(paper)
    print(f"Computer choice: {scissors} \n You loose!")
