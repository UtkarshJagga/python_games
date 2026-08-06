import random;

number = int (random.randint(1, 100));

print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 1 and 100. Try to guess it!")

choice = int(input("Do you want to play the game? (1 for Yes, 0 for No): "))

if choice == 0:
        print("Exiting the game. Goodbye, Sweet Dreams!")
elif choice == 1:
        attempts = 0
        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")    
            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                break
            if attempts >= 5:
                print(f"Sorry, you've reached the maximum number of attempts. The number was {number}.")
                break   
else:
        print("Invalid input. Please enter 1 to play or 0 to exit.")