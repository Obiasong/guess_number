import random
import checkguess
name =  input("Enter your name and press enter to start the game: ")

number  =  random.randint(1, 10)

attempts_limit = 3
attempts = 0

# Exit the loop if user gets the correct guess, else stop game after 3 (attempts_limit) attempts
while attempts < attempts_limit:
    try:
        guess = int(input("Enter a number between 1 and 10 (including the endpoints): "))
        
        # Invoke a value error is number is not in the required range
        if guess < 1 or guess > 10:
            raise ValueError("Please enter a number between 1 and 10 from inside")
        if checkguess.compareGuess(number, guess):
            print(f"Great Job {name}!! You guessed correctly the number is {number}")
            break
        else :
            if attempts == attempts_limit-1:
                print(f"The number is {number}")
                pass
            else :
                print(f"You almost got it {name}, Try again!")
                pass
    except ValueError:
        print("Please enter a valid number between 1 and 10") 
    attempts += 1    
else :
    print(f"Sorry {name}! You have not been able to guess the number after {attempts_limit} attempts.")
    exit(0)