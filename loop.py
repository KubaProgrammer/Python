import random

def printNumbers(n):
    print(f"Numbers form 1 to {n} are: ", end="")
    for i in range(n):
        print(i+1, end=" ")
    print("")

def sumSeries(n):
    x = 0
    for i in range(n):
        x += i+1
    print(f"The sum of the series from 1 to {n} is {x}.")

def guessTheNumber():
    number = random.randint(1, 5)
    print("Gueass the number from 1 to 5.")
    guess = int(input("Your guess: "))
    if guess == number:
        print(f"You guessed it right! The number was {guess}!!!")
    else:
        while guess != number:
            if guess < 1 or guess > 5:
                guess = int(input("The range of possible numbers is 1 - 5. Try again.\n"))
            else:
                guess = int(input("Wrong guess, try again.\n"))
        print(f"You guessed it right! The number was {guess}!!!")
    

printNumbers(10)
sumSeries(int(input("Give me the highest number of the series you want to get the sum of: ")))
guessTheNumber()