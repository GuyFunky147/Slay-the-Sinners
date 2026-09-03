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