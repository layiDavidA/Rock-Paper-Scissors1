from enum import Enum
import random
import sys


class RPS(Enum):
    ROCK = 1
    SCISSORS = 2
    PAPER = 3


print(" ")
playerchoice = input(
    "Enter...\n 1 for rock\n 2 for scissors\n 3 for paper\n Enter:")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("Please enter a number 1 through 3.")

computerC = random.choice(" 123")
computer = int(computerC)

print(" ")
print("you chose " + str(RPS(player)).replace('RPS.', "") + ".")
print("I chose " + str(RPS(computer)).replace('RPS.', "") + ".")
print(" ")

if player == 1 and computer == 2:
    print("You Won!")
elif player == 2 and computer == 3:
    print("You Won!")
elif player == 3 and computer == 1:
    print("You Won!")
elif player == computer:
    print("Tie!")
else:
    print("You lost!")
