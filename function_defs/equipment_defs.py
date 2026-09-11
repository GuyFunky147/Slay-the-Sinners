"""Equipment management system for equipping weapons and armor."""

from function_defs.helper_functions import typewriter
from function_defs.menu_utils import get_menu_selection
from equippables.weapons import WEAPONS
from equippables.armors import ARMOR


def equip_weapon(player):
    """Display available weapons and allow player to equip one."""
    available_weapons = list(WEAPONS.keys())
    
    typewriter("\n--- Available Weapons ---")
    typewriter(f"Currently equipped: {player.weapon if player.weapon else 'None'}\n")
    
    # Show inventory weapons
    inventory_weapons = [item for item in player.inventory if item in available_weapons]
    
    if not inventory_weapons:
        typewriter("You have no weapons in your inventory.")
        return
    
    typewriter("Your weapons:")
    selected_weapon = get_menu_selection(inventory_weapons, show_items=True)
    
    if selected_weapon is None:
        return
    
    # Unequip previous weapon if it exists
    if player.weapon:
        if player.weapon not in player.inventory:
            player.inventory.append(player.weapon)
        typewriter(f"Unequipped: {player.weapon}")
    
    # Equip new weapon
    player.weapon = selected_weapon
    player.inventory.remove(selected_weapon)
    
    weapon_data = WEAPONS[selected_weapon]
    typewriter(f"\nEquipped: {selected_weapon}")
    typewriter(f"Damage: +{weapon_data['damage']}")


def equip_armor(player):
    """Display available armor and allow player to equip one."""
    available_armor = list(ARMOR.keys())
    
    typewriter("\n--- Available Armor ---")
    typewriter(f"Currently equipped: {player.armor if player.armor else 'None'}\n")
    
    # Show inventory armor
    inventory_armor = [item for item in player.inventory if item in available_armor]
    
    if not inventory_armor:
        typewriter("You have no armor in your inventory.")
        return
    
    typewriter("Your armor:")
    selected_armor = get_menu_selection(inventory_armor, show_items=True)
    
    if selected_armor is None:
        return
    
    # Unequip previous armor if it exists
    if player.armor:
        if player.armor not in player.inventory:
            player.inventory.append(player.armor)
        typewriter(f"Unequipped: {player.armor}")
    
    # Equip new armor
    player.armor = selected_armor
    player.inventory.remove(selected_armor)
    
    armor_data = ARMOR[selected_armor]
    typewriter(f"\nEquipped: {selected_armor}")
    typewriter(f"Defense: +{armor_data['defense']}")


def view_equipment(player):
    """Display currently equipped items and their stats."""
    typewriter("\n--- Current Equipment ---")
    
    if player.weapon:
        weapon_data = WEAPONS[player.weapon]
        typewriter(f"\nWeapon: {player.weapon}")
        typewriter(f"  Damage: +{weapon_data['damage']}")
        if "fades" in weapon_data:
            typewriter(f"  Special: {weapon_data}")
    else:
        typewriter("\nWeapon: None")
    
    if player.armor:
        armor_data = ARMOR[player.armor]
        typewriter(f"\nArmor: {player.armor}")
        typewriter(f"  Defense: +{armor_data['defense']}")
        if "fades" in armor_data:
            typewriter(f"  Special: {armor_data}")
    else:
        typewriter("\nArmor: None")
    
    typewriter(f"\nTotal Stats:")
    total_atk = player.atk + (WEAPONS[player.weapon]["damage"] if player.weapon else 0)
    total_def = player.defense + (ARMOR[player.armor]["defense"] if player.armor else 0)
    typewriter(f"  Attack: {total_atk}")
    typewriter(f"  Defense: {total_def}")


def equipment_menu(player):
    """Main equipment management menu."""
    while True:
        typewriter("\n--- Equipment Menu ---")
        
        choice = input("""
1. Equip Weapon
2. Equip Armor
3. View Equipment
4. Back
> """)
        
        if choice == "1":
            equip_weapon(player)
        elif choice == "2":
            equip_armor(player)
        elif choice == "3":
            view_equipment(player)
        elif choice == "4":
            break
        else:
            typewriter("Invalid choice.")
