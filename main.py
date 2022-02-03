import random 
print("Hint:The numbers are from 0 to 10 only")
user_choice = input("Enter your Guess \n")
user_choice = int(user_choice)
comp_choice = random.randrange(1,10)
if user_choice == comp_choice:
    print(f"You guessed it right, The number was {comp_choice}")
elif comp_choice == comp_choice:
    print(f"You Lost, The number was {comp_choice}")
else:
    print("Error*_*404/Draw of both user and computer")