import random
def com_guess():
    y = random.randint(1,100)
    return y
x = com_guess()
guess = 0
while x!=guess:
    guess = int(input("Enter your guess:"))
    if x>guess:
        print("guess higher")
    elif x<guess:
        print("guess lower")
    else:
        print("you have guessed the number ",x)