import random
import sys

Pscore = 0
Cscore = 0

def count(winner):
    global Pscore, Cscore

    if winner == "player":
        Pscore += 1

    elif winner == "computer":
        Cscore += 1

    print (" Score:\n",Pscore, "-", Cscore, "\n")
    player_pick()

def compare(Pfighter, Cfighter):
    print("\nYou picked:", Pfighter)
    print("Computer picked:", Cfighter, "\nComparing...\n")

    if Pfighter == Cfighter:
        print("It's a tie, restarting\n")
        count("tie")

    elif Pfighter == "Rock":
        if Cfighter == "Paper":
            print("Computer wins, restarting")
            count("computer")

        elif Cfighter == "Scissors":
            print("You win, restarting")
            count("player")

    elif Pfighter == "Paper":
        if Cfighter == "Rock":
            print("You win, restarting")
            count("player")

        elif Cfighter == "Scissors":
            print("Computer wins, restarting")
            count("computer")

    elif Pfighter == "Scissors":
        if Cfighter == "Rock":
            print("Computer wins, restarting")
            count("computer")

        elif Cfighter == "Paper":
            print("You win, restarting")
            count("player")

def computer_pick(Pfighter):
    options = ["Rock", "Paper", "Scissors"]
    Cfighter = random.choice(options)

    compare(Pfighter, Cfighter)

def player_pick():
    print("Rock, Paper, Scissors")
    pick = input("Choose Your Fighter:\n")

    if pick in ["Rock", "rock", "R", "r"]:
        computer_pick("Rock")

    elif pick in ["Paper", "paper", "P", "p"]:
        computer_pick("Paper")

    elif pick in ["Scissors", "scissors", "S", "s"]:
        computer_pick("Scissors")

    elif pick in ["Quit", "quit", "Close", "close", "Exit", "exit", "Q", "q", "C", "c", "E", "e"]:
        print("\nExiting program...\n")
        sys.exit()

    else:
        print("Error, please try again. Write your choice's name or first letter. Case insensitive \n\n")
        player_pick()

player_pick()
