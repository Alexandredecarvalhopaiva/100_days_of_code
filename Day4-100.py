import random

# Welcome message
print(" Welcome to the Rock, Paper, Scissors Game! \n")
print("Game Rules:")
print("* You choose between Rock, Paper or Scissors.")
print("* The computer will also make a random choice.")
print("* The outcome will be decided as follows:")
print("   - Rock crushes Scissors ")
print("   - Scissors cuts Paper ")
print("   - Paper wraps Rock")
print("\nLet's play! Choose wisely...\n")

# ASCII Art
rock = '''\
    _______
---'   ____)
      (_____ )
      (_____ )
      (____)
---.__(___)
'''
paper = '''\
     _______
---'   ____)____
          ______)
         _______)
         _______)
---.__________)
'''
scissors = '''\
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_art = {
    "Rock": rock,
    "Paper": paper,
    "Scissors": scissors
}

options = ["Rock", "Paper", "Scissors"]

# Player input
player_choice = input("Choose one of the options: \n 1 - Rock \n 2 - Paper \n 3 - Scissors\n")

if player_choice not in ["1", "2", "3"]:
    print("Invalid choice. Please choose 1, 2, or 3.")

player_choice = int(player_choice)
player_move = options[player_choice - 1]
computer_move = random.choice(options)

# Show choices with ASCII art
print(f"\nYou chose: {player_move}")
print(ascii_art[player_move])
print(f"The computer chose: {computer_move}")
print(ascii_art[computer_move])

# Game logic
if player_move == computer_move:
    print("\nIt's a tie!")
elif (player_move == "Rock" and computer_move == "Scissors") or \
     (player_move == "Paper" and computer_move == "Rock") or \
     (player_move == "Scissors" and computer_move == "Paper"):
    print("\nCongratulations, you won!! 🎉")
else:
    print("\nYou lost badly... 😞")
