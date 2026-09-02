import json
import os
import time

seed = 0

ceremonial_knife = False
sacrificial_garb = False
altar2go = False
black_flame = False

elpis = False
holis = False
cognifis = False

def typewriter(text, speed=0.05):
    
    for character in text:
        
        print(character, end="", flush=True)
        
        time.sleep(speed)

    print()

def say(speaker, text):
    typewriter(f"\n{speaker}:")
    typewriter(text)


def choice(speaker, text, *options):
    typewriter(f"\n{speaker}:")
    typewriter(text)

    for i, option in enumerate(options, 1):
        typewriter(f"({i}) {option}")
    while True:
        answer = input("> ")

        if answer.isdigit():
            index = int(answer)

            if 1 <= index <= len(options):
                return options[index - 1]

class Player:
    def __init__(self):
        self.hp = 50
        self.max_hp = 50

        self.atk = 10
        self.defense = 5

        self.sin = 0
        self.saint = 0

        self.weapon = None
        self.armor = None

        self.spells = []

        self.inventory = ["Health Potion"]


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


WEAPONS = {
    "Rusty Dagger": {
        "damage": 3
    },

    "Saintblade": {
        "damage": 15
    },

    "Sinner's Fang": {
        "damage": 18
    },

    "Ceremonial Knife": {
        "damage": 1,
        "fades": True,
        "awakened_damage": 999999
    }
}


ARMOR = {
    "Tattered Robes": {
        "defense": 1
    },

    "Saint Mail": {
        "defense": 5
    },

    "Sinwoven Cloak": {
        "defense": 8
    },

    "Sacrificial Garb": {
        "defense": 1,
        "fades": True,
        "awakened_effect": "immortality"
    }
}


SPELLS = {
    "Heal": {
        "cost": 5,
        "heal": 20
    },

    "Holy Burst": {
        "cost": 10,
        "damage": 30
    },

    "Black Flame": {
        "cost": 1,
        "damage": 1,
        "spread": True,
        "awakened_damage": 999999
    }
}

def save_game(player):
    
    filename = input("Which of the three save slots would you like to save to?")
    if filename == "1":
        filename = "slot1.json"
    if filename == "2":
        filename = "slot2.json"
    if filename == "3":
        filename = "slot3.json"

    data = {
        "hp": player.hp,
        "max_hp": player.max_hp,
        "atk": player.atk,
        "defense": player.defense,

        "sin": player.sin,
        "saint": player.saint,

        "weapon": player.weapon,
        "armor": player.armor,

        "spells": player.spells,
        "inventory": player.inventory,

        "ceremonial_knife": ceremonial_knife,
        "sacrificial_garb": sacrificial_garb,
        "altar2go": altar2go,
        "black_flame": black_flame,

        "elpis": elpis,
        "holis": holis,
        "cognifis": cognifis,

        "seed": seed
    }

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    say("Narrator",
"You kneel before the altar.\n"
"A sinner's soul is offered.\n"
"The cycle remembers.")
    typewriter("Game Saved.")

def load_game():

    filename = input("Which of the three save slots would you like to load?")
    if filename == "1":
        filename = "slot1.json"
    if filename == "2":
        filename = "slot2.json"
    if filename == "3":
        filename = "slot3.json"

    global ceremonial_knife
    global sacrificial_garb
    global altar2go
    global black_flame

    global elpis
    global holis
    global cognifis

    global seed

    if not os.path.exists(filename):

        typewriter(f"No save file found at location {filename}")

        return Player()

    with open(filename, "r") as file:
        data = json.load(file)

    player = Player()

    player.hp = data["hp"]
    player.max_hp = data["max_hp"]

    player.atk = data["atk"]
    player.defense = data["defense"]

    player.sin = data["sin"]
    player.saint = data["saint"]

    player.weapon = data["weapon"]
    player.armor = data["armor"]

    player.spells = data["spells"]
    player.inventory = data["inventory"]

    ceremonial_knife = data["ceremonial_knife"]
    sacrificial_garb = data["sacrificial_garb"]
    altar2go = data["altar2go"]
    black_flame = data["black_flame"]

    elpis = data["elpis"]
    holis = data["holis"]
    cognifis = data["cognifis"]

    seed = data["seed"]

    typewriter("Game Loaded.")

    return player

class Enemy:
    def __init__(self, enemy_name):
        enemy = ENEMIES[enemy_name]

        self.name = enemy_name
        self.hp = enemy["hp"]
        self.atk = enemy["atk"]
        self.defense = enemy["def"]


def attack(attacker, defender):

    damage = max(
        1,
        attacker.atk - defender.defense
    )

    defender.hp -= damage

    typewriter(f"{attacker.name} dealt {damage} damage.")


def attack_with_weapon(player, enemy):

    weapon_damage = 0

    if player.weapon:
        weapon_damage = WEAPONS[player.weapon]["damage"]

    damage = max(
        1,
        player.atk + weapon_damage - enemy.defense
    )

    enemy.hp -= damage

    typewriter(f"You dealt {damage} damage.")

def get_player_defense(player):

    defense = player.defense

    if player.armor:
        defense += ARMOR[player.armor]["defense"]

    return defense

def inventory_menu(player):

    if len(player.inventory) == 0:
        typewriter("Your inventory is empty.")
        return

    typewriter("\nInventory")

    for i, item in enumerate(player.inventory, 1):
        typewriter(f"{i}. {item}")

    choice = input("> ")

    if not choice.isdigit():
        return

    index = int(choice) - 1

    if index < 0 or index >= len(player.inventory):
        return

    item = player.inventory[index]

    if item == "Health Potion":

        player.hp = min(
            player.max_hp,
            player.hp + 25
        )

        player.inventory.remove(item)

        typewriter("Recovered 25 HP.")


