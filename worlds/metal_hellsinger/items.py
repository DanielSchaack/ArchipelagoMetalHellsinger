from collections import Counter
from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Item, ItemClassification
from worlds.metal_hellsinger.options import (
    FillerItemsDistribution,
    IncludeProgressiveAnguishGateSkips,
    MetalHellsingerOptions,
    WinCondition,
)

if TYPE_CHECKING:
    from . import MetalHellsingerWorld
else:
    MetalHellsingerWorld = object

class ItemData(NamedTuple):
    name: str
    id: int
    group: str
    classification: ItemClassification = ItemClassification.progression
    required_num: int = 0


class MetalHellsingerItem(Item):
    game: str = "Metal: Hellsinger"

def create_item(world: "MetalHellsingerWorld", name: str) -> MetalHellsingerItem:
    item_data = item_table[name]
    if item_data.classification == ItemClassification.progression:
        classication = get_refined_classification(world.options, item_data.group, name)
    else:
        classication = item_data.classification
    return MetalHellsingerItem(name, classication, item_data.id, world.player)

def get_refined_classification(options: MetalHellsingerOptions, group: str, name: str) -> ItemClassification:
    classification = ItemClassification.progression
    if group == "Outfit" and not options.include_section_clears_with_outfits_checks:
        classification = ItemClassification.useful
    elif group == "Song" and not options.include_section_clears_with_songs_checks and name != "No Tomorrow":
        classification = ItemClassification.useful
    elif not options.include_miscellaneous_checks and (name == "The Red Right Hand Ultimate" or name == "Telos Ultimate"):
        classification = ItemClassification.useful
    return classification



def create_random_items(world: MetalHellsingerWorld, weights: dict[str, int], count: int) -> list[str]:
    filler_pool = weights.copy()
    return world.random.choices(population=list(filler_pool.keys()),
                                weights=list(filler_pool.values()),
                                k=count)

basegame_weapons = {
    # 0: "Paz",
    # 1: "Terminus",
    2: "Persephone",
    3: "The Hounds",
    4: "Vulcan",
    5: "Hellcrow",
}

option_to_weapons = {
    0: "Paz",
    1: "Terminus",
    2: "Persephone",
    3: "The Hounds",
    4: "Vulcan",
    5: "Hellcrow",
    6: "The Red Right Hand",
    7: "Telos",
    8: "Lost Persephone",
    9: "Manifested Persephone",
    10: "The Lost Hounds",
    11: "Lost Vulcan",
}


option_to_difficulty = {
    0: "Lamb",
    1: "Goat",
    2: "Beast",
    3: "Archdevil",
}

option_to_hells = {
    0: "Voke",
    1: "Stygia",
    2: "Yhelm",
    3: "Incaustis",
    4: "Gehenna",
    5: "Nihil",
    6: "Acheron",
    7: "Sheol",
}

basegame_outfits = {
    0: "Outfit of the Unknown",
    1: "Outfit of the Leviathan",
}
option_to_outfits = {
    0: "Outfit of the Unknown",
    1: "Outfit of the Leviathan",
    2: "Outfit of the Dark Devotee",
    3: "Outfit of the Morning Star",
    4: "Outfit of the Angel Eyes",
    5: "Outfit of the Obsidian",
    6: "Outfit of the Amethyst",
    7: "Outfit of the Chromatica",
}

basegame_main_songs = {
    0: "This is the End",
    1: "Stygia (Song)",
    2: "Burial At Night",
    3: "This Devastation",
    4: "Poetry of Cinder",
    5: "Dissolution",
    6: "Acheron (Song)",
    7: "Silent No More",
}

basegame_boss_songs = {
    0: "Blood and Law",
    1: "Infernal Invocation I: Hopes and Fears",
    2: "Infernal Invocation II: Defiance",
    3: "Infernal Invocation III: Dreaming in Distortion",
    4: "No Tomorrow",
}

def create_hells_item_pool(world: MetalHellsingerWorld) -> tuple[list[str], int]:
    required_items_dict: dict[str, int] = {}
    required_items: list[ItemData] = []
    placed_items = 0
    if world.options.win_condition == WinCondition.option_hells_completion or world.options.win_condition == WinCondition.option_sheol_completion:
        world.push_precollected(world.create_item("Hells"))

        if world.options.regressive_difficulty:
            world.push_precollected(world.create_item("Regressive Difficulty"))
            required_items_dict["Regressive Difficulty"] = 3
        else:
            required_difficulty = world.options.starting_difficulty.value if world.options.starting_difficulty.value >= world.options.minimal_difficulty.value else world.options.minimal_difficulty.value
            option = option_to_difficulty[required_difficulty]
            world.push_precollected(world.create_item(option))
            available_diff = list(option_to_difficulty.values())
            available_diff.remove(option)
            required_items.extend(item_table[diff] for diff in available_diff)

        required_items.append(item_table["Tutorial"])

        if world.options.hells_unlocks_as_progressive:
            world.push_precollected(world.create_item("Progressive Hells"))
            required_items_dict["Progressive Hells"] = 7
        else:
            option = option_to_hells[world.options.starting_hells.value]
            world.push_precollected(world.create_item(option))
            available_hells = list(option_to_hells.values())
            available_hells.remove(option)
            required_items.extend(item_table[hells] for hells in available_hells)

        if world.options.randomized_torments_enabled:
            if world.options.torment_unlocks_as_progressive:
                required_items.append(item_table["Progressive Killing with Rhythm"])
                required_items.append(item_table["Progressive Weapon Trickery"])
                required_items.append(item_table["Progressive Relic Thief"])
                required_items.append(item_table["Progressive Giantslayer"])
                required_items.append(item_table["Progressive Death's Edge"])
                required_items.append(item_table["Progressive Ultimate Mastery"])
                required_items.append(item_table["Progressive Slaughter Mastery"])
            else:
                required_items.append(item_table["Killing with Rhythm: 1"])
                required_items.append(item_table["Killing with Rhythm: 2"])
                required_items.append(item_table["Killing with Rhythm: 3"])
                required_items.append(item_table["Weapon Trickery: 1"])
                required_items.append(item_table["Weapon Trickery: 2"])
                required_items.append(item_table["Weapon Trickery: 3"])
                required_items.append(item_table["Relic Thief: 1"])
                required_items.append(item_table["Relic Thief: 2"])
                required_items.append(item_table["Relic Thief: 3"])
                required_items.append(item_table["Giantslayer: 1"])
                required_items.append(item_table["Giantslayer: 2"])
                required_items.append(item_table["Giantslayer: 3"])
                required_items.append(item_table["Death's Edge: 1"])
                required_items.append(item_table["Death's Edge: 2"])
                required_items.append(item_table["Death's Edge: 3"])
                required_items.append(item_table["Ultimate Mastery: 1"])
                required_items.append(item_table["Ultimate Mastery: 2"])
                required_items.append(item_table["Ultimate Mastery: 3"])
                required_items.append(item_table["Slaughter Mastery: 1"])
                required_items.append(item_table["Slaughter Mastery: 2"])
                required_items.append(item_table["Slaughter Mastery: 3"])

        required_items.append(item_table["Progressive Streak Guardian"])
        required_items.append(item_table["Progressive Ghost Rounds"])
        required_items.append(item_table["Progressive Boon Momentum"])
        required_items.append(item_table["Progressive Unyielding Fury"])
        required_items.append(item_table["Progressive Last Breath Aegis"])
        required_items.append(item_table["Progressive Ultimate Sovereignty"])
        required_items.append(item_table["Progressive The Perfectionist"])

        is_random_weapon = False
        available_weapon = list(basegame_weapons.values())
        if world.options.include_additional_weapon_variants:
            available_weapon.append("Lost Persephone")
            available_weapon.append("Manifested Persephone")
            available_weapon.append("The Lost Hounds")
            available_weapon.append("Lost Vulcan")

        if world.options.include_dream_of_the_beast_weapon:
            available_weapon.append("The Red Right Hand")

        if world.options.include_purgatory_weapon:
            available_weapon.append("Telos")

        if world.options.starting_weapon.value == 6 and not world.options.include_dream_of_the_beast_weapon:
            is_random_weapon = True

        if world.options.starting_weapon.value == 7 and not world.options.include_purgatory_weapon:
            is_random_weapon = True

        if world.options.starting_weapon.value in (8, 9, 10, 11) and not world.options.include_additional_weapon_variants:
            is_random_weapon = True

        if is_random_weapon:
            weapon = world.random.choice(available_weapon)
            world.push_precollected(world.create_item(weapon))
            available_weapon.remove(weapon)
        else:
            weapon = option_to_weapons[world.options.starting_weapon.value]
            world.push_precollected(world.create_item(weapon))
            available_weapon.remove(weapon)

        required_items.extend(item_table[weapon] for weapon in available_weapon)
        required_items.append(item_table["Paz"])
        required_items.append(item_table["Terminus"])

        if world.options.randomized_weapon_ultimates_enabled:
            required_items.append(item_table["Paz Ultimate"])
            required_items.append(item_table["Terminus Ultimate"])
            required_items.append(item_table["Persephone Ultimate"])
            required_items.append(item_table["The Hounds Ultimate"])
            required_items.append(item_table["Vulcan Ultimate"])
            required_items.append(item_table["Hellcrow Ultimate"])

            if world.options.include_dream_of_the_beast_weapon:
                required_items.append(item_table["The Red Right Hand Ultimate"])

            if world.options.include_purgatory_weapon:
                required_items.append(item_table["Telos Ultimate"])

        if world.options.randomized_songs_enabled:
            selected_main_song = basegame_main_songs[world.options.starting_main_song.value]
            world.push_precollected(world.create_item(selected_main_song))
            main_songs = list(basegame_main_songs.values())
            main_songs.remove(selected_main_song)
            required_items.extend(item_table[song] for song in main_songs)

            selected_boss_song = basegame_boss_songs[world.options.starting_boss_song.value]
            world.push_precollected(world.create_item(selected_boss_song))
            boss_songs = list(basegame_boss_songs.values())
            boss_songs.remove(selected_boss_song)
            required_items.extend(item_table[song] for song in boss_songs)

            if world.options.include_dream_of_the_beast_songs:
                required_items.append(item_table["Leviathan (Song)"])
                required_items.append(item_table["Dream of the Beast"])
            if world.options.include_purgatory_songs:
                required_items.append(item_table["Swallow the Fire"])
                required_items.append(item_table["Mouth of Hell"])
                required_items.append(item_table["Goodbye, Morning Star"])
            if world.options.include_dusk_soundtrack_songs:
                required_items.append(item_table["Departure to Destruction"])
                required_items.append(item_table["Hand Cannon"])
                required_items.append(item_table["Burn in Hell"])
                required_items.append(item_table["Murder Machine Inc"])
                required_items.append(item_table["Endless"])
                required_items.append(item_table["Mine Control"])
                required_items.append(item_table["Sacrifice"])
                required_items.append(item_table["Erebus Reaction"])
                required_items.append(item_table["Bleeding Out"])
            if world.options.include_essential_hits_soundtrack_songs:
                required_items.append(item_table["Down With the Sickness"])
                required_items.append(item_table["Uprising"])
                required_items.append(item_table["Misery Business"])
                required_items.append(item_table["Tsunami (Original Mix)"])
                required_items.append(item_table["Runaway (U&I)"])
                required_items.append(item_table["Feel Good Inc."])
                required_items.append(item_table["I Love It feat. Charli XCX"])
                required_items.append(item_table["Personal Jesus"])

        if world.options.randomized_outfits_enabled:
            is_random_outfit = False
            available_outfit = list(basegame_outfits.values())
            if world.options.include_dream_of_the_beast_outfits:
                available_outfit.append("Outfit of the Dark Devotee")
                available_outfit.append("Outfit of the Morning Star")
                available_outfit.append("Outfit of the Angel Eyes")
            if world.options.include_purgatory_outfits:
                available_outfit.append("Outfit of the Obsidian")
                available_outfit.append("Outfit of the Amethyst")
                available_outfit.append("Outfit of the Chromatica")

            if world.options.starting_outfit.value in (2, 3, 4) and not world.options.include_dream_of_the_beast_outfits:
                is_random_outfit = True
            if world.options.starting_outfit.value in (5, 6, 7) and not world.options.include_purgatory_outfits:
                is_random_outfit = True

            if is_random_outfit:
                outfit = world.random.choice(available_outfit)
                world.push_precollected(world.create_item(outfit))
                available_outfit.remove(outfit)
            else:
                outfit = option_to_outfits[world.options.starting_outfit.value]
                world.push_precollected(world.create_item(outfit))
                available_outfit.remove(outfit)

            required_items.extend(item_table[outfit] for outfit in available_outfit)

        if world.options.include_coat_of_arms_checks:
            required_items.append(item_table["Coat of Arms"])
        elif world.options.require_coat_of_arms_for_sheol:
            loc_names = world.location_name_groups["CoatOfArms"]
            for loc in loc_names:
                if not loc.startswith("Sheol"):
                    world.multiworld.get_location(loc, world.player).place_locked_item(world.create_item("Coat of Arms"))
                    placed_items+=1

            required_items_dict["Coat of Arms"] = 4
        elif world.options.include_randomized_weapon_skins_checks:
            loc_names = world.location_name_groups["CoatOfArms"]
            for loc in loc_names:
                world.multiworld.get_location(loc, world.player).place_locked_item( world.create_item("Coat of Arms"))
                placed_items+=1

        if world.options.randomized_boons_enabled:
            required_items.append(item_table["Enduring Fury"])
            required_items.append(item_table["Faster Ultimate Gain"])
            required_items.append(item_table["Deadlier Dash"])
            required_items.append(item_table["Explosive Slaughter"])

        if world.options.randomized_dash_enabled:
            required_items.append(item_table["Progressive Dash"])

        if world.options.randomized_jump_enabled:
            required_items.append(item_table["Progressive Jump"])

        if world.options.randomized_reload_enabled:
            required_items.append(item_table["Progressive Reload"])

        if world.options.randomized_slaughter_enabled:
            required_items.append(item_table["Slaughter"])

        if world.options.destructible_as_unlocks:
            required_items.append(item_table["Destructible Ammostashes"])
            required_items.append(item_table["Destructible Health Crystals"])
            required_items.append(item_table["Destructible Chaos Crystals"])

        if world.options.include_randomized_weapon_skins_checks:
            required_items.append(item_table["Paz Skin"])
            required_items.append(item_table["Terminus Skin"])
            required_items.append(item_table["Persephone Skin"])
            required_items.append(item_table["The Hounds Skin"])
            required_items.append(item_table["Vulcan Skin"])
            required_items.append(item_table["Hellcrow Skin"])

        if world.options.require_aspect_for_boss_arena:
            required_items.append(item_table["Aspect of Anger"])
            required_items.append(item_table["Aspect of the Charged"])
            required_items.append(item_table["Aspect of the Fortress"])
            required_items.append(item_table["Aspect of Infernal Fury"])
            required_items.append(item_table["Aspect of the Hellstorm"])
            required_items.append(item_table["Aspect of the Doppelganger"])
            required_items.append(item_table["Aspect of the Wheel"])

        if world.options.include_progressive_anguish_gate_skips == IncludeProgressiveAnguishGateSkips.option_encounter_skips_for_completions:
            for hell in option_to_hells.values():
                item_name = f"Progressive {hell} Anguish Gate Skip"
                for i  in range(1,5):
                    location_name = f"{hell} - Finished forced Encounter {i}"
                    world.multiworld.get_location(location_name, world.player).place_locked_item(world.create_item(item_name))
                    placed_items += 1

        if world.options.include_progressive_anguish_gate_skips == IncludeProgressiveAnguishGateSkips.option_randomized_progressive_encounter_skips:
            for hell in option_to_hells.values():
                item_name = f"Progressive {hell} Anguish Gate Skip"
                required_items.append(item_table[item_name])

        if world.options.include_progressive_anguish_gate_skips == IncludeProgressiveAnguishGateSkips.option_randomized_individual_encounter_skips:
            for hell in option_to_hells.values():
                for i  in range(1,5):
                    item_name = f"{hell} Anguish Gate {i} Skip"
                    required_items.append(item_table[item_name])

    required_items_dict.update({item.name: item.required_num for item in required_items})
    return list(Counter(required_items_dict).elements()), placed_items

