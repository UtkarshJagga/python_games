from game.case import Case
from data.case_data import suspects, evidence


def show_intro():

    print("=" * 60)
    print("                    CASE ZERO")
    print("=" * 60)

    print("""
A murder has occurred at Blackwood Mansion.

Edward Blackwood has been found dead
inside his private study.

Five people were connected to the victim.

Someone is lying.

Your job is to discover who.
""")

    input("Press ENTER to begin...")


def main():

    show_intro()

    case = Case(
        suspects=suspects,
        evidence=evidence
    )

    while True:

        print("\n" + "=" * 60)
        print("                    CASE ZERO")
        print("=" * 60)

        print(
            f"\nInvestigation Points: "
            f"{case.investigation_points}"
        )

        print("\n1. View Suspects")
        print("2. Investigate Location")
        print("3. Interrogate Suspect")
        print("4. Open Notebook")
        print("5. Deduction Report")
        print("6. Make Final Accusation")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":

            case.show_suspects()

        elif choice == "2":

            case.investigate()

        elif choice == "3":

            case.interrogate()

        elif choice == "4":

            case.notebook()

        elif choice == "5":

            case.deduction_report()

        elif choice == "6":

            solved = case.accusation()

            if solved:
                break

        elif choice == "7":

            print("\nInvestigation terminated.")

            break

        else:

            print("\nInvalid option.")


if __name__ == "__main__":
    main()