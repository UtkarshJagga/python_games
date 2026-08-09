class Evidence:

    def __init__(
        self,
        name,
        description,
        location,
        related_suspect=None
    ):
        self.name = name
        self.description = description
        self.location = location
        self.related_suspect = related_suspect

    def display(self):

        print("\n" + "-" * 50)

        print(f"🔎 {self.name}")

        print("\nDescription:")
        print(self.description)

        print(f"\nFound at: {self.location}")

        if self.related_suspect:
            print(
                f"Possible connection: "
                f"{self.related_suspect}"
            )

        print("-" * 50)