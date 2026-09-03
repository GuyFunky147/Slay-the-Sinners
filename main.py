from equippables.spells import SPELLS
from equippables.weapons import WEAPONS
from enemies import ENEMIES
from equippables.armors import ARMOR
from battle_stuff import attack, attack_with_weapon, get_player_defense, inventory_menu, cast_spell, speak, battle
from function_defs.helper_functions import typewriter, say, choice
from function_defs.story_functions import awaken_relics, can_resist_reset
from function_defs.save_load_defs import save_game, load_game

seed = 0000000

ceremonial_knife = False
sacrificial_garb = False
altar2go = False
black_flame = False

elpis = False
holis = False
cognifis = False

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

class Enemy:
    def __init__(self, enemy_name):
        enemy = ENEMIES[enemy_name]

        self.name = enemy_name
        self.hp = enemy["hp"]
        self.atk = enemy["atk"]
        self.defense = enemy["def"]

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