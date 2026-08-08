import random

choice = int(input("Do you want to roll the dice? (1 for Yes, 0 for No): "))


if choice == 0:
    print("Exiting the game. Goodbye!")
elif choice == 1:
    time = int(input("How many times do you want to roll the dice? "))
    for _ in range(time):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(dice1, dice2)

else:
    print("Invalid input. Please enter 1 to roll the dice or 0 to exit.")