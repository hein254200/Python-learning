import random
secret_number=random.randint(1,10)
guess_number = None
attempt=0
while secret_number!=guess_number:
    attempt+=1

    guess_number = int(input("Enter your guess number:"))
    if secret_number!= guess_number:
        print("You lose.Please try again!")
    else:
        print(f"your number is {guess_number}.screct number is {secret_number}. You win!")

print(f"You win the game with {attempt} attempt.")
    
