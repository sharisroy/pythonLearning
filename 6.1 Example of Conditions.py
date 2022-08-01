# Guessing Game

from random import randint
guessNumber = int(input("Enter a number between 1 to 5: "))
randomNumber = randint(1, 5)
if guessNumber == randomNumber:
    print("Your guess is correct")
elif guessNumber <= 5:
    print("Your guess is not correct")
    print("Random number was : ", randomNumber)
else:
    print("You entered wrong number which is out of 5")
    print("your number is : ", guessNumber)