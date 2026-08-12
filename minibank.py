balance = 0


def check_balance():
    print(f"\nYour current balance is: ₹{balance}")


def deposit():
    global balance

    amount = float(input("\nEnter amount to deposit: ₹"))

    if amount <= 0:
        print("❌ Enter a valid amount.")
    else:
        balance += amount
        print(f" ₹{amount} deposited successfully!")


def withdraw():
    global balance

    amount = float(input("\nEnter amount to withdraw: ₹"))

    if amount <= 0:
        print("❌ Enter a valid amount.")
    elif amount > balance:
        print("❌ Insufficient balance.")
    else:
        balance -= amount
        print(f" ₹{amount} withdrawn successfully!")


def main():
    print("================================")
    print("        MINI BANKING SYSTEM")
    print("================================")

    while True:
        print("\n---------- MENU ----------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank you for using our banking system!")
            break

        else:
            print(" Invalid choice. Please try again.")


main()