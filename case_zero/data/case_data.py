from game.suspect import Suspect
from game.evidence import Evidence

suspects = [

    Suspect(
        name="James",
        role="Business Partner",
        description=(
            "A wealthy businessman and Edward's "
            "business partner."
        ),
        statement=(
            "I was in the dining room during "
            "the entire evening."
        ),
        motive=(
            "Edward was planning to remove James "
            "from the company."
        ),
        suspicious=True
    ),

    Suspect(
        name="Sarah",
        role="Sister",
        description=(
            "Edward's younger sister. "
            "She appears extremely nervous."
        ),
        statement=(
            "I was upstairs in my room "
            "the entire night."
        ),
        motive=(
            "Sarah recently argued with Edward "
            "over the family inheritance."
        ),
        suspicious=True
    ),

    Suspect(
        name="Michael",
        role="Butler",
        description=(
            "The Blackwood family's butler "
            "for more than fifteen years."
        ),
        statement=(
            "I was preparing dinner in the kitchen."
        ),
        motive=(
            "Michael had no known financial "
            "connection to Edward."
        ),
        suspicious=False
    ),

    Suspect(
        name="Emma",
        role="Journalist",
        description=(
            "A journalist who was interviewing "
            "Edward about his company."
        ),
        statement=(
            "I left the mansion before the murder."
        ),
        motive=(
            "Emma was investigating corruption "
            "inside Edward's company."
        ),
        suspicious=False
    ),

    Suspect(
        name="Daniel",
        role="Neighbor",
        description=(
            "Edward's neighbor who claims "
            "he heard nothing unusual."
        ),
        statement=(
            "I stayed at home all evening."
        ),
        motive=(
            "Daniel had no obvious motive."
        ),
        suspicious=False
    )
]

evidence = [

    Evidence(
        name="Broken Luxury Watch",
        description=(
            "A broken luxury watch was found "
            "beside the victim's chair."
        ),
        location="Study",
        related_suspect="James"
    ),

    Evidence(
        name="Blood-Stained Handkerchief",
        description=(
            "A handkerchief containing traces "
            "of blood was found underneath the desk."
        ),
        location="Study",
        related_suspect="James"
    ),

    Evidence(
        name="Missing Kitchen Knife",
        description=(
            "One of the mansion's kitchen knives "
            "is missing."
        ),
        location="Kitchen",
        related_suspect="Michael"
    ),

    Evidence(
        name="Fresh Footprints",
        description=(
            "Fresh footprints were found near "
            "the back door."
        ),
        location="Kitchen"
    ),

    Evidence(
        name="Black Fabric",
        description=(
            "A torn piece of black fabric was "
            "found on a garden bush."
        ),
        location="Garden",
        related_suspect="James"
    ),

    Evidence(
        name="Garden Footprints",
        description=(
            "Footprints lead from the garden "
            "toward the kitchen."
        ),
        location="Garden"
    ),

    Evidence(
        name="Family Photograph",
        description=(
            "A family photograph was knocked "
            "off the bedroom table."
        ),
        location="Bedroom",
        related_suspect="Sarah"
    ),

    Evidence(
        name="Small Key",
        description=(
            "A small brass key was found "
            "underneath the bed."
        ),
        location="Bedroom"
    ),

    Evidence(
        name="Open Book",
        description=(
            "A book about financial fraud "
            "was found open on the library floor."
        ),
        location="Library",
        related_suspect="Emma"
    )
]