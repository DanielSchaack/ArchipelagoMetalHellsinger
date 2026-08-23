from typing import TYPE_CHECKING

from BaseClasses import Region
from worlds.metal_hellsinger.options import WinCondition

if TYPE_CHECKING:
    from . import MetalHellsingerWorld

def create_and_connect_regions(world: "MetalHellsingerWorld") -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: "MetalHellsingerWorld") -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    regions: list[Region] = []

    if world.options.win_condition == WinCondition.option_hells_completion or world.options.win_condition == WinCondition.option_sheol_completion:
        global_region = Region("Global", world.player, world.multiworld)

        tutorial = Region("Tutorial", world.player, world.multiworld)
        voke_arena1 = Region("Voke Arena1", world.player, world.multiworld)
        voke_arena2 = Region("Voke Arena2", world.player, world.multiworld)
        voke_arena3 = Region("Voke Arena3", world.player, world.multiworld)
        voke_arena4 = Region("Voke Arena4", world.player, world.multiworld)
        voke_boss = Region("Voke Boss", world.player, world.multiworld)
        stygia_arena1 = Region("Stygia Arena1", world.player, world.multiworld)
        stygia_arena2 = Region("Stygia Arena2", world.player, world.multiworld)
        stygia_arena3 = Region("Stygia Arena3", world.player, world.multiworld)
        stygia_arena4 = Region("Stygia Arena4", world.player, world.multiworld)
        stygia_boss = Region("Stygia Boss", world.player, world.multiworld)
        yhelm_arena1 = Region("Yhelm Arena1", world.player, world.multiworld)
        yhelm_arena2 = Region("Yhelm Arena2", world.player, world.multiworld)
        yhelm_arena3 = Region("Yhelm Arena3", world.player, world.multiworld)
        yhelm_arena4 = Region("Yhelm Arena4", world.player, world.multiworld)
        yhelm_boss = Region("Yhelm Boss", world.player, world.multiworld)
        incaustis_arena1 = Region("Incaustis Arena1", world.player, world.multiworld)
        incaustis_arena2 = Region("Incaustis Arena2", world.player, world.multiworld)
        incaustis_arena3 = Region("Incaustis Arena3", world.player, world.multiworld)
        incaustis_arena4 = Region("Incaustis Arena4", world.player, world.multiworld)
        incaustis_boss = Region("Incaustis Boss", world.player, world.multiworld)
        gehenna_arena1 = Region("Gehenna Arena1", world.player, world.multiworld)
        gehenna_arena2 = Region("Gehenna Arena2", world.player, world.multiworld)
        gehenna_arena3 = Region("Gehenna Arena3", world.player, world.multiworld)
        gehenna_arena4 = Region("Gehenna Arena4", world.player, world.multiworld)
        gehenna_boss = Region("Gehenna Boss", world.player, world.multiworld)
        nihil_arena1 = Region("Nihil Arena1", world.player, world.multiworld)
        nihil_arena2 = Region("Nihil Arena2", world.player, world.multiworld)
        nihil_arena3 = Region("Nihil Arena3", world.player, world.multiworld)
        nihil_arena4 = Region("Nihil Arena4", world.player, world.multiworld)
        nihil_boss = Region("Nihil Boss", world.player, world.multiworld)
        acheron_arena1 = Region("Acheron Arena1", world.player, world.multiworld)
        acheron_arena2 = Region("Acheron Arena2", world.player, world.multiworld)
        acheron_arena3 = Region("Acheron Arena3", world.player, world.multiworld)
        acheron_arena4 = Region("Acheron Arena4", world.player, world.multiworld)
        acheron_boss = Region("Acheron Boss", world.player, world.multiworld)
        sheol_arena1 = Region("Sheol Arena1", world.player, world.multiworld)
        sheol_arena2 = Region("Sheol Arena2", world.player, world.multiworld)
        sheol_arena3 = Region("Sheol Arena3", world.player, world.multiworld)
        sheol_arena4 = Region("Sheol Arena4", world.player, world.multiworld)
        sheol_boss = Region("Sheol Boss", world.player, world.multiworld)
        killingwithrhythm_torment1 = Region("KillingWithRhythm Torment1", world.player, world.multiworld)
        killingwithrhythm_torment2 = Region("KillingWithRhythm Torment2", world.player, world.multiworld)
        killingwithrhythm_torment3 = Region("KillingWithRhythm Torment3", world.player, world.multiworld)
        giantslayer_torment1 = Region("Giantslayer Torment1", world.player, world.multiworld)
        giantslayer_torment2 = Region("Giantslayer Torment2", world.player, world.multiworld)
        giantslayer_torment3 = Region("Giantslayer Torment3", world.player, world.multiworld)
        ultimatemastery_torment1 = Region("UltimateMastery Torment1", world.player, world.multiworld)
        ultimatemastery_torment2 = Region("UltimateMastery Torment2", world.player, world.multiworld)
        ultimatemastery_torment3 = Region("UltimateMastery Torment3", world.player, world.multiworld)
        slaughtermastery_torment1 = Region("SlaughterMastery Torment1", world.player, world.multiworld)
        slaughtermastery_torment2 = Region("SlaughterMastery Torment2", world.player, world.multiworld)
        slaughtermastery_torment3 = Region("SlaughterMastery Torment3", world.player, world.multiworld)
        relicthief_torment1 = Region("RelicThief Torment1", world.player, world.multiworld)
        relicthief_torment2 = Region("RelicThief Torment2", world.player, world.multiworld)
        relicthief_torment3 = Region("RelicThief Torment3", world.player, world.multiworld)
        weapontrickery_torment1 = Region("WeaponTrickery Torment1", world.player, world.multiworld)
        weapontrickery_torment2 = Region("WeaponTrickery Torment2", world.player, world.multiworld)
        weapontrickery_torment3 = Region("WeaponTrickery Torment3", world.player, world.multiworld)
        deathsedge_torment1 = Region("DeathsEdge Torment1", world.player, world.multiworld)
        deathsedge_torment2 = Region("DeathsEdge Torment2", world.player, world.multiworld)
        deathsedge_torment3 = Region("DeathsEdge Torment3", world.player, world.multiworld)
        weapon_basegame = Region("Weapon Basegame", world.player, world.multiworld)
        weapon_extra = Region("Weapon Extra", world.player, world.multiworld)
        weapon_dreamofthebeast = Region("Weapon DreamOfTheBeast", world.player, world.multiworld)
        weapon_purgatory = Region("Weapon Purgatory", world.player, world.multiworld)
        outfit_basegame = Region("Outfit Basegame", world.player, world.multiworld)
        outfit_dreamofthebeast = Region("Outfit DreamOfTheBeast", world.player, world.multiworld)
        outfit_purgatory = Region("Outfit Purgatory", world.player, world.multiworld)
        song_basegame = Region("Song Basegame", world.player, world.multiworld)
        song_dreamofthebeast = Region("Song DreamOfTheBeast", world.player, world.multiworld)
        song_purgatory = Region("Song Purgatory", world.player, world.multiworld)
        song_dusksoundtrack = Region("Song DuskSoundtrack", world.player, world.multiworld)
        song_essentialhits = Region("Song EssentialHits", world.player, world.multiworld)

        regions += [
            global_region,
            tutorial,
            voke_arena1,
            voke_arena2,
            voke_arena3,
            voke_arena4,
            voke_boss,
            stygia_arena1,
            stygia_arena2,
            stygia_arena3,
            stygia_arena4,
            stygia_boss,
            yhelm_arena1,
            yhelm_arena2,
            yhelm_arena3,
            yhelm_arena4,
            yhelm_boss,
            incaustis_arena1,
            incaustis_arena2,
            incaustis_arena3,
            incaustis_arena4,
            incaustis_boss,
            gehenna_arena1,
            gehenna_arena2,
            gehenna_arena3,
            gehenna_arena4,
            gehenna_boss,
            nihil_arena1,
            nihil_arena2,
            nihil_arena3,
            nihil_arena4,
            nihil_boss,
            acheron_arena1,
            acheron_arena2,
            acheron_arena3,
            acheron_arena4,
            acheron_boss,
            sheol_arena1,
            sheol_arena2,
            sheol_arena3,
            sheol_arena4,
            sheol_boss,
        ]

        if world.options.include_section_clears_with_weapons_checks:
            regions.append(weapon_basegame)
            if world.options.include_dream_of_the_beast_weapon:
                regions.append(weapon_dreamofthebeast)
            if world.options.include_purgatory_weapon:
                regions.append(weapon_purgatory)
            if world.options.include_additional_weapon_variants:
                regions.append(weapon_extra)

        if world.options.include_section_clears_with_outfits_checks:
            regions.append(outfit_basegame)
            if world.options.include_dream_of_the_beast_outfits:
                regions.append(outfit_dreamofthebeast)
            if world.options.include_purgatory_outfits:
                regions.append(outfit_purgatory)

        if world.options.include_section_clears_with_songs_checks:
            regions.append(song_basegame)
            if world.options.include_dream_of_the_beast_songs:
                regions.append(song_dreamofthebeast)
            if world.options.include_purgatory_songs:
                regions.append(song_purgatory)
            if world.options.include_dusk_soundtrack_songs:
                regions.append(song_dusksoundtrack)
            if world.options.include_essential_hits_soundtrack_songs:
                regions.append(song_essentialhits)

        if world.options.randomized_torments_enabled:
            regions += [
                killingwithrhythm_torment1,
                killingwithrhythm_torment2,
                killingwithrhythm_torment3,
                giantslayer_torment1,
                giantslayer_torment2,
                giantslayer_torment3,
                ultimatemastery_torment1,
                ultimatemastery_torment2,
                ultimatemastery_torment3,
                slaughtermastery_torment1,
                slaughtermastery_torment2,
                slaughtermastery_torment3,
                relicthief_torment1,
                relicthief_torment2,
                relicthief_torment3,
                weapontrickery_torment1,
                weapontrickery_torment2,
                weapontrickery_torment3,
                deathsedge_torment1,
                deathsedge_torment2,
                deathsedge_torment3,
            ]

    world.multiworld.regions += regions


