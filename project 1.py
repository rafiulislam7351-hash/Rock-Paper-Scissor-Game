import random

computer = -random.choice([1, -1, 0])
player = input("Enter your choice(Rock,Paper,Scissors):").capitalize()

playerDict = {"Rock": 1, "Paper": -1, "Scissors": 0}
computerDict = {1: "Rock", -1: "Paper", 0: "Scissors"}

print("Computer's choice =", computerDict[computer])
player_number = playerDict[player]

if computer == -1 and player_number == 1:
    print("You Lose!")
elif computer == -1 and player_number == 0:
    print("You Win!")
elif computer == 1 and player_number == 0:
    print("You Lose!")
elif computer == 1 and player_number == -1:
    print("You Win!")
elif computer == 0 and player_number == 1:
    print("You Win!")
elif computer == 0 and player_number == -1:
    print("You Lose!")
elif computer == player_number:
    print("It's a Draw (>_<)!Keep Trying")
else:

    print("Better Luck Next Time!")