# TODO: leviathan integration
def create_leviathan_item_pool(world: MetalHellsingerWorld) -> tuple[list[str], int]:
    required_items: dict[str, int] = {}
    placed_items = 0
    return list(Counter(required_items).elements()), placed_items

def create_all_items(world: MetalHellsingerWorld) -> None:
    player = world.player
    locations_to_fill = len(world.multiworld.get_unfilled_locations(player))

    hells_items, placed_hells_items = create_hells_item_pool(world)
    leviathan_item, placed_leviathan_items = create_leviathan_item_pool(world)
    itempool = hells_items + leviathan_item

    required_filler = locations_to_fill - len(itempool) - (placed_hells_items + placed_leviathan_items)
    filler_items_distribution = world.options.filler_items_distribution.value.copy()
    if sum(filler_items_distribution.values()) == 0:
        filler_items_distribution = FillerItemsDistribution.default.copy()
    itempool += create_random_items(
        world, filler_items_distribution, required_filler
    )

    world.multiworld.itempool += [create_item(world, name) for name in itempool]


item_table: dict[str, ItemData] = {
    "Hells": ItemData("Hells", 1, "Gamemode", ItemClassification.progression, 1),
    "Leviathan": ItemData("Leviathan", 2, "Gamemode", ItemClassification.progression, 1),
    "Enduring Fury": ItemData("Enduring Fury", 3, "Ability", ItemClassification.progression, 1),
    "Faster Ultimate Gain": ItemData("Faster Ultimate Gain", 4, "Ability", ItemClassification.progression, 1),
    "Deadlier Dash": ItemData("Deadlier Dash", 5, "Ability", ItemClassification.progression, 1),
    "Explosive Slaughter": ItemData("Explosive Slaughter", 6, "Ability", ItemClassification.progression, 1),
    "Regressive Difficulty": ItemData("Regressive Difficulty", 7, "Difficulty", ItemClassification.progression, 1),
    "Archdevil": ItemData("Archdevil", 8, "Difficulty", ItemClassification.progression, 1),
    "Beast": ItemData("Beast", 9, "Difficulty", ItemClassification.progression, 1),
    "Goat": ItemData("Goat", 10, "Difficulty", ItemClassification.progression, 1),
    "Lamb": ItemData("Lamb", 11, "Difficulty", ItemClassification.progression, 1),
    "Progressive Killing with Rhythm": ItemData("Progressive Killing with Rhythm", 12, "Torment", ItemClassification.progression, 3),
    "Killing with Rhythm: 1": ItemData("Killing with Rhythm: 1", 13, "Torment", ItemClassification.progression, 1),
    "Killing with Rhythm: 2": ItemData("Killing with Rhythm: 2", 14, "Torment", ItemClassification.progression, 1),
    "Killing with Rhythm: 3": ItemData("Killing with Rhythm: 3", 15, "Torment", ItemClassification.progression, 1),
    "Progressive Weapon Trickery": ItemData("Progressive Weapon Trickery", 16, "Torment", ItemClassification.progression, 3),
    "Weapon Trickery: 1": ItemData("Weapon Trickery: 1", 17, "Torment", ItemClassification.progression, 1),
    "Weapon Trickery: 2": ItemData("Weapon Trickery: 2", 18, "Torment", ItemClassification.progression, 1),
    "Weapon Trickery: 3": ItemData("Weapon Trickery: 3", 19, "Torment", ItemClassification.progression, 1),
    "Progressive Relic Thief": ItemData("Progressive Relic Thief", 20, "Torment", ItemClassification.progression, 3),
    "Relic Thief: 1": ItemData("Relic Thief: 1", 21, "Torment", ItemClassification.progression, 1),
    "Relic Thief: 2": ItemData("Relic Thief: 2", 22, "Torment", ItemClassification.progression, 1),
    "Relic Thief: 3": ItemData("Relic Thief: 3", 23, "Torment", ItemClassification.progression, 1),
    "Progressive Giantslayer": ItemData("Progressive Giantslayer", 24, "Torment", ItemClassification.progression, 3),
    "Giantslayer: 1": ItemData("Giantslayer: 1", 25, "Torment", ItemClassification.progression, 1),
    "Giantslayer: 2": ItemData("Giantslayer: 2", 26, "Torment", ItemClassification.progression, 1),
    "Giantslayer: 3": ItemData("Giantslayer: 3", 27, "Torment", ItemClassification.progression, 1),
    "Progressive Death's Edge": ItemData("Progressive Death's Edge", 28, "Torment", ItemClassification.progression, 3),
    "Death's Edge: 1": ItemData("Death's Edge: 1", 29, "Torment", ItemClassification.progression, 1),
    "Death's Edge: 2": ItemData("Death's Edge: 2", 30, "Torment", ItemClassification.progression, 1),
    "Death's Edge: 3": ItemData("Death's Edge: 3", 31, "Torment", ItemClassification.progression, 1),
    "Progressive Ultimate Mastery": ItemData("Progressive Ultimate Mastery", 32, "Torment", ItemClassification.progression, 3),
    "Ultimate Mastery: 1": ItemData("Ultimate Mastery: 1", 33, "Torment", ItemClassification.progression, 1),
    "Ultimate Mastery: 2": ItemData("Ultimate Mastery: 2", 34, "Torment", ItemClassification.progression, 1),
    "Ultimate Mastery: 3": ItemData("Ultimate Mastery: 3", 35, "Torment", ItemClassification.progression, 1),
    "Progressive Slaughter Mastery": ItemData("Progressive Slaughter Mastery", 36, "Torment", ItemClassification.progression, 3),
    "Slaughter Mastery: 1": ItemData("Slaughter Mastery: 1", 37, "Torment", ItemClassification.progression, 1),
    "Slaughter Mastery: 2": ItemData("Slaughter Mastery: 2", 38, "Torment", ItemClassification.progression, 1),
    "Slaughter Mastery: 3": ItemData("Slaughter Mastery: 3", 39, "Torment", ItemClassification.progression, 1),
    "Progressive Hells": ItemData("Progressive Hells", 50, "Level", ItemClassification.progression, 8),
    "Voke": ItemData("Voke", 51, "Level", ItemClassification.progression, 1),
    "Stygia": ItemData("Stygia", 52, "Level", ItemClassification.progression, 1),
    "Yhelm": ItemData("Yhelm", 53, "Level", ItemClassification.progression, 1),
    "Incaustis": ItemData("Incaustis", 54, "Level", ItemClassification.progression, 1),
    "Gehenna": ItemData("Gehenna", 55, "Level", ItemClassification.progression, 1),
    "Nihil": ItemData("Nihil", 56, "Level", ItemClassification.progression, 1),
    "Acheron": ItemData("Acheron", 57, "Level", ItemClassification.progression, 1),
    "Sheol": ItemData("Sheol", 58, "Level", ItemClassification.progression, 1),
    "Tutorial": ItemData("Tutorial", 59, "Level", ItemClassification.progression, 1),
    "Coat of Arms": ItemData("Coat of Arms", 60, "Collectible", ItemClassification.progression, 32),
    "Garden of Chronos": ItemData("Garden of Chronos", 62, "Level", ItemClassification.progression, 1),
    "Calamity": ItemData("Calamity", 63, "Level", ItemClassification.progression, 1),
    "Demonitorium": ItemData("Demonitorium", 64, "Level", ItemClassification.progression, 1),
    "Tombs of the Ancients": ItemData("Tombs of the Ancients", 65, "Level", ItemClassification.progression, 1),
    "Necropolis": ItemData("Necropolis", 66, "Level", ItemClassification.progression, 1),
    "Axiom": ItemData("Axiom", 67, "Level", ItemClassification.progression, 1),
    "Final Destination": ItemData("Final Destination", 68, "Level", ItemClassification.progression, 1),
    "Progressive Tutorial Anguish Gate Skip": ItemData("Progressive Tutorial Anguish Gate Skip", 70, "AnguishGate", ItemClassification.useful, 4),
    "Tutorial Anguish Gate 1 Skip": ItemData("Tutorial Anguish Gate 1 Skip", 71, "AnguishGate", ItemClassification.useful, 1),
    "Progressive Voke Anguish Gate Skip": ItemData("Progressive Voke Anguish Gate Skip", 72, "AnguishGate", ItemClassification.useful, 4),
    "Voke Anguish Gate 1 Skip": ItemData("Voke Anguish Gate 1 Skip", 73, "AnguishGate", ItemClassification.useful, 1),
    "Voke Anguish Gate 2 Skip": ItemData("Voke Anguish Gate 2 Skip", 74, "AnguishGate", ItemClassification.useful, 1),
    "Voke Anguish Gate 3 Skip": ItemData("Voke Anguish Gate 3 Skip", 75, "AnguishGate", ItemClassification.useful, 1),
    "Voke Anguish Gate 4 Skip": ItemData("Voke Anguish Gate 4 Skip", 76, "AnguishGate", ItemClassification.useful, 1),
    "Progressive Stygia Anguish Gate Skip": ItemData("Progressive Stygia Anguish Gate Skip", 77, "AnguishGate", ItemClassification.useful, 4),
    "Stygia Anguish Gate 1 Skip": ItemData("Stygia Anguish Gate 1 Skip", 78, "AnguishGate", ItemClassification.useful, 1),
    "Stygia Anguish Gate 2 Skip": ItemData("Stygia Anguish Gate 2 Skip", 79, "AnguishGate", ItemClassification.useful, 1),
    "Stygia Anguish Gate 3 Skip": ItemData("Stygia Anguish Gate 3 Skip", 80, "AnguishGate", ItemClassification.useful, 1),
    "Stygia Anguish Gate 4 Skip": ItemData("Stygia Anguish Gate 4 Skip", 81, "AnguishGate", ItemClassification.useful, 1),
    "Progressive Yhelm Anguish Gate Skip": ItemData("Progressive Yhelm Anguish Gate Skip", 82, "AnguishGate", ItemClassification.useful, 4),
    "Yhelm Anguish Gate 1 Skip": ItemData("Yhelm Anguish Gate 1 Skip", 83, "AnguishGate", ItemClassification.useful, 1),
    "Yhelm Anguish Gate 2 Skip": ItemData("Yhelm Anguish Gate 2 Skip", 84, "AnguishGate", ItemClassification.useful, 1),
    "Yhelm Anguish Gate 3 Skip": ItemData("Yhelm Anguish Gate 3 Skip", 85, "AnguishGate", ItemClassification.useful, 1),
    "Yhelm Anguish Gate 4 Skip": ItemData("Yhelm Anguish Gate 4 Skip", 86, "AnguishGate", ItemClassification.useful, 1),
    "Progressive Incaustis Anguish Gate Skip": ItemData("Progressive Incaustis Anguish Gate Skip", 87, "AnguishGate", ItemClassification.useful, 4),
    "Incaustis Anguish Gate 1 Skip": ItemData("Incaustis Anguish Gate 1 Skip", 88, "AnguishGate", ItemClassification.useful, 1),
    "Incaustis Anguish Gate 2 Skip": ItemData("Incaustis Anguish Gate 2 Skip", 89, "AnguishGate", ItemClassification.useful, 1),
    "Incaustis Anguish Gate 3 Skip": ItemData("Incaustis Anguish Gate 3 Skip", 90, "AnguishGate", ItemClassification.useful, 1),
    "Incaustis Anguish Gate 4 Skip": ItemData("Incaustis Anguish Gate 4 Skip", 91, "AnguishGate", ItemClassification.useful, 1),
    "Progressive Gehenna Anguish Gate Skip": ItemData("Progressive Gehenna Anguish Gate Skip", 92, "AnguishGate", ItemClassification.useful, 4),
    "Gehenna Anguish Gate 1 Skip": ItemData("Gehenna Anguish Gate 1 Skip", 93, "AnguishGate", ItemClassification.useful, 1),
    "Gehenna Anguish Gate 2 Skip": ItemData("Gehenna Anguish Gate 2 Skip", 94, "AnguishGate", ItemClassification.useful, 1),
    "Gehenna Anguish Gate 3 Skip": ItemData("Gehenna Anguish Gate 3 Skip", 95, "AnguishGate", ItemClassification.useful, 1),
    "Gehenna Anguish Gate 4 Skip": ItemData("Gehenna Anguish Gate 4 Skip", 96, "AnguishGate", ItemClassification.useful, 1),
    "Progressive Nihil Anguish Gate Skip": ItemData("Progressive Nihil Anguish Gate Skip", 97, "AnguishGate", ItemClassification.useful, 4),
    "Nihil Anguish Gate 1 Skip": ItemData("Nihil Anguish Gate 1 Skip", 98, "AnguishGate", ItemClassification.useful, 1),
    "Nihil Anguish Gate 2 Skip": ItemData("Nihil Anguish Gate 2 Skip", 99, "AnguishGate", ItemClassification.useful, 1),
    "Nihil Anguish Gate 3 Skip": ItemData("Nihil Anguish Gate 3 Skip", 100, "AnguishGate", ItemClassification.useful, 1),
    "Nihil Anguish Gate 4 Skip": ItemData("Nihil Anguish Gate 4 Skip", 101, "AnguishGate", ItemClassification.useful, 1),
    "Progressive Acheron Anguish Gate Skip": ItemData("Progressive Acheron Anguish Gate Skip", 102, "AnguishGate", ItemClassification.useful, 4),
    "Acheron Anguish Gate 1 Skip": ItemData("Acheron Anguish Gate 1 Skip", 103, "AnguishGate", ItemClassification.useful, 1),
    "Acheron Anguish Gate 2 Skip": ItemData("Acheron Anguish Gate 2 Skip", 104, "AnguishGate", ItemClassification.useful, 1),
    "Acheron Anguish Gate 3 Skip": ItemData("Acheron Anguish Gate 3 Skip", 105, "AnguishGate", ItemClassification.useful, 1),
    "Acheron Anguish Gate 4 Skip": ItemData("Acheron Anguish Gate 4 Skip", 106, "AnguishGate", ItemClassification.useful, 1),
    "Progressive Sheol Anguish Gate Skip": ItemData("Progressive Sheol Anguish Gate Skip", 107, "AnguishGate", ItemClassification.useful, 4),
    "Sheol Anguish Gate 1 Skip": ItemData("Sheol Anguish Gate 1 Skip", 108, "AnguishGate", ItemClassification.useful, 1),
    "Sheol Anguish Gate 2 Skip": ItemData("Sheol Anguish Gate 2 Skip", 109, "AnguishGate", ItemClassification.useful, 1),
    "Sheol Anguish Gate 3 Skip": ItemData("Sheol Anguish Gate 3 Skip", 110, "AnguishGate", ItemClassification.useful, 1),
    "Sheol Anguish Gate 4 Skip": ItemData("Sheol Anguish Gate 4 Skip", 111, "AnguishGate", ItemClassification.useful, 1),
    "Progressive Streak Guardian": ItemData("Progressive Streak Guardian", 120, "Sigil", ItemClassification.useful, 3),
    "Progressive Ghost Rounds": ItemData("Progressive Ghost Rounds", 121, "Sigil", ItemClassification.useful, 3),
    "Progressive Boon Momentum": ItemData("Progressive Boon Momentum", 122, "Sigil", ItemClassification.useful, 3),
    "Progressive Unyielding Fury": ItemData("Progressive Unyielding Fury", 123, "Sigil", ItemClassification.useful, 3),
    "Progressive Last Breath Aegis": ItemData("Progressive Last Breath Aegis", 124, "Sigil", ItemClassification.useful, 3),
    "Progressive Ultimate Sovereignty": ItemData("Progressive Ultimate Sovereignty", 125, "Sigil", ItemClassification.useful, 3),
    "Progressive The Perfectionist": ItemData("Progressive The Perfectionist", 126, "Sigil", ItemClassification.useful, 3),
    "Paz": ItemData("Paz", 130, "Weapon", ItemClassification.progression, 1),
    "Paz Ultimate": ItemData("Paz Ultimate", 131, "WeaponUpgrade", ItemClassification.progression, 1),
    "Terminus": ItemData("Terminus", 132, "Weapon", ItemClassification.progression, 1),
    "Terminus Ultimate": ItemData("Terminus Ultimate", 133, "WeaponUpgrade", ItemClassification.progression, 1),
    "Persephone": ItemData("Persephone", 134, "Weapon", ItemClassification.progression, 1),
    "Persephone Ultimate": ItemData("Persephone Ultimate", 135, "WeaponUpgrade", ItemClassification.progression, 1),
    "Lost Persephone": ItemData("Lost Persephone", 136, "Weapon", ItemClassification.progression, 1),
    "Manifested Persephone": ItemData("Manifested Persephone", 137, "Weapon", ItemClassification.progression, 1),
    "The Hounds": ItemData("The Hounds", 138, "Weapon", ItemClassification.progression, 1),
    "The Hounds Ultimate": ItemData("The Hounds Ultimate", 139, "WeaponUpgrade", ItemClassification.progression, 1),
    "The Lost Hounds": ItemData("The Lost Hounds", 140, "Weapon", ItemClassification.progression, 1),
    "Vulcan": ItemData("Vulcan", 141, "Weapon", ItemClassification.progression, 1),
    "Vulcan Ultimate": ItemData("Vulcan Ultimate", 142, "WeaponUpgrade", ItemClassification.progression, 1),
    "Lost Vulcan": ItemData("Lost Vulcan", 143, "Weapon", ItemClassification.progression, 1),
    "Hellcrow": ItemData("Hellcrow", 144, "Weapon", ItemClassification.progression, 1),
    "Hellcrow Ultimate": ItemData("Hellcrow Ultimate", 145, "WeaponUpgrade", ItemClassification.progression, 1),
    "The Red Right Hand": ItemData("The Red Right Hand", 146, "Weapon", ItemClassification.progression, 1),
    "The Red Right Hand Ultimate": ItemData("The Red Right Hand Ultimate", 147, "WeaponUpgrade", ItemClassification.progression, 1),
    "Telos": ItemData("Telos", 148, "Weapon", ItemClassification.progression, 1),
    "Telos Ultimate": ItemData("Telos Ultimate", 149, "WeaponUpgrade", ItemClassification.progression, 1),
    "Paz Skin": ItemData("Paz Skin", 150, "Skin", ItemClassification.filler, 1),
    "Terminus Skin": ItemData("Terminus Skin", 151, "Skin", ItemClassification.filler, 1),
    "Persephone Skin": ItemData("Persephone Skin", 152, "Skin", ItemClassification.filler, 1),
    "The Hounds Skin": ItemData("The Hounds Skin", 153, "Skin", ItemClassification.filler, 1),
    "Vulcan Skin": ItemData("Vulcan Skin", 154, "Skin", ItemClassification.filler, 1),
    "Hellcrow Skin": ItemData("Hellcrow Skin", 155, "Skin", ItemClassification.filler, 1),
    "Progressive Dash": ItemData("Progressive Dash", 160, "Ability", ItemClassification.progression, 2),
    "Dash": ItemData("Dash", 161, "Ability", ItemClassification.progression, 1),
    "Soar": ItemData("Soar", 162, "Ability", ItemClassification.progression, 1),
    "Progressive Jump": ItemData("Progressive Jump", 163, "Ability", ItemClassification.progression, 3),
    "Jump": ItemData("Jump", 164, "Ability", ItemClassification.progression, 1),
    "Double Jump": ItemData("Double Jump", 165, "Ability", ItemClassification.progression, 1),
    "Infinite Jump": ItemData("Infinite Jump", 166, "Ability", ItemClassification.progression, 1),
    "Progressive Reload": ItemData("Progressive Reload", 167, "Ability", ItemClassification.progression, 2),
    "Quick Reload": ItemData("Quick Reload", 168, "Ability", ItemClassification.progression, 1),
    "Manual Reload": ItemData("Manual Reload", 169, "Ability", ItemClassification.progression, 1),
    "Destructible Ammostashes": ItemData("Destructible Ammostashes", 170, "Ability", ItemClassification.progression, 1),
    "Destructible Health Crystals": ItemData("Destructible Health Crystals", 171, "Ability", ItemClassification.progression, 1),
    "Destructible Chaos Crystals": ItemData("Destructible Chaos Crystals", 172, "Ability", ItemClassification.progression, 1),
    "Slaughter": ItemData("Slaughter", 173, "Ability", ItemClassification.progression, 1),
    "Aspect of Anger": ItemData("Aspect of Anger", 180, "Aspect", ItemClassification.progression, 1),
    "Aspect of the Charged": ItemData("Aspect of the Charged", 181, "Aspect", ItemClassification.progression, 1),
    "Aspect of the Fortress": ItemData("Aspect of the Fortress", 182, "Aspect", ItemClassification.progression, 1),
    "Aspect of Infernal Fury": ItemData("Aspect of Infernal Fury", 183, "Aspect", ItemClassification.progression, 1),
    "Aspect of the Hellstorm": ItemData("Aspect of the Hellstorm", 184, "Aspect", ItemClassification.progression, 1),
    "Aspect of the Doppelganger": ItemData("Aspect of the Doppelganger", 185, "Aspect", ItemClassification.progression, 1),
    "Aspect of the Wheel": ItemData("Aspect of the Wheel", 186, "Aspect", ItemClassification.progression, 1),
    "Progressive Dream of the Heartbeat of Leviathan": ItemData("Progressive Dream of the Heartbeat of Leviathan", 310, "Dream", ItemClassification.useful, 4),
    "Progressive Dream of Stubborn Outrage": ItemData("Progressive Dream of Stubborn Outrage", 311, "Dream", ItemClassification.useful, 3),
    "Dream of Ultimate Pots": ItemData("Dream of Ultimate Pots", 312, "Dream", ItemClassification.useful, 1),
    "Dream of Dress for Success": ItemData("Dream of Dress for Success", 313, "Dream", ItemClassification.useful, 1),
    "Dream of Extra Memory": ItemData("Dream of Extra Memory", 314, "Dream", ItemClassification.useful, 1),
    "Progressive Dream of Strategic Withdrawal": ItemData("Progressive Dream of Strategic Withdrawal", 320, "Dream", ItemClassification.progression, 2),
    "Dream of Bloodthirst": ItemData("Dream of Bloodthirst", 321, "Dream", ItemClassification.progression, 1),
    "Dream of to Charge or not to Charge": ItemData("Dream of to Charge or not to Charge", 322, "Dream", ItemClassification.useful, 3),
    "Progressive Dream of Hellcrow": ItemData("Progressive Dream of Hellcrow", 323, "Dream", ItemClassification.progression, 5),
    "Progressive Dream of The Hounds": ItemData("Progressive Dream of The Hounds", 324, "Dream", ItemClassification.progression, 5),
    "Progressive Dream of The Lost Hounds": ItemData("Progressive Dream of The Lost Hounds", 325, "Dream", ItemClassification.progression, 5),
    "Progressive Dream of Persephone": ItemData("Progressive Dream of Persephone", 326, "Dream", ItemClassification.progression, 5),
    "Progressive Dream of Lost Persephone": ItemData("Progressive Dream of Lost Persephone", 327, "Dream", ItemClassification.progression, 5),
    "Progressive Dream of Manifested Persephone": ItemData("Progressive Dream of Manifested Persephone", 328, "Dream", ItemClassification.progression, 5),
    "Progressive Dream of Vulcan": ItemData("Progressive Dream of Vulcan", 329, "Dream", ItemClassification.progression, 5),
    "Progressive Dream of Lost Vulcan": ItemData("Progressive Dream of Lost Vulcan", 330, "Dream", ItemClassification.progression, 5),
    "Progressive Dream of The Red Right Hand": ItemData("Progressive Dream of The Red Right Hand", 331, "Dream", ItemClassification.progression, 5),
    "Progressive Dream of Telos": ItemData("Progressive Dream of Telos", 332, "Dream", ItemClassification.progression, 5),
    "Progressive Dream of Vitality": ItemData("Progressive Dream of Vitality", 340, "Dream", ItemClassification.progression, 5),
    "Progressive Dream of Flux Capacity": ItemData("Progressive Dream of Flux Capacity", 341, "Dream", ItemClassification.useful, 4),
    "Progressive Dream of Life Manifested": ItemData("Progressive Dream of Life Manifested", 342, "Dream", ItemClassification.progression, 3),
    "Progressive Dream of no Surrender": ItemData("Progressive Dream of no Surrender", 343, "Dream", ItemClassification.progression, 2),
    "Dream of the Memory Palace": ItemData("Dream of the Memory Palace", 344, "Dream", ItemClassification.useful, 1),
    "Progressive Dream of Streak Guardian": ItemData("Progressive Dream of Streak Guardian", 350, "Dream", ItemClassification.useful, 3),
    "Progressive Dream of Ghost Rounds": ItemData("Progressive Dream of Ghost Rounds", 351, "Dream", ItemClassification.useful, 3),
    "Progressive Dream of Boon Momentum": ItemData("Progressive Dream of Boon Momentum", 352, "Dream", ItemClassification.useful, 3),
    "Progressive Dream of Unyielding Fury": ItemData("Progressive Dream of Unyielding Fury", 353, "Dream", ItemClassification.useful, 3),
    "Progressive Dream of Last Breath Aegis": ItemData("Progressive Dream of Last Breath Aegis", 354, "Dream", ItemClassification.useful, 3),
    "Progressive Dream of Ultimate Sovereignty": ItemData("Progressive Dream of Ultimate Sovereignty", 355, "Dream", ItemClassification.useful, 3),
    "Progressive Dream of The Perfectionist": ItemData("Progressive Dream of The Perfectionist", 356, "Dream", ItemClassification.useful, 3),
    "Progressive Memory of Destructive Force": ItemData("Progressive Memory of Destructive Force", 360, "Memory", ItemClassification.progression, 3),
    "Progressive Memory of Sharpened Blade": ItemData("Progressive Memory of Sharpened Blade", 361, "Memory", ItemClassification.progression, 3),
    "Progressive Memory of Precise Focus": ItemData("Progressive Memory of Precise Focus", 362, "Memory", ItemClassification.progression, 3),
    "Progressive Memory of Equal in Death": ItemData("Progressive Memory of Equal in Death", 363, "Memory", ItemClassification.progression, 3),
    "Progressive Memory of Defensive Charm": ItemData("Progressive Memory of Defensive Charm", 364, "Memory", ItemClassification.progression, 3),
    "Memory of Bounty of Void Echoes": ItemData("Memory of Bounty of Void Echoes", 365, "Memory", ItemClassification.useful, 0),
    "Progressive Memory of Stubborn Outrage": ItemData("Progressive Memory of Stubborn Outrage", 369, "Memory", ItemClassification.useful, 3),
    "Progressive Memory of Echoing Harvest": ItemData("Progressive Memory of Echoing Harvest", 370, "Memory", ItemClassification.useful, 3),
    "Progressive Memory of Shard Magnet": ItemData("Progressive Memory of Shard Magnet", 371, "Memory", ItemClassification.useful, 3),
    "Progressive Mind over Matter Memory": ItemData("Progressive Mind over Matter Memory", 372, "Memory", ItemClassification.useful, 3),
    "Memory of Echoing Perfection": ItemData("Memory of Echoing Perfection", 373, "Memory", ItemClassification.useful, 1),
    "Memory of Echoing Combos": ItemData("Memory of Echoing Combos", 374, "Memory", ItemClassification.useful, 1),
    "Memory of Sturdy Boots": ItemData("Memory of Sturdy Boots", 375, "Memory", ItemClassification.useful, 1),
    "Memory of Profane Onslaught": ItemData("Memory of Profane Onslaught", 376, "Memory", ItemClassification.useful, 1),
    "Memory of Cursed Blades": ItemData("Memory of Cursed Blades", 377, "Memory", ItemClassification.useful, 1),
    "Memory of Demonic Precision": ItemData("Memory of Demonic Precision", 378, "Memory", ItemClassification.useful, 1),
    "Memory of Cursing Headshots": ItemData("Memory of Cursing Headshots", 379, "Memory", ItemClassification.useful, 1),
    "Memory of Cursed Chaos": ItemData("Memory of Cursed Chaos", 380, "Memory", ItemClassification.useful, 1),
    "Memory of Perfect Curse Explosions": ItemData("Memory of Perfect Curse Explosions", 381, "Memory", ItemClassification.useful, 1),
    "Memory of Damning Charge": ItemData("Memory of Damning Charge", 382, "Memory", ItemClassification.useful, 1),
    "Memory of Damning Marksmanship": ItemData("Memory of Damning Marksmanship", 383, "Memory", ItemClassification.useful, 1),
    "Memory of Damning Cuts": ItemData("Memory of Damning Cuts", 384, "Memory", ItemClassification.useful, 1),
    "Memory of Freezing Cannonry": ItemData("Memory of Freezing Cannonry", 385, "Memory", ItemClassification.useful, 1),
    "Memory of Freezing Blades": ItemData("Memory of Freezing Blades", 386, "Memory", ItemClassification.useful, 1),
    "Memory of Biting Precision": ItemData("Memory of Biting Precision", 387, "Memory", ItemClassification.useful, 1),
    "Memory of Chilling Headshots": ItemData("Memory of Chilling Headshots", 388, "Memory", ItemClassification.useful, 1),
    "Memory of Slow Chaos": ItemData("Memory of Slow Chaos", 389, "Memory", ItemClassification.useful, 1),
    "Memory of Perfect Slow Explosions": ItemData("Memory of Perfect Slow Explosions", 390, "Memory", ItemClassification.useful, 1),
    "Memory of Unfair Advantage": ItemData("Memory of Unfair Advantage", 391, "Memory", ItemClassification.useful, 1),
    "Memory of Fish in a Barrel": ItemData("Memory of Fish in a Barrel", 392, "Memory", ItemClassification.useful, 1),
    "Memory of Cold-Seeking Blades": ItemData("Memory of Cold-Seeking Blades", 393, "Memory", ItemClassification.useful, 1),
    "Memory of Heavy Consquences": ItemData("Memory of Heavy Consquences", 394, "Memory", ItemClassification.useful, 1),
    "Memory of Crimson Cuts": ItemData("Memory of Crimson Cuts", 395, "Memory", ItemClassification.useful, 1),
    "Memory of Bloody Precision": ItemData("Memory of Bloody Precision", 396, "Memory", ItemClassification.useful, 1),
    "Memory of Bleeding Headshots": ItemData("Memory of Bleeding Headshots", 397, "Memory", ItemClassification.useful, 1),
    "Memory of Bleeding Chaos": ItemData("Memory of Bleeding Chaos", 398, "Memory", ItemClassification.useful, 1),
    "Memory of Perfect Blood Explosions": ItemData("Memory of Perfect Blood Explosions", 399, "Memory", ItemClassification.useful, 1),
    "Memory of Sanguine Blade": ItemData("Memory of Sanguine Blade", 400, "Memory", ItemClassification.useful, 1),
    "Memory of Easy Pickings": ItemData("Memory of Easy Pickings", 401, "Memory", ItemClassification.useful, 1),
    "Memory of Hunting Knives": ItemData("Memory of Hunting Knives", 402, "Memory", ItemClassification.useful, 1),
    "Progressive Memory of Ultimate Urgency": ItemData("Progressive Memory of Ultimate Urgency", 403, "Memory", ItemClassification.filler, 3),
    "Memory of Ultimate Perfection": ItemData("Memory of Ultimate Perfection", 404, "Memory", ItemClassification.filler, 1),
    "Memory of Ultimate Combos": ItemData("Memory of Ultimate Combos", 405, "Memory", ItemClassification.filler, 1),
    "Memory of Ultimate Contract": ItemData("Memory of Ultimate Contract", 406, "Memory", ItemClassification.filler, 1),
    "Progressive Memory of Positive Mindset": ItemData("Progressive Memory of Positive Mindset", 407, "Memory", ItemClassification.filler, 3),
    "Memory of Revitalizing Perfection": ItemData("Memory of Revitalizing Perfection", 408, "Memory", ItemClassification.filler, 1),
    "Memory of Revitalizing Combos": ItemData("Memory of Revitalizing Combos", 409, "Memory", ItemClassification.filler, 1),
    "Progressive Memory of Volatile Demons": ItemData("Progressive Memory of Volatile Demons", 410, "Memory", ItemClassification.filler, 3),
    "Memory of Bloodthirst": ItemData("Memory of Bloodthirst", 411, "Memory", ItemClassification.useful, 1),
    "Memory of Paz Crystallization": ItemData("Memory of Paz Crystallization", 412, "Memory", ItemClassification.useful, 1),
    "Progressive Memory of Strategic Withdrawal": ItemData("Progressive Memory of Strategic Withdrawal", 413, "Memory", ItemClassification.useful, 2),
    "Memory of Perfect Authority": ItemData("Memory of Perfect Authority", 414, "Memory", ItemClassification.filler, 1),
    "Memory of Ultimate Pots": ItemData("Memory of Ultimate Pots", 415, "Memory", ItemClassification.useful, 1),
    "Memory of Double Trouble": ItemData("Memory of Double Trouble", 416, "Memory", ItemClassification.useful, 1),
    "Memory of Rush of Ultimate": ItemData("Memory of Rush of Ultimate", 417, "Memory", ItemClassification.filler, 1),
    "Memory of being Light-Footed": ItemData("Memory of being Light-Footed", 418, "Memory", ItemClassification.filler, 1),
    "Memory of Crystal Attunement": ItemData("Memory of Crystal Attunement", 419, "Memory", ItemClassification.filler, 1),
    "Memory of Hellcrow": ItemData("Memory of Hellcrow", 420, "Memory", ItemClassification.progression, 1),
    "Memory of The Hounds": ItemData("Memory of The Hounds", 421, "Memory", ItemClassification.progression, 1),
    "Memory of The Lost Hounds": ItemData("Memory of The Lost Hounds", 422, "Memory", ItemClassification.progression, 1),
    "Memory of Persephone": ItemData("Memory of Persephone", 423, "Memory", ItemClassification.progression, 1),
    "Memory of Lost Persephone": ItemData("Memory of Lost Persephone", 424, "Memory", ItemClassification.progression, 1),
    "Memory of Manifested Persephone": ItemData("Memory of Manifested Persephone", 425, "Memory", ItemClassification.progression, 1),
    "Memory of Vulcan": ItemData("Memory of Vulcan", 426, "Memory", ItemClassification.progression, 1),
    "Memory of Lost Vulcan": ItemData("Memory of Lost Vulcan", 427, "Memory", ItemClassification.progression, 1),
    "Memory of The Red Right Hand": ItemData("Memory of The Red Right Hand", 428, "Memory", ItemClassification.progression, 1),
    "Memory of Telos": ItemData("Memory of Telos", 429, "Memory", ItemClassification.progression, 1),
    "Progressive Memory of Seraphs": ItemData("Progressive Memory of Seraphs", 430, "Memory", ItemClassification.useful, 2),
    "Progressive Memory of Behemoths": ItemData("Progressive Memory of Behemoths", 431, "Memory", ItemClassification.useful, 2),
    "Progressive Memory of Stalkers": ItemData("Progressive Memory of Stalkers", 432, "Memory", ItemClassification.useful, 2),
    "Progressive Memory of Hierophants": ItemData("Progressive Memory of Hierophants", 433, "Memory", ItemClassification.useful, 2),
    "Progressive Memory of Eyeless": ItemData("Progressive Memory of Eyeless", 434, "Memory", ItemClassification.useful, 2),
    "Progressive Memory of Elites": ItemData("Progressive Memory of Elites", 435, "Memory", ItemClassification.useful, 2),
    "Outfit of the Unknown": ItemData("Outfit of the Unknown", 500, "Outfit", ItemClassification.progression, 1),
    "Outfit of the Leviathan": ItemData("Outfit of the Leviathan", 501, "Outfit", ItemClassification.progression, 1),
    "Outfit of the Dark Devotee": ItemData("Outfit of the Dark Devotee", 502, "Outfit", ItemClassification.progression, 1),
    "Outfit of the Morning Star": ItemData("Outfit of the Morning Star", 503, "Outfit", ItemClassification.progression, 1),
    "Outfit of the Angel Eyes": ItemData("Outfit of the Angel Eyes", 504, "Outfit", ItemClassification.progression, 1),
    "Outfit of the Obsidian": ItemData("Outfit of the Obsidian", 505, "Outfit", ItemClassification.progression, 1),
    "Outfit of the Amethyst": ItemData("Outfit of the Amethyst", 506, "Outfit", ItemClassification.progression, 1),
    "Outfit of the Chromatica": ItemData("Outfit of the Chromatica", 507, "Outfit", ItemClassification.progression, 1),
    "This is the End": ItemData("This is the End", 510, "Song", ItemClassification.progression, 1),
    "Stygia (Song)": ItemData("Stygia (Song)", 511, "Song", ItemClassification.progression, 1),
    "Burial At Night": ItemData("Burial At Night", 512, "Song", ItemClassification.progression, 1),
    "This Devastation": ItemData("This Devastation", 513, "Song", ItemClassification.progression, 1),
    "Poetry of Cinder": ItemData("Poetry of Cinder", 514, "Song", ItemClassification.progression, 1),
    "Dissolution": ItemData("Dissolution", 515, "Song", ItemClassification.progression, 1),
    "Acheron (Song)": ItemData("Acheron (Song)", 517, "Song", ItemClassification.progression, 1),
    "Silent No More": ItemData("Silent No More", 518, "Song", ItemClassification.progression, 1),
    "Blood and Law": ItemData("Blood and Law", 519, "Song", ItemClassification.progression, 1),
    "Infernal Invocation I: Hopes and Fears": ItemData("Infernal Invocation I: Hopes and Fears", 520, "Song", ItemClassification.progression, 1),
    "Infernal Invocation II: Defiance": ItemData("Infernal Invocation II: Defiance", 521, "Song", ItemClassification.progression, 1),
    "Infernal Invocation III: Dreaming in Distortion": ItemData("Infernal Invocation III: Dreaming in Distortion", 522, "Song", ItemClassification.progression, 1),
    "No Tomorrow": ItemData("No Tomorrow", 523, "Song", ItemClassification.progression, 1),
    "Departure to Destruction": ItemData("Departure to Destruction", 524, "Song", ItemClassification.progression, 1),
    "Hand Cannon": ItemData("Hand Cannon", 525, "Song", ItemClassification.progression, 1),
    "Burn in Hell": ItemData("Burn in Hell", 526, "Song", ItemClassification.progression, 1),
    "Murder Machine Inc": ItemData("Murder Machine Inc", 527, "Song", ItemClassification.progression, 1),
    "Endless": ItemData("Endless", 528, "Song", ItemClassification.progression, 1),
    "Mine Control": ItemData("Mine Control", 529, "Song", ItemClassification.progression, 1),
    "Sacrifice": ItemData("Sacrifice", 530, "Song", ItemClassification.progression, 1),
    "Erebus Reaction": ItemData("Erebus Reaction", 531, "Song", ItemClassification.progression, 1),
    "Bleeding Out": ItemData("Bleeding Out", 532, "Song", ItemClassification.progression, 1),
    "Leviathan (Song)": ItemData("Leviathan (Song)", 533, "Song", ItemClassification.progression, 1),
    "Dream of the Beast": ItemData("Dream of the Beast", 534, "Song", ItemClassification.progression, 1),
    "Swallow the Fire": ItemData("Swallow the Fire", 535, "Song", ItemClassification.progression, 1),
    "Mouth of Hell": ItemData("Mouth of Hell", 536, "Song", ItemClassification.progression, 1),
    "Goodbye, Morning Star": ItemData("Goodbye, Morning Star", 537, "Song", ItemClassification.progression, 1),
    "Down With the Sickness": ItemData("Down With the Sickness", 538, "Song", ItemClassification.progression, 1),
    "Uprising": ItemData("Uprising", 539, "Song", ItemClassification.progression, 1),
    "Misery Business": ItemData("Misery Business", 540, "Song", ItemClassification.progression, 1),
    "Tsunami (Original Mix)": ItemData("Tsunami (Original Mix)", 541, "Song", ItemClassification.progression, 1),
    "Runaway (U&I)": ItemData("Runaway (U&I)", 542, "Song", ItemClassification.progression, 1),
    "Feel Good Inc.": ItemData("Feel Good Inc.", 543, "Song", ItemClassification.progression, 1),
    "I Love It feat. Charli XCX": ItemData("I Love It feat. Charli XCX", 544, "Song", ItemClassification.progression, 1),
    "Personal Jesus": ItemData("Personal Jesus", 545, "Song", ItemClassification.progression, 1),
    "Next Multiplier": ItemData("Next Multiplier", 550, "Combat", ItemClassification.filler, 0),
    "Max Multiplier": ItemData("Max Multiplier", 551, "Combat", ItemClassification.filler, 0),
    "Always on Beat": ItemData("Always on Beat", 552, "Combat", ItemClassification.filler, 0),
    "Compliment": ItemData("Compliment", 553, "Combat", ItemClassification.filler, 0),
    "Encouragement": ItemData("Encouragement", 554, "Combat", ItemClassification.filler, 0),
    "Failure": ItemData("Failure", 555, "Combat", ItemClassification.filler, 0),
    "Reset Multiplier": ItemData("Reset Multiplier", 560, "Combat", ItemClassification.trap, 0),
    "Double Time": ItemData("Double Time", 561, "Combat", ItemClassification.trap, 0),
    "Half Time": ItemData("Half Time", 562, "Combat", ItemClassification.trap, 0),
    "Invisible Weapons": ItemData("Invisible Weapons", 563, "Combat", ItemClassification.trap, 0),
    "Weapon Trickery": ItemData("Weapon Trickery", 564, "Combat", ItemClassification.trap, 0),
    "Trigger Ultimate": ItemData("Trigger Ultimate", 565, "Combat", ItemClassification.trap, 0),
    "Death": ItemData("Death", 566, "Combat", ItemClassification.trap, 0),
    "Filler": ItemData("Filler", 666, "Global", ItemClassification.filler, 0),
    "Out of Logic": ItemData("Out of Logic", 999, "Global", ItemClassification.progression, 0),
}

item_name_to_id: dict[str, int] = {name: data.id for name, data in item_table.items()}

item_name_groups: dict[str, set[str]] = {}
for item_name, item_data in item_table.items():
    item_name_groups.setdefault(item_data.group, set()).add(item_name)
