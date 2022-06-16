import random
def gameFunction():
    while True:
        rightAns = random.randrange(1,10)

        userGuess = int(input('Enter your guess \n'))

        if userGuess == rightAns:
            print(f'You Won The number was {rightAns} which matched with yours number {userGuess}.')
            False
            quit()
            
        else:
            True

try:
    gameFunction()

except ValueError as error:
    print(error)
    print("Now, Onwards please try to enter in integer only not in string or floats values.")

finally:
    gameFunction()