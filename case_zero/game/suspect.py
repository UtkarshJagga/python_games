class Suspect:

    def __init__(
        self,
        name,
        role,
        description,
        statement,
        motive,
        suspicious=False
    ):
        self.name = name
        self.role = role
        self.description = description
        self.statement = statement
        self.motive = motive
        self.suspicious = suspicious

        self.interrogated = False
        self.clues_found = []

    def interrogate(self):

        self.interrogated = True

        print("\n" + "=" * 50)
        print(f"INTERROGATING {self.name.upper()}")
        print("=" * 50)

        print(f"\nRole: {self.role}")

        print(f'\n{self.name}:')
        print(f'"{self.statement}"')

        if self.suspicious:
            print("\n⚠ You notice inconsistencies in their story.")
        else:
            print("\nTheir behavior appears calm.")

    def show_information(self):

        print(f"\nName: {self.name}")
        print(f"Role: {self.role}")
        print(f"Description: {self.description}")
        print(f"Motive: {self.motive}")