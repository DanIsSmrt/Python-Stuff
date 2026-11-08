import random

def game10(tenrange):
    guess = int(input("guess a number, 1 - 10\n:"))

    if guess == tenrange:
        print("correct!\n\n")
        gameselect()
        
    elif guess > tenrange:
        print("\ntoo high!")
        game10(tenrange)

    elif guess < tenrange:
        print("\ntoo low!")
        game10(tenrange)

    else:
        print("\nerr")
        game10(tenrange)

def game100(hunrange):
    guess = int(input("guess a number, 1 - 100\n"))

    if guess == hunrange:
        print("correct!\n\n")
        gameselect()

    elif guess > hunrange:
        print("\ntoo high")
        game100(hunrange)

    elif guess < hunrange:
        print("\ntoo low")
        game100(hunrange)

    else:
        print("\nerr")
        game100(hunrange)

def game1000(thourange):
    guess = int(input("guess a number, 1 - 1000:\n"))

    if guess == thourange:
        print("correct!\n\n")
        gameselect()

    elif guess > thourange:
        print("\ntoo high!")
        game1000(thourange)

    elif guess < thourange:
        print("\ntoo low!")
        game1000(thourange)

    else:
        print("\nerr")
        game1000(thourange)

def gameselect():
    gamemode = int(input("\ngamemode: 10, 100, 1000\n:"))

    if gamemode == 10:
        print("game selected: 10\n")
        
        tenrange = random.randint(1,10)
        game10(tenrange)
        
    elif gamemode == 100:
        print("game selected: 100\n")

        hunrange = random.randint(1,100)
        game100(hunrange)
        
    elif gamemode == 1000: 
        print("game selected: 100\n")

        thourange = random.randint(1,1000)
        game1000(thourange)
        
    else:
        print("do better buddy,", gamemode, "is not an answer")
        gameselect()

gameselect()
