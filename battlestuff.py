from helperfunctions import typewriter, say, choice
from equippables.armors import ARMOR
from main import Player, Enemy
from equippables.weapons import WEAPONS
from equippables.spells import SPELLS

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