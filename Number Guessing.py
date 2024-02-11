import random
# random number from range between 1-50
n = random.randrange(1,50)
print("NUMBER GUESSING GAME")
# user input to enter a number
guess = int(input("Guess a number : "))
while n != guess:
    if guess < n:
        print("Too low")
        guess = int(input("Guess Again : "))
    elif guess > n:
        print("Too High")
        guess = int(input("Guess Again : "))
    else:
        break
print(" *** You guessed it Right !! *** ")