def cast_spell(player, enemy):

    if len(player.spells) == 0:
        print("You know no spells.")
        return

    typewriter("\nSpells")

    for i, spell in enumerate(player.spells, 1):
        typewriter(f"{i}. {spell}")

    choice = input("> ")

    if not choice.isdigit():
        return

    index = int(choice) - 1

    if index < 0 or index >= len(player.spells):
        return

    spell = player.spells[index]

    if spell == "Heal":

        player.hp = min(
            player.max_hp,
            player.hp + 20
        )

        typewriter("Recovered 20 HP.")

    elif spell == "Holy Burst":

        enemy.hp -= 30

        typewriter("Holy Burst dealt 30 damage!")

    elif spell == "Black Flame":

        damage = SPELLS["Black Flame"]["damage"]

        enemy.hp -= damage

        typewriter(f"Black Flame dealt {damage} damage.")


def speak(enemy):

    enemy_data = ENEMIES[enemy.name]

    if "speak" not in enemy_data:
        print("They refuse to answer.")
        return

    options = list(enemy_data["speak"].keys())

    typewriter("\nSpeak")

    for i, option in enumerate(options, 1):
        typewriter(f"{i}. {option}")

    choice = input("> ")

    if not choice.isdigit():
        return

    index = int(choice) - 1

    if index < 0 or index >= len(options):
        return

    option = options[index]

    typewriter(enemy_data["speak"][option])


def awaken_relics(player):

    if hasattr(player, "killed_holis"):

        WEAPONS["Ceremonial Knife"]["damage"] = (
            WEAPONS["Ceremonial Knife"]["awakened_damage"]
        )

    if hasattr(player, "killed_elpis"):

        ARMOR["Sacrificial Garb"]["immortal"] = True

    if hasattr(player, "killed_cognifis"):

        SPELLS["Black Flame"]["damage"] = (
            SPELLS["Black Flame"]["awakened_damage"]
        )


def can_resist_reset(player):

    return (
        player.sin >= 100
        or
        player.saint >= 100
    )


def battle(player, enemy_name):

    enemy = Enemy(enemy_name)

    defending = False

    while player.hp > 0 and enemy.hp > 0:

        print("\n-------------------")
        print(enemy.name)
        typewriter(f"Enemy HP: {enemy.hp}")
        typewriter(f"Your HP: {player.hp}")

        choice = input("""
1. Attack
2. Defend
3. Speak
4. Spell
5. Inventory
> """)

        if choice == "1":

            attack_with_weapon(player, enemy)

        elif choice == "2":

            defending = True
            typewriter("You brace yourself.")

        elif choice == "3":

            speak(enemy)

        elif choice == "4":

            cast_spell(player, enemy)

        elif choice == "5":

            inventory_menu(player)

        if enemy.hp <= 0:
            break

        enemy_damage = max(
            1,
            enemy.atk - get_player_defense(player)
        )

        if defending:

            enemy_damage -= get_player_defense(player)

            if enemy_damage < 1:
                enemy_damage = 0

            defending = False

        player.hp -= enemy_damage

        typewriter(
            f"{enemy.name} dealt {enemy_damage} damage."
        )

    if player.hp <= 0:

        typewriter(f"\nYou were slain by {enemy.name}.")
        return False

    typewriter(f"\nYou defeated {enemy.name}.")

    for drop in ENEMIES[enemy_name]["drops"]:

        player.inventory.append(drop)

        typewriter(f"You obtained: {drop}")

    return True

typewriter(r"""This is a world of sinners and saints.

With the dawn of the Seven,
people began to wield powers greater than their own,
and in doing so lost their humanity
and became sinners.

They expected great reward
for their devotion to the Descended One.

However, all sinners save for the Seven
were cast into the pits of the Great Below.

Because of this, new subjects were acquired.

And then cast into the Great Below.

And again.

And again, every thousand years...

This cycle of sin and retribution
has endured for as long as any can remember.

It is the norm for sinners.
It is the norm for saints.

Then three more came.

Elpis.

Cognifis.

Holis.

The Three Virtues.

And all came to follow them.

All except seven sinners.

Seven who would not bow.

Seven who would rather be damned.

And now there are Eight.

And thus the question arises...

Art thou a sinner?

Or art thou ours?""")

player = Player()

answer = choice(
    "Narrator",
    "You're on a path that goes towards the pits of the Great Below.",
    "Retreat!",
    "Descend..."
)

if answer == "2":
    say("Narrator", "Are you sure?\n\n"
    "Choosing such choices is an object of despair.")
    
    say("Beckoner",
    "No.\n"
    "There are debts yet unpaid.\n"
    "Things yet ungathered.\n"
    "Seven artifacts necessary for entry.\n\n"
    "But forget about those.\n\n"
    "You won't be coming back until you're done here.")
if answer == "1":
    say("Narrator", "Good choice... You seem to be forgetting something in the pit, though.\n"
    "Nevertheless, godspeed, friend.\n"
    "Descend out of this dark madness!")
say("Narrator", "Once you descended out of the cycle of dreams,\n"
    "you woke up in your room with a strange feeling of deja vu. Suddenly, a creature attacks you!")
battle(player,"Lesser Sinner")