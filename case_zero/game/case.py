class Case:

    def __init__(self, suspects, evidence):

        self.suspects = suspects
        self.evidence = evidence

        self.collected_evidence = []
        self.investigation_points = 12

        self.murderer = "James"
    def show_suspects(self):

        print("\n" + "=" * 60)
        print("                    SUSPECTS")
        print("=" * 60)

        for number, suspect in enumerate(self.suspects, start=1):

            print(f"\n{number}. {suspect.name}")
            print(f"   Role: {suspect.role}")
            print(f"   {suspect.description}")
    def investigate(self):

        if self.investigation_points <= 0:

            print("\n❌ You have no investigation points left.")

            return

        print("\n" + "=" * 60)
        print("                 LOCATIONS")
        print("=" * 60)

        locations = list(
            set(e.location for e in self.evidence)
        )

        for number, location in enumerate(locations, start=1):

            print(f"{number}. {location}")

        choice = input("\nChoose location: ")

        if not choice.isdigit():

            print("Please enter a number.")

            return

        choice = int(choice)

        if choice < 1 or choice > len(locations):

            print("Invalid location.")

            return

        selected_location = locations[choice - 1]

        self.investigation_points -= 1

        print(f"\nYou investigate the {selected_location}...")

        found = False

        for evidence in self.evidence:

            if (
                evidence.location == selected_location
                and evidence not in self.collected_evidence
            ):

                evidence.display()

                self.collected_evidence.append(evidence)

                found = True

                break

        if not found:

            print("\nNothing new was found here.")

        print(
            f"\nInvestigation points remaining: "
            f"{self.investigation_points}"
        )
    def interrogate(self):

        if self.investigation_points <= 0:

            print("\n❌ No investigation points remaining.")

            return

        self.show_suspects()

        choice = input("\nChoose suspect: ")

        if not choice.isdigit():

            print("Please enter a number.")

            return

        choice = int(choice)

        if choice < 1 or choice > len(self.suspects):

            print("Invalid suspect.")

            return

        suspect = self.suspects[choice - 1]

        self.investigation_points -= 1

        suspect.interrogate()

        print(
            f"\nInvestigation points remaining: "
            f"{self.investigation_points}"
        )

    def notebook(self):

        print("\n" + "=" * 60)
        print("                 DETECTIVE NOTEBOOK")
        print("=" * 60)

        print(
            f"\nEvidence collected: "
            f"{len(self.collected_evidence)}"
        )

        if not self.collected_evidence:

            print("\nNo evidence collected.")

        else:

            for number, evidence in enumerate(
                self.collected_evidence,
                start=1
            ):

                print(
                    f"\n{number}. "
                    f"{evidence.name}"
                )

                print(
                    f"   {evidence.description}"
                )

                print(
                    f"   Location: "
                    f"{evidence.location}"
                )

    def deduction_report(self):

        print("\n" + "=" * 60)
        print("                 DEDUCTION REPORT")
        print("=" * 60)

        scores = {}

        for suspect in self.suspects:

            scores[suspect.name] = 0

        for evidence in self.collected_evidence:

            if evidence.related_suspect:

                suspect_name = evidence.related_suspect

                if suspect_name in scores:

                    scores[suspect_name] += 1

        for suspect in self.suspects:

            if suspect.interrogated:

                if suspect.suspicious:

                    scores[suspect.name] += 1

        sorted_scores = sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\nCurrent suspicion levels:\n")

        for name, score in sorted_scores:

            print(
                f"{name}: "
                f"{'█' * score} "
                f"({score})"
            )

    def accusation(self):

        print("\n" + "=" * 60)
        print("                 FINAL ACCUSATION")
        print("=" * 60)

        self.deduction_report()

        print("\nWho is the murderer?")

        for number, suspect in enumerate(
            self.suspects,
            start=1
        ):

            print(f"{number}. {suspect.name}")

        choice = input("\nYour accusation: ")

        if not choice.isdigit():

            print("Invalid choice.")

            return False

        choice = int(choice)

        if choice < 1 or choice > len(self.suspects):

            print("Invalid suspect.")

            return False

        accused = self.suspects[choice - 1].name

        print("\nAnalyzing evidence...")

        if accused == self.murderer:

            print("\n" + "=" * 60)
            print("                  CASE SOLVED")
            print("=" * 60)

            print(f"""
You accused {accused}.

Your deduction was correct.

James was responsible for the murder.

The evidence, timeline and contradictions
all pointed toward him.

Congratulations, Detective.
""")

            return True

        else:

            print("\n" + "=" * 60)
            print("                 CASE FAILED")
            print("=" * 60)

            print(f"""
You accused {accused}.

That accusation was incorrect.

The real murderer was {self.murderer}.

The case remains unsolved.
""")

            return False