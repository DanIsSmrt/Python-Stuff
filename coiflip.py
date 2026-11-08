import random

def coinflip():
    ht = random.randint(1,2)

    if ht == 1:
        print("heads")
    elif ht== 2:
        print("tails")
    else:
        print("fuck")
coinflip()

