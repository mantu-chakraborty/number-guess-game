
import random
number=random.randint(1,10)
guess=None
tries=0

print("guess the number between 1 and 10!")
while guess!= number:
    guess= int(input("your guess:"))
    tries+=1

    if guess<number:
        print("TOO LOW!")
    elif guess>number:
        print("TOO HIGH!")
    else:
        print("CONGRATULATIONS! YOU GUESSED IT IN{tries}tries.")