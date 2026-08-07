print("Welcome to the Rock, Paper, Scissors Game!")
print("Get ready to play!") 
choice = int(input("Do you want to play the game? (1 for Yes, 0 for No): "))
if choice == 0:
    print("Exiting the game. Goodbye!") 
if choice == 1: 
    import random
    options = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    else:
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")   
        else:
            print("Computer wins!") 
