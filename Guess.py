import random

highest = 1000
ans = random.randint(1, highest)

guess = 0

while guess != ans:
    guess = int(input("guess: "))

    if guess == 0:
        print("game over".swapcase())
        break
    if guess == ans:
        print("Good job")
        break
    elif guess < ans:
        print("Your guess is lower than the answer")
    else:
        print("Your guess is higher than the answer")
        