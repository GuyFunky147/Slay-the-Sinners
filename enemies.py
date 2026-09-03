from main import Enemy

ENEMIES = {

    "Lesser Sinner": {
        "hp": 20,
        "atk": 5,
        "def": 1,
        "sin": 10,
        "saint": 0,
        "drops": [],
        "speak": {
            "Why do you fight?": "Because I refuse to bow.",
            "Repent.": "Never."
        }
    },

    "Saint Guard": {
        "hp": 25,
        "atk": 4,
        "def": 3,
        "sin": 0,
        "saint": 10,
        "drops": ["Saint Mail"],
        "speak": {
            "Why do you fight?": "Because duty demands it."
        }
    },

    "First Sinner": {
        "hp": 100,
        "atk": 15,
        "def": 5,
        "sin": 30,
        "saint": 0,
        "drops": ["First Relic"],
        "speak": {
            "Why won't you bow?": "Because I know what waits above.",
            "What waits above?": ".........\nEnvy refuses to answer."
        }
    },

    "Second Sinner": {
        "hp": 125,
        "atk": 18,
        "def": 6,
        "sin": 40,
        "saint": 0,
        "drops": ["Second Relic"]
    },

    "Third Sinner": {
        "hp": 150,
        "atk": 22,
        "def": 8,
        "sin": 50,
        "saint": 0,
        "drops": ["Third Relic"]
    },

    "Elpis": {
        "hp": 500,
        "atk": 40,
        "def": 10,
        "sin": 0,
        "saint": 100,
        "drops": ["Elpis Essence"],
        "speak": {
            "Who are you?": "Hope incarnate."
        }
    },

    "Cognifis": {
        "hp": 500,
        "atk": 45,
        "def": 12,
        "sin": 0,
        "saint": 100,
        "drops": ["Cognifis Essence"],
        "speak": {
            "Who are you?": "The one who decides Right and Wrong."
        }
    },

    "Holis": {
        "hp": 500,
        "atk": 35,
        "def": 15,
        "sin": 0,
        "saint": 100,
        "drops": ["Holis Essence"],
        "speak": {
            "Who are you?": "I am he who separateth sinner from saint."
        }
    },

    "Descended One": {
        "hp": 1200,
        "atk": 70,
        "def": 25,
        "sin": 120,
        "saint": 120,
        "drops": ["Crown of the Descended"],
        "speak": {
            "Who are you?": ".........\nThe Descended one chooses not to answer, for he is afraid.",
            "Why did you attempt to start the cycle early?": "You do not get to know of such matters."
        }
    },

    "Sinslayer": {
        "hp": 1,
        "atk": 1,
        "def": 1,
        "sin": 999,
        "saint": 999,
        "drops": [
            "Scroll: Blindness of Hell",
            "Scroll: Resistance of Saints",
            "Scroll: Vengeance of Sinners"
        ]
    }
}