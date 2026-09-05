import json
import os
from main import player, Player, seed, holis, cognifis, elpis, ceremonial_knife, sacrificial_garb, black_flame, altar2go

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
