from function_defs.helper_functions import typewriter, say, choice
from function_defs.menu_utils import get_menu_selection, get_menu_index
from equippables.armors import ARMOR
from equippables.weapons import WEAPONS
from equippables.spells import SPELLS
from enemies import ENEMIES, Enemy


def attack(attacker, defender):
    """Basic attack without weapon."""
    damage = max(
        1,
        attacker.atk - defender.defense
    )

    defender.hp -= damage

    typewriter(f"{attacker.name} dealt {damage} damage.")


def attack_with_weapon(player, enemy):
    """Attack using equipped weapon."""
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
    """Calculate total defense including equipped armor."""
    defense = player.defense

    if player.armor:
        defense += ARMOR[player.armor]["defense"]

    return defense


def use_health_potion(player, inventory):
    """Use a health potion to restore HP."""
    player.hp = min(
        player.max_hp,
        player.hp + 25
    )

    inventory.remove("Health Potion")
    typewriter("Recovered 25 HP.")


def use_mana_potion(player, inventory):
    """Use a mana potion to restore mana."""
    player.mana = min(
        player.max_mana,
        player.mana + 15
    )

    inventory.remove("Mana Potion")
    typewriter("Recovered 15 Mana.")


def cast_heal_spell(player, cost):
    """Cast Heal spell."""
    if player.mana < cost:
        typewriter(f"Not enough mana! You need {cost} mana but only have {player.mana}.")
        return False
    
    player.mana -= cost
    player.hp = min(
        player.max_hp,
        player.hp + SPELLS["Heal"]["heal"]
    )
    typewriter(f"Recovered {SPELLS['Heal']['heal']} HP.")
    return True


def cast_holy_burst(player, enemy, cost):
    """Cast Holy Burst spell."""
    if player.mana < cost:
        typewriter(f"Not enough mana! You need {cost} mana but only have {player.mana}.")
        return False
    
    player.mana -= cost
    damage = SPELLS["Holy Burst"]["damage"]
    enemy.hp -= damage
    typewriter(f"Holy Burst dealt {damage} damage!")
    return True


def cast_black_flame(player, enemy, cost):
    """Cast Black Flame spell."""
    if player.mana < cost:
        typewriter(f"Not enough mana! You need {cost} mana but only have {player.mana}.")
        return False
    
    player.mana -= cost
    damage = SPELLS["Black Flame"]["damage"]
    enemy.hp -= damage
    typewriter(f"Black Flame dealt {damage} damage.")
    return True


# Spell effect dispatcher - maps spell names to their effect functions
SPELL_EFFECTS = {
    "Heal": cast_heal_spell,
    "Holy Burst": cast_holy_burst,
    "Black Flame": cast_black_flame,
}


def cast_spell(player, enemy):
    """Cast a spell from player's known spells."""
    if len(player.spells) == 0:
        typewriter("You know no spells.")
        return

    typewriter("\nSpells")
    
    # Display spells with mana costs
    for i, spell in enumerate(player.spells, 1):
        mana_cost = SPELLS[spell].get("cost", 0)
        typewriter(f"{i}. {spell} (Cost: {mana_cost} mana)")
    
    selected_spell = get_menu_selection(player.spells, show_items=False)
    
    if selected_spell is None:
        return

    # Get mana cost
    mana_cost = SPELLS[selected_spell].get("cost", 0)

    # Execute spell effect if it exists
    if selected_spell in SPELL_EFFECTS:
        if selected_spell == "Heal":
            SPELL_EFFECTS[selected_spell](player, mana_cost)
        else:
            SPELL_EFFECTS[selected_spell](player, enemy, mana_cost)


def inventory_menu(player):
    """Display inventory and allow player to use items."""
    if len(player.inventory) == 0:
        typewriter("Your inventory is empty.")
        return

    typewriter("\nInventory")

    selected_item = get_menu_selection(player.inventory, show_items=True)
    
    if selected_item is None:
        return

    # Item effect dispatcher
    if selected_item == "Health Potion":
        use_health_potion(player, player.inventory)
    elif selected_item == "Mana Potion":
        use_mana_potion(player, player.inventory)


def speak(enemy):
    """Have a conversation with an enemy."""
    enemy_data = ENEMIES[enemy.name]

    if "speak" not in enemy_data:
        typewriter("They refuse to answer.")
        return

    options = list(enemy_data["speak"].keys())

    typewriter("\nSpeak")

    selected_option = get_menu_selection(options, show_items=True)
    
    if selected_option is None:
        return

    typewriter(enemy_data["speak"][selected_option])


def battle(player, enemy_name):
    """Main battle loop with cached defense calculation and mana system."""
    enemy = Enemy(enemy_name)
    defending = False

    while player.hp > 0 and enemy.hp > 0:

        print("\n-------------------")
        print(enemy.name)
        typewriter(f"Enemy HP: {enemy.hp}")
        typewriter(f"Your HP: {player.hp}/{player.max_hp}")
        typewriter(f"Your Mana: {player.mana}/{player.max_mana}")

        choice_input = input("""
1. Attack
2. Defend
3. Speak
4. Spell
5. Inventory
> """)

        if choice_input == "1":
            attack_with_weapon(player, enemy)

        elif choice_input == "2":
            defending = True
            typewriter("You brace yourself.")

        elif choice_input == "3":
            speak(enemy)

        elif choice_input == "4":
            cast_spell(player, enemy)

        elif choice_input == "5":
            inventory_menu(player)

        if enemy.hp <= 0:
            break

        # Cache player defense for this turn
        player_defense = get_player_defense(player)
        
        enemy_damage = max(
            1,
            enemy.atk - player_defense
        )

        if defending:
            enemy_damage -= player_defense

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
