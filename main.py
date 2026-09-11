from equippables.spells import SPELLS
from equippables.weapons import WEAPONS
from enemies import ENEMIES, Enemy
from equippables.armors import ARMOR
from battle_stuff import attack, attack_with_weapon, get_player_defense, inventory_menu, cast_spell, speak, battle
from function_defs.helper_functions import typewriter, say, choice
from function_defs.story_functions import awaken_relics, can_resist_reset
from function_defs.save_load_defs import save_game, load_game
from function_defs.equipment_defs import equipment_menu
from function_defs.mana_recovery import restore_mana_meditation, restore_mana_potion, full_rest, partial_rest, view_mana_status
from player import Player

seed = 0000000

ceremonial_knife = False
sacrificial_garb = False
altar2go = False
black_flame = False

elpis = False
holis = False
cognifis = False

if __name__ == "__main__":
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

    if answer == "Descend...":
        say("Narrator", "Are you sure?\n\n"
        "Choosing such choices is an object of despair.")

        say("Beckoner",
        "No.\n"
        "There are debts yet unpaid.\n"
        "Things yet ungathered.\n"
        "Seven artifacts necessary for entry.\n\n"
        "But forget about those.\n\n"
        "You won't be coming back until you're done here.")
    elif answer == "Retreat!":
        say("Narrator", "Good choice... You seem to be forgetting something in the pit, though.\n"
        "Nevertheless, godspeed, friend.\n"
        "Descend out of this dark madness!")
    say("Narrator", "Once you descended out of the cycle of dreams,\n"
        "you woke up in your room with a strange feeling of deja vu. Suddenly, a creature from the pit attacks you!")
    
    # Main game loop
    while True:
        typewriter(f"\nHP: {player.hp}/{player.max_hp} | Mana: {player.mana}/{player.max_mana}")
        
        menu_choice = choice(
            "Beckoner",
            "What would you like to do?",
            "Prepare for Battle",
            "Check Equipment",
            "Restore Mana",
            "Rest",
            "View Status"
        )
        
        if menu_choice == "Prepare for Battle":
            battle(player, "Lesser Sinner")
        elif menu_choice == "Check Equipment":
            equipment_menu(player)
        elif menu_choice == "Restore Mana":
            mana_choice = choice(
                "Beckoner",
                "How would you like to restore your mana?",
                "Meditate (10 mana)",
                "Use Mana Potion (15 mana)",
                "Back"
            )
            if mana_choice == "Meditate (10 mana)":
                restore_mana_meditation(player, 10)
            elif mana_choice == "Use Mana Potion (15 mana)":
                restore_mana_potion(player, player.inventory)
        elif menu_choice == "Rest":
            rest_choice = choice(
                "Beckoner",
                "How would you like to rest?",
                "Full Rest (recover all HP and Mana)",
                "Partial Rest (recover half HP and Mana)",
                "Back"
            )
            if rest_choice == "Full Rest (recover all HP and Mana)":
                full_rest(player)
            elif rest_choice == "Partial Rest (recover half HP and Mana)":
                partial_rest(player)
        elif menu_choice == "View Status":
            view_mana_status(player)