def connect_regions(world: "MetalHellsingerWorld") -> None:
    global_region = world.get_region("Global")

    tutorial = world.get_region("Tutorial")
    global_region.connect(tutorial, "Global to Tutorial")


    voke_arena1 = world.get_region("Voke Arena1")
    voke_arena2 = world.get_region("Voke Arena2")
    voke_arena3 = world.get_region("Voke Arena3")
    voke_arena4 = world.get_region("Voke Arena4")
    voke_boss = world.get_region("Voke Boss")

    global_region.connect(voke_arena1, "Global to Voke Arena1")
    voke_arena1.connect(voke_arena2, "Voke Arena1 to Voke Arena2")
    voke_arena2.connect(voke_arena3, "Voke Arena2 to Voke Arena3")
    voke_arena3.connect(voke_arena4, "Voke Arena3 to Voke Arena4")
    voke_arena4.connect(voke_boss, "Voke Arena4 to Voke Boss")

    stygia_arena1 = world.get_region("Stygia Arena1")
    stygia_arena2 = world.get_region("Stygia Arena2")
    stygia_arena3 = world.get_region("Stygia Arena3")
    stygia_arena4 = world.get_region("Stygia Arena4")
    stygia_boss = world.get_region("Stygia Boss")

    global_region.connect(stygia_arena1, "Global to Stygia Arena1")
    stygia_arena1.connect(stygia_arena2, "Stygia Arena1 to Stygia Arena2")
    stygia_arena2.connect(stygia_arena3, "Stygia Arena2 to Stygia Arena3")
    stygia_arena3.connect(stygia_arena4, "Stygia Arena3 to Stygia Arena4")
    stygia_arena4.connect(stygia_boss, "Stygia Arena4 to Stygia Boss")


    yhelm_arena1 = world.get_region("Yhelm Arena1")
    yhelm_arena2 = world.get_region("Yhelm Arena2")
    yhelm_arena3 = world.get_region("Yhelm Arena3")
    yhelm_arena4 = world.get_region("Yhelm Arena4")
    yhelm_boss = world.get_region("Yhelm Boss")

    global_region.connect(yhelm_arena1, "Global to Yhelm Arena1")
    yhelm_arena1.connect(yhelm_arena2, "Yhelm Arena1 to Yhelm Arena2")
    yhelm_arena2.connect(yhelm_arena3, "Yhelm Arena2 to Yhelm Arena3")
    yhelm_arena3.connect(yhelm_arena4, "Yhelm Arena3 to Yhelm Arena4")
    yhelm_arena4.connect(yhelm_boss, "Yhelm Arena4 to Yhelm Boss")


    incaustis_arena1 = world.get_region("Incaustis Arena1")
    incaustis_arena2 = world.get_region("Incaustis Arena2")
    incaustis_arena3 = world.get_region("Incaustis Arena3")
    incaustis_arena4 = world.get_region("Incaustis Arena4")
    incaustis_boss = world.get_region("Incaustis Boss")

    global_region.connect(incaustis_arena1, "Global to Incaustis Arena1")
    incaustis_arena1.connect(incaustis_arena2, "Incaustis Arena1 to Incaustis Arena2")
    incaustis_arena2.connect(incaustis_arena3, "Incaustis Arena2 to Incaustis Arena3")
    incaustis_arena3.connect(incaustis_arena4, "Incaustis Arena3 to Incaustis Arena4")
    incaustis_arena4.connect(incaustis_boss, "Incaustis Arena4 to Incaustis Boss")


    gehenna_arena1 = world.get_region("Gehenna Arena1")
    gehenna_arena2 = world.get_region("Gehenna Arena2")
    gehenna_arena3 = world.get_region("Gehenna Arena3")
    gehenna_arena4 = world.get_region("Gehenna Arena4")
    gehenna_boss = world.get_region("Gehenna Boss")

    global_region.connect(gehenna_arena1, "Global to Gehenna Arena1")
    gehenna_arena1.connect(gehenna_arena2, "Gehenna Arena1 to Gehenna Arena2")
    gehenna_arena2.connect(gehenna_arena3, "Gehenna Arena2 to Gehenna Arena3")
    gehenna_arena3.connect(gehenna_arena4, "Gehenna Arena3 to Gehenna Arena4")
    gehenna_arena4.connect(gehenna_boss, "Gehenna Arena4 to Gehenna Boss")


    nihil_arena1 = world.get_region("Nihil Arena1")
    nihil_arena2 = world.get_region("Nihil Arena2")
    nihil_arena3 = world.get_region("Nihil Arena3")
    nihil_arena4 = world.get_region("Nihil Arena4")
    nihil_boss = world.get_region("Nihil Boss")

    global_region.connect(nihil_arena1, "Global to Nihil Arena1")
    nihil_arena1.connect(nihil_arena2, "Nihil Arena1 to Nihil Arena2")
    nihil_arena2.connect(nihil_arena3, "Nihil Arena2 to Nihil Arena3")
    nihil_arena3.connect(nihil_arena4, "Nihil Arena3 to Nihil Arena4")
    nihil_arena4.connect(nihil_boss, "Nihil Arena4 to Nihil Boss")


    acheron_arena1 = world.get_region("Acheron Arena1")
    acheron_arena2 = world.get_region("Acheron Arena2")
    acheron_arena3 = world.get_region("Acheron Arena3")
    acheron_arena4 = world.get_region("Acheron Arena4")
    acheron_boss = world.get_region("Acheron Boss")

    global_region.connect(acheron_arena1, "Global to Acheron Arena1")
    acheron_arena1.connect(acheron_arena2, "Acheron Arena1 to Acheron Arena2")
    acheron_arena2.connect(acheron_arena3, "Acheron Arena2 to Acheron Arena3")
    acheron_arena3.connect(acheron_arena4, "Acheron Arena3 to Acheron Arena4")
    acheron_arena4.connect(acheron_boss, "Acheron Arena4 to Acheron Boss")


    sheol_arena1 = world.get_region("Sheol Arena1")
    sheol_arena2 = world.get_region("Sheol Arena2")
    sheol_arena3 = world.get_region("Sheol Arena3")
    sheol_arena4 = world.get_region("Sheol Arena4")
    sheol_boss = world.get_region("Sheol Boss")

    global_region.connect(sheol_arena1, "Global to Sheol Arena1")
    sheol_arena1.connect(sheol_arena2, "Sheol Arena1 to Sheol Arena2")
    sheol_arena2.connect(sheol_arena3, "Sheol Arena2 to Sheol Arena3")
    sheol_arena3.connect(sheol_arena4, "Sheol Arena3 to Sheol Arena4")
    sheol_arena4.connect(sheol_boss, "Sheol Arena4 to Sheol Boss")


    if world.options.include_section_clears_with_weapons_checks:
        weapon_basegame = world.get_region("Weapon Basegame")
        global_region.connect(weapon_basegame, "Global to Weapon Basegame")

        if world.options.include_dream_of_the_beast_weapon:
            weapon_dreamofthebeast = world.get_region("Weapon DreamOfTheBeast")
            global_region.connect(weapon_dreamofthebeast, "Global to Weapon DreamOfTheBeast")

        if world.options.include_purgatory_weapon:
            weapon_purgatory = world.get_region("Weapon Purgatory")
            global_region.connect(weapon_purgatory, "Global to Weapon Purgatory")

        if world.options.include_additional_weapon_variants:
            weapon_extra = world.get_region("Weapon Extra")
            global_region.connect(weapon_extra, "Global to Weapon Extra")


    if world.options.include_section_clears_with_outfits_checks:
        outfit_basegame = world.get_region("Outfit Basegame")
        global_region.connect(outfit_basegame, "Global to Outfit Basegame")

        if world.options.include_dream_of_the_beast_outfits:
            outfit_dreamofthebeast = world.get_region("Outfit DreamOfTheBeast")
            global_region.connect(outfit_dreamofthebeast, "Global to Outfit DreamOfTheBeast")

        if world.options.include_purgatory_outfits:
            outfit_purgatory = world.get_region("Outfit Purgatory")
            global_region.connect(outfit_purgatory, "Global to Outfit Purgatory")


    if world.options.include_section_clears_with_songs_checks:
        song_basegame = world.get_region("Song Basegame")
        global_region.connect(song_basegame, "Global to Song Basegame")

        if world.options.include_dream_of_the_beast_songs:
            song_dreamofthebeast = world.get_region("Song DreamOfTheBeast")
            global_region.connect(song_dreamofthebeast, "Global to Song DreamOfTheBeast")

        if world.options.include_purgatory_songs:
            song_purgatory = world.get_region("Song Purgatory")
            global_region.connect(song_purgatory, "Global to Song Purgatory")

        if world.options.include_dusk_soundtrack_songs:
            song_dusksoundtrack = world.get_region("Song DuskSoundtrack")
            global_region.connect(song_dusksoundtrack, "Global to Song DuskSoundtrack")

        if world.options.include_essential_hits_soundtrack_songs:
            song_essentialhits = world.get_region("Song EssentialHits")
            global_region.connect(song_essentialhits, "Global to Song EssentialHits")


    if world.options.randomized_torments_enabled:
        killingwithrhythm_torment1 = world.get_region("KillingWithRhythm Torment1")
        killingwithrhythm_torment2 = world.get_region("KillingWithRhythm Torment2")
        killingwithrhythm_torment3 = world.get_region("KillingWithRhythm Torment3")
        global_region.connect(killingwithrhythm_torment1, "Global to KillingWithRhythm Torment1")
        global_region.connect(killingwithrhythm_torment2, "Global to KillingWithRhythm Torment2")
        global_region.connect(killingwithrhythm_torment3, "Global to KillingWithRhythm Torment3")

        giantslayer_torment1 = world.get_region("Giantslayer Torment1")
        giantslayer_torment2 = world.get_region("Giantslayer Torment2")
        giantslayer_torment3 = world.get_region("Giantslayer Torment3")
        global_region.connect(giantslayer_torment1, "Global to Giantslayer Torment1")
        global_region.connect(giantslayer_torment2, "Global to Giantslayer Torment2")
        global_region.connect(giantslayer_torment3, "Global to Giantslayer Torment3")

        ultimatemastery_torment1 = world.get_region("UltimateMastery Torment1")
        ultimatemastery_torment2 = world.get_region("UltimateMastery Torment2")
        ultimatemastery_torment3 = world.get_region("UltimateMastery Torment3")
        global_region.connect(ultimatemastery_torment1, "Global to UltimateMastery Torment1")
        global_region.connect(ultimatemastery_torment2, "Global to UltimateMastery Torment2")
        global_region.connect(ultimatemastery_torment3, "Global to UltimateMastery Torment3")

        slaughtermastery_torment1 = world.get_region("SlaughterMastery Torment1")
        slaughtermastery_torment2 = world.get_region("SlaughterMastery Torment2")
        slaughtermastery_torment3 = world.get_region("SlaughterMastery Torment3")
        global_region.connect(slaughtermastery_torment1, "Global to SlaughterMastery Torment1")
        global_region.connect(slaughtermastery_torment2, "Global to SlaughterMastery Torment2")
        global_region.connect(slaughtermastery_torment3, "Global to SlaughterMastery Torment3")

        relicthief_torment1 = world.get_region("RelicThief Torment1")
        relicthief_torment2 = world.get_region("RelicThief Torment2")
        relicthief_torment3 = world.get_region("RelicThief Torment3")
        global_region.connect(relicthief_torment1, "Global to RelicThief Torment1")
        global_region.connect(relicthief_torment2, "Global to RelicThief Torment2")
        global_region.connect(relicthief_torment3, "Global to RelicThief Torment3")

        weapontrickery_torment1 = world.get_region("WeaponTrickery Torment1")
        weapontrickery_torment2 = world.get_region("WeaponTrickery Torment2")
        weapontrickery_torment3 = world.get_region("WeaponTrickery Torment3")
        global_region.connect(weapontrickery_torment1, "Global to WeaponTrickery Torment1")
        global_region.connect(weapontrickery_torment2, "Global to WeaponTrickery Torment2")
        global_region.connect(weapontrickery_torment3, "Global to WeaponTrickery Torment3")

        deathsedge_torment1 = world.get_region("DeathsEdge Torment1")
        deathsedge_torment2 = world.get_region("DeathsEdge Torment2")
        deathsedge_torment3 = world.get_region("DeathsEdge Torment3")
        global_region.connect(deathsedge_torment1, "Global to DeathsEdge Torment1")
        global_region.connect(deathsedge_torment2, "Global to DeathsEdge Torment2")
        global_region.connect(deathsedge_torment3, "Global to DeathsEdge Torment3")
