"""Mana recovery and management system."""

from function_defs.helper_functions import typewriter


def restore_mana_meditation(player, amount=10):
    """
    Restore mana through meditation.
    
    Args:
        player: Player object
        amount: Amount of mana to restore (default: 10)
    """
    player.mana = min(
        player.max_mana,
        player.mana + amount
    )
    typewriter(f"You meditate and recover {amount} mana.")
    typewriter(f"Current Mana: {player.mana}/{player.max_mana}")


def restore_mana_potion(player, inventory):
    """
    Use a mana potion to restore mana.
    
    Args:
        player: Player object
        inventory: Player's inventory list
    """
    if "Mana Potion" not in inventory:
        typewriter("You don't have any Mana Potions.")
        return False
    
    player.mana = min(
        player.max_mana,
        player.mana + 15
    )
    
    inventory.remove("Mana Potion")
    typewriter("You drink a Mana Potion and recover 15 mana.")
    typewriter(f"Current Mana: {player.mana}/{player.max_mana}")
    return True


def full_rest(player):
    """
    Full rest to recover all HP and mana.
    
    Args:
        player: Player object
    """
    player.hp = player.max_hp
    player.mana = player.max_mana
    typewriter("You rest and recover all HP and Mana.")
    typewriter(f"HP: {player.hp}/{player.max_hp}")
    typewriter(f"Mana: {player.mana}/{player.max_mana}")


def partial_rest(player):
    """
    Partial rest to recover half of max HP and mana.
    
    Args:
        player: Player object
    """
    recovery_hp = player.max_hp // 2
    recovery_mana = player.max_mana // 2
    
    player.hp = min(player.max_hp, player.hp + recovery_hp)
    player.mana = min(player.max_mana, player.mana + recovery_mana)
    
    typewriter("You rest for a while.")
    typewriter(f"Recovered {recovery_hp} HP and {recovery_mana} Mana.")
    typewriter(f"HP: {player.hp}/{player.max_hp}")
    typewriter(f"Mana: {player.mana}/{player.max_mana}")


def view_mana_status(player):
    """
    Display current mana status and recovery options.
    
    Args:
        player: Player object
    """
    mana_percent = (player.mana / player.max_mana) * 100
    
    typewriter("\n--- Mana Status ---")
    typewriter(f"Mana: {player.mana}/{player.max_mana}")
    typewriter(f"Percentage: {mana_percent:.1f}%")
    
    if player.mana < player.max_mana:
        deficit = player.max_mana - player.mana
        typewriter(f"Mana deficit: {deficit}")
    else:
        typewriter("Mana is full!")


def check_spell_availability(player, spell_name):
    """
    Check if player has enough mana to cast a spell.
    
    Args:
        player: Player object
        spell_name: Name of the spell to check
    
    Returns:
        True if player has enough mana, False otherwise
    """
    from equippables.spells import SPELLS
    
    if spell_name not in SPELLS:
        return False
    
    mana_cost = SPELLS[spell_name].get("cost", 0)
    return player.mana >= mana_cost
