from __future__ import annotations

from collections.abc import Collection
from typing import TYPE_CHECKING

from BaseClasses import Location
from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import CanReachRegion, Has, HasAll, HasAny, HasGroup
from worlds.metal_hellsinger.options import (
    ArchdevilEnemiesEnabled,
    DestructibleAsUnlocks,
    HellsUnlocksAsProgressive,
    IncludeAdditionalWeaponVariants,
    IncludeDreamOfTheBeastWeapon,
    IncludePurgatoryWeapon,
    MinimalDifficulty,
    RandomizedDashEnabled,
    RandomizedJumpEnabled,
    RandomizedReloadEnabled,
    RandomizedSlaughterEnabled,
    RandomizedSongsEnabled,
    RandomizedWeaponUltimatesEnabled,
    RegressiveDifficulty,
    RequireAspectForBossArena,
    RequireCoatOfArmsForSheol,
    RequiredCoatOfArmsForSheol,
    RequiredHellsCompletion,
    RequireNoTomorrowForSheol,
    RequireStageForTorments,
    RequireWeaponsForTorments,
    TormentUnlocksAsProgressive,
    WinCondition,
)

if TYPE_CHECKING:
    from . import MetalHellsingerWorld

OUT_OF_LOGIC = Has("Out of Logic")
IS_ADDITIONAL_WEAPONS = OptionFilter(IncludeAdditionalWeaponVariants, True)
IS_NOT_ADDITIONAL_WEAPONS = OptionFilter(IncludeAdditionalWeaponVariants, False)
IS_DREAM_WEAPON = OptionFilter(IncludeDreamOfTheBeastWeapon, True)
IS_PURGATORY_WEAPON = OptionFilter(IncludePurgatoryWeapon, True)

IS_WEAPON_ULTIMATE_SEPARATE = OptionFilter(RandomizedWeaponUltimatesEnabled, True)
IS_NOT_WEAPON_ULTIMATE_SEPARATE = OptionFilter(RandomizedWeaponUltimatesEnabled, False)

HAS_PAZ = Has("Paz")
HAS_TERMINUS = Has("Terminus")
HAS_PERSEPHONE = (IS_NOT_ADDITIONAL_WEAPONS & Has("Persephone")) | (IS_ADDITIONAL_WEAPONS & HasAny("Persephone", "Lost Persephone", "Manifested Persephone"))
HAS_THE_HOUNDS = (IS_NOT_ADDITIONAL_WEAPONS & Has("The Hounds")) | (IS_ADDITIONAL_WEAPONS & HasAny("The Hounds", "The Lost Hounds"))
HAS_VULCAN = (IS_NOT_ADDITIONAL_WEAPONS & Has("Vulcan")) | (IS_ADDITIONAL_WEAPONS & HasAny("Vulcan", "Lost Vulcan"))
HAS_HELLCROW = Has("Hellcrow")
HAS_THE_RED_RIGHT_HAND = IS_DREAM_WEAPON & Has("The Red Right Hand")
HAS_TELOS = IS_PURGATORY_WEAPON & Has("Telos")

HAS_PAZ_WITH_ULTIMATE = (IS_NOT_WEAPON_ULTIMATE_SEPARATE & HAS_PAZ) | (IS_WEAPON_ULTIMATE_SEPARATE & HasAll("Paz", "Paz Ultimate"))
HAS_TERMINUS_WITH_ULTIMATE = (IS_NOT_WEAPON_ULTIMATE_SEPARATE & HAS_TERMINUS) | (IS_WEAPON_ULTIMATE_SEPARATE & HasAll("Terminus", "Terminus Ultimate"))
HAS_PERSEPHONE_WITH_ULTIMATE = (IS_NOT_WEAPON_ULTIMATE_SEPARATE & HAS_PERSEPHONE) | (IS_WEAPON_ULTIMATE_SEPARATE & HAS_PERSEPHONE & Has("Persephone Ultimate"))
HAS_THE_HOUNDS_WITH_ULTIMATE = (IS_NOT_WEAPON_ULTIMATE_SEPARATE & HAS_THE_HOUNDS) | (IS_WEAPON_ULTIMATE_SEPARATE & HAS_THE_HOUNDS & Has("The Hounds Ultimate"))
HAS_VULCAN_WITH_ULTIMATE = (IS_NOT_WEAPON_ULTIMATE_SEPARATE & HAS_VULCAN) | (IS_WEAPON_ULTIMATE_SEPARATE & HAS_VULCAN & Has("Vulcan Ultimate"))
HAS_HELLCROW_WITH_ULTIMATE = (IS_NOT_WEAPON_ULTIMATE_SEPARATE & HAS_HELLCROW) | (IS_WEAPON_ULTIMATE_SEPARATE & HAS_HELLCROW & Has("Hellcrow Ultimate"))
HAS_THE_RED_RIGHT_HAND_WITH_ULTIMATE = (IS_NOT_WEAPON_ULTIMATE_SEPARATE & HAS_THE_RED_RIGHT_HAND) | (IS_WEAPON_ULTIMATE_SEPARATE & HAS_THE_RED_RIGHT_HAND & Has("The Red Right Hand Ultimate"))
HAS_TELOS_WITH_ULTIMATE = (IS_NOT_WEAPON_ULTIMATE_SEPARATE & HAS_TELOS) | (IS_WEAPON_ULTIMATE_SEPARATE & HAS_TELOS & Has("Telos Ultimate"))

HAS_RANGED_WEAPON_WITH_ULTIMATE = HAS_PERSEPHONE_WITH_ULTIMATE | HAS_THE_HOUNDS_WITH_ULTIMATE | HAS_VULCAN_WITH_ULTIMATE | HAS_HELLCROW_WITH_ULTIMATE | HAS_THE_RED_RIGHT_HAND_WITH_ULTIMATE | HAS_TELOS_WITH_ULTIMATE

IS_PROGRESSIVE_HELLS = OptionFilter(HellsUnlocksAsProgressive, True)
IS_NOT_PROGRESSIVE_HELLS = OptionFilter(HellsUnlocksAsProgressive, False)

REQUIRE_ASPECT_FOR_BOSS = OptionFilter(RequireAspectForBossArena, True)
REQUIRE_NO_ASPECT_FOR_BOSS = OptionFilter(RequireAspectForBossArena, False)

HAS_TUTORIAL = Has("Hells") & Has("Tutorial")
HAS_VOKE = Has("Hells") & (Has("Voke", options=[IS_NOT_PROGRESSIVE_HELLS]) | Has("Progressive Hells", count=1, options=[IS_PROGRESSIVE_HELLS]))
HAS_VOKE_ASPECT = REQUIRE_NO_ASPECT_FOR_BOSS | (REQUIRE_ASPECT_FOR_BOSS & Has("Aspect of Anger"))
HAS_STYGIA = Has("Hells") & (Has("Stygia", options=[IS_NOT_PROGRESSIVE_HELLS]) | Has("Progressive Hells", count=2, options=[IS_PROGRESSIVE_HELLS]))
HAS_STYGIA_ASPECT = REQUIRE_NO_ASPECT_FOR_BOSS | (REQUIRE_ASPECT_FOR_BOSS & Has("Aspect of the Charged"))
HAS_YHELM = Has("Hells") & (Has("Yhelm", options=[IS_NOT_PROGRESSIVE_HELLS]) | Has("Progressive Hells", count=3, options=[IS_PROGRESSIVE_HELLS]))
HAS_YHELM_ASPECT = REQUIRE_NO_ASPECT_FOR_BOSS | (REQUIRE_ASPECT_FOR_BOSS & Has("Aspect of the Fortress"))
HAS_INCAUSTIS = Has("Hells") & (Has("Incaustis", options=[IS_NOT_PROGRESSIVE_HELLS]) | Has("Progressive Hells", count=4, options=[IS_PROGRESSIVE_HELLS]))
HAS_INCAUSTIS_ASPECT = REQUIRE_NO_ASPECT_FOR_BOSS | (REQUIRE_ASPECT_FOR_BOSS & Has("Aspect of Infernal Fury"))
HAS_GEHENNA = Has("Hells") & (Has("Gehenna", options=[IS_NOT_PROGRESSIVE_HELLS]) | Has("Progressive Hells", count=5, options=[IS_PROGRESSIVE_HELLS]))
HAS_GEHENNA_ASPECT = REQUIRE_NO_ASPECT_FOR_BOSS | (REQUIRE_ASPECT_FOR_BOSS & Has("Aspect of the Hellstorm"))
HAS_NIHIL = Has("Hells") & (Has("Nihil", options=[IS_NOT_PROGRESSIVE_HELLS]) | Has("Progressive Hells", count=6, options=[IS_PROGRESSIVE_HELLS]))
HAS_NIHIL_ASPECT = REQUIRE_NO_ASPECT_FOR_BOSS | (REQUIRE_ASPECT_FOR_BOSS & Has("Aspect of the Doppelganger"))
HAS_ACHERON = Has("Hells") & (Has("Acheron", options=[IS_NOT_PROGRESSIVE_HELLS]) | Has("Progressive Hells", count=7, options=[IS_PROGRESSIVE_HELLS]))
HAS_ACHERON_ASPECT = REQUIRE_NO_ASPECT_FOR_BOSS | (REQUIRE_ASPECT_FOR_BOSS & Has("Aspect of the Wheel"))
HAS_SHEOL = Has("Hells") & (Has("Sheol", options=[IS_NOT_PROGRESSIVE_HELLS]) | Has("Progressive Hells", count=8, options=[IS_PROGRESSIVE_HELLS]))


RANDOMIZED_SONGS = OptionFilter(RandomizedSongsEnabled, True)
NO_RANDOMIZED_SONGS = OptionFilter(RandomizedSongsEnabled, False)

REQUIRE_NO_TOMORROW = OptionFilter(RequireNoTomorrowForSheol, True)
NOT_REQUIRE_NO_TOMORROW = OptionFilter(RequireNoTomorrowForSheol, False)
HAS_NO_TOMORROW = NO_RANDOMIZED_SONGS | (RANDOMIZED_SONGS & (NOT_REQUIRE_NO_TOMORROW | (REQUIRE_NO_TOMORROW & Has("No Tomorrow"))))

REQUIRE_COAT_OF_ARMS_FOR_SHEOL = OptionFilter(RequireCoatOfArmsForSheol, True)
REQUIRE_NO_COAT_OF_ARMS_FOR_SHEOL = OptionFilter(RequireCoatOfArmsForSheol, False)
HAS_COAT_OF_ARMS_FOR_SHEOL = REQUIRE_NO_COAT_OF_ARMS_FOR_SHEOL | (REQUIRE_COAT_OF_ARMS_FOR_SHEOL & Has("Coat of Arms", count=FromOption(RequiredCoatOfArmsForSheol)))

HAS_SHEOL_EXTRA_CONDITIONS = Has("Hells") & HAS_COAT_OF_ARMS_FOR_SHEOL & HAS_NO_TOMORROW

HAS_ANY_HELL = HAS_VOKE | HAS_STYGIA | HAS_YHELM | HAS_INCAUSTIS | HAS_GEHENNA | HAS_NIHIL | HAS_ACHERON | (HAS_SHEOL & HAS_SHEOL_EXTRA_CONDITIONS)
CAN_REACH_ANY_BOSS = CanReachRegion("Voke Boss") | CanReachRegion("Stygia Boss") | CanReachRegion("Yhelm Boss") | CanReachRegion("Incaustis Boss") | CanReachRegion("Gehenna Boss") | CanReachRegion("Nihil Boss") | CanReachRegion("Acheron Boss") | CanReachRegion("Sheol Boss")

HAS_CLOSE_RANGE_WEAPON = HAS_PERSEPHONE | HAS_THE_RED_RIGHT_HAND | HAS_HELLCROW
HAS_LONG_RANGE_WEAPON = HAS_THE_HOUNDS | HAS_VULCAN | HAS_TELOS
HAS_RELOADABLE_WEAPON = HAS_PERSEPHONE | HAS_THE_HOUNDS | HAS_VULCAN | HAS_THE_RED_RIGHT_HAND | HAS_TELOS


IS_PROGRESSIVE_JUMP = OptionFilter(RandomizedJumpEnabled, True)
IS_NOT_PROGRESSIVE_JUMP = OptionFilter(RandomizedJumpEnabled, False)
HAS_JUMP = IS_NOT_PROGRESSIVE_JUMP | (IS_PROGRESSIVE_JUMP & Has("Progressive Jump"))
HAS_DOUBLE_JUMP = IS_NOT_PROGRESSIVE_JUMP | (IS_PROGRESSIVE_JUMP & Has("Progressive Jump", count=2))
HAS_INFINITE_JUMP = IS_PROGRESSIVE_JUMP & Has("Progressive Jump", count=3)

IS_PROGRESSIVE_DASH = OptionFilter(RandomizedDashEnabled, True)
IS_NOT_PROGRESSIVE_DASH = OptionFilter(RandomizedDashEnabled, False)
HAS_DASH = IS_NOT_PROGRESSIVE_DASH | (IS_PROGRESSIVE_DASH & Has("Progressive Dash", count=1))
HAS_SOAR = IS_NOT_PROGRESSIVE_DASH | (IS_PROGRESSIVE_DASH & Has("Progressive Dash", count=2))

IS_PROGRESSIVE_RELOAD = OptionFilter(RandomizedReloadEnabled, True)
IS_NOT_PROGRESSIVE_RELOAD = OptionFilter(RandomizedReloadEnabled, False)
HAS_QUICK_RELOAD = IS_NOT_PROGRESSIVE_RELOAD | (IS_PROGRESSIVE_RELOAD & Has("Progressive Reload", count=1))
HAS_MANUAL_RELOAD = IS_NOT_PROGRESSIVE_RELOAD | (IS_PROGRESSIVE_RELOAD & Has("Progressive Reload", count=2))

IS_RANDOM_SLAUGHTER = OptionFilter(RandomizedSlaughterEnabled, True)
IS_NOT_RANDOM_SLAUGHTER = OptionFilter(RandomizedSlaughterEnabled, False)
HAS_SLAUGHTER = IS_NOT_RANDOM_SLAUGHTER | (IS_RANDOM_SLAUGHTER & Has("Slaughter"))

IS_DESTRUCTIBLE_RANDOM = OptionFilter(DestructibleAsUnlocks, True)
IS_NOT_DESTRUCTIBLE_RANDOM = OptionFilter(DestructibleAsUnlocks, False)
HAS_DESTRUCTIBLE_AMMOSTASHES = IS_NOT_DESTRUCTIBLE_RANDOM | (IS_DESTRUCTIBLE_RANDOM & Has("Destructible Ammostashes"))
HAS_DESTRUCTIBLE_HEALTH_CRYSTALS = IS_NOT_DESTRUCTIBLE_RANDOM | (IS_DESTRUCTIBLE_RANDOM & Has("Destructible Health Crystals"))
HAS_DESTRUCTIBLE_CHAOS_CRYSTALS  = IS_NOT_DESTRUCTIBLE_RANDOM | (IS_DESTRUCTIBLE_RANDOM & Has("Destructible Chaos Crystals"))

HAS_ANY_HEAL = HAS_SLAUGHTER | HAS_DESTRUCTIBLE_HEALTH_CRYSTALS
HAS_ALL_HEAL = HAS_SLAUGHTER & HAS_DESTRUCTIBLE_HEALTH_CRYSTALS

HAS_ALL_DESCTRUCTIBLES = HAS_DESTRUCTIBLE_AMMOSTASHES & HAS_DESTRUCTIBLE_HEALTH_CRYSTALS & HAS_DESTRUCTIBLE_CHAOS_CRYSTALS
HAS_ANY_DESTRUCTIBLES = HAS_DESTRUCTIBLE_AMMOSTASHES | HAS_DESTRUCTIBLE_HEALTH_CRYSTALS | HAS_DESTRUCTIBLE_CHAOS_CRYSTALS

HAS_REGRESSIVE_DIFFICULTY = OptionFilter(RegressiveDifficulty, True)
HAS_NOT_REGRESSIVE_DIFFICULTY = OptionFilter(RegressiveDifficulty, False)

HAS_ARCHDEVIL_SPAWNS = OptionFilter(ArchdevilEnemiesEnabled, True)
HAS_ARCHDEVIL = ((HAS_NOT_REGRESSIVE_DIFFICULTY & Has("Archdevil")) | (HAS_REGRESSIVE_DIFFICULTY & Has("Regressive Difficulty", count=1))) & OptionFilter(MinimalDifficulty, 3, "le")
HAS_BEAST = ((HAS_NOT_REGRESSIVE_DIFFICULTY & Has("Beast")) | (HAS_REGRESSIVE_DIFFICULTY & Has("Regressive Difficulty", count=2))) & OptionFilter(MinimalDifficulty, 2, "le")
HAS_GOAT = ((HAS_NOT_REGRESSIVE_DIFFICULTY & Has("Goat")) | (HAS_REGRESSIVE_DIFFICULTY & Has("Regressive Difficulty", count=3))) & OptionFilter(MinimalDifficulty, 1, "le")
HAS_LAMB = ((HAS_NOT_REGRESSIVE_DIFFICULTY & Has("Lamb")) | (HAS_REGRESSIVE_DIFFICULTY & Has("Regressive Difficulty", count=4))) & OptionFilter(MinimalDifficulty, 0, "le")
HAS_NON_ARCHDEVIL = HAS_LAMB | HAS_GOAT | HAS_BEAST

HAS_BASE_MOVEMENT = HAS_JUMP | HAS_DASH
HAS_ADVANCED_MOVEMENT = (HAS_JUMP & HAS_DASH) | HAS_SOAR | HAS_DOUBLE_JUMP

HAS_GENERIC_ARENA_2_ACCESS = (HAS_BASE_MOVEMENT & HAS_ANY_HEAL) | OUT_OF_LOGIC
HAS_GENERIC_ARENA_3_ACCESS = (((HAS_ALL_HEAL & (HAS_ARCHDEVIL | HAS_ARCHDEVIL_SPAWNS) & HAS_ADVANCED_MOVEMENT) | (HAS_BEAST & HAS_ADVANCED_MOVEMENT) | (HAS_GOAT | HAS_LAMB)) & (HAS_RANGED_WEAPON_WITH_ULTIMATE | HAS_QUICK_RELOAD)) | OUT_OF_LOGIC
HAS_GENERIC_ARENA_4_ACCESS = (((HAS_ALL_HEAL & (HAS_ARCHDEVIL | HAS_ARCHDEVIL_SPAWNS) & HAS_ADVANCED_MOVEMENT) | (HAS_BEAST & HAS_ADVANCED_MOVEMENT) | (HAS_GOAT | HAS_LAMB)) & (HAS_RANGED_WEAPON_WITH_ULTIMATE | HAS_QUICK_RELOAD)) | OUT_OF_LOGIC
HAS_GENERIC_BOSS_ACCESS = (HAS_ALL_HEAL & HAS_ADVANCED_MOVEMENT & HAS_RANGED_WEAPON_WITH_ULTIMATE & HAS_QUICK_RELOAD) | OUT_OF_LOGIC

IS_PROGRESSIVE_TORMENT = OptionFilter(TormentUnlocksAsProgressive, True)
IS_NOT_PROGRESSIVE_TORMENT = OptionFilter(TormentUnlocksAsProgressive, False)

REQUIRES_TORMENT_WEAPONS = OptionFilter(RequireWeaponsForTorments, True)
REQUIRES_NO_TORMENT_WEAPONS = OptionFilter(RequireWeaponsForTorments, False)

REQUIRE_STAGE_OF_HELL = OptionFilter(RequireStageForTorments, True)
REQUIRE_NO_STAGE_OF_HELL = OptionFilter(RequireStageForTorments, False)

HAS_KWR_1_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_PAZ & HAS_PERSEPHONE)
HAS_KWR_2_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_PAZ & HAS_TERMINUS & HAS_THE_HOUNDS)
HAS_KWR_3_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_PAZ & HAS_TERMINUS & HAS_HELLCROW)
HAS_KWR_1_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_VOKE)
HAS_KWR_2_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_YHELM)
HAS_KWR_3_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_GEHENNA)
HAS_KWR_1 = Has("Hells") & HAS_KWR_1_HELLS & HAS_KWR_1_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Killing with Rhythm", count=1)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Killing with Rhythm: 1")))
HAS_KWR_2 = Has("Hells") & HAS_KWR_2_HELLS & HAS_KWR_2_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Killing with Rhythm", count=2)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Killing with Rhythm: 2")))
HAS_KWR_3 = Has("Hells") & HAS_KWR_3_HELLS & HAS_KWR_3_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Killing with Rhythm", count=3)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Killing with Rhythm: 3")))

HAS_WT_1_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS & HAS_PERSEPHONE)
HAS_WT_2_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS & HAS_PERSEPHONE & HAS_THE_HOUNDS & HAS_VULCAN)
HAS_WT_3_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS & HAS_PERSEPHONE & HAS_THE_HOUNDS & HAS_VULCAN & HAS_HELLCROW)
HAS_WT_1_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_VOKE)
HAS_WT_2_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_YHELM)
HAS_WT_3_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_GEHENNA)
HAS_WT_1 = Has("Hells") & HAS_WT_1_HELLS & HAS_WT_1_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Weapon Trickery", count=1)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Weapon Trickery: 1")))
HAS_WT_2 = Has("Hells") & HAS_WT_2_HELLS & HAS_WT_2_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Weapon Trickery", count=2)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Weapon Trickery: 2")))
HAS_WT_3 = Has("Hells") & HAS_WT_3_HELLS & HAS_WT_3_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Weapon Trickery", count=3)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Weapon Trickery: 3")))

HAS_RT_1_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS & HAS_PERSEPHONE)
HAS_RT_2_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS & HAS_PERSEPHONE & HAS_THE_HOUNDS)
HAS_RT_3_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS & HAS_VULCAN & HAS_HELLCROW)
HAS_RT_1_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_VOKE)
HAS_RT_2_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_STYGIA)
HAS_RT_3_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_INCAUSTIS)
HAS_RT_1 = Has("Hells") & HAS_RT_1_HELLS & HAS_RT_1_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Relic Thief", count=1)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Relic Thief: 1")))
HAS_RT_2 = Has("Hells") & HAS_RT_2_HELLS & HAS_RT_2_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Relic Thief", count=2)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Relic Thief: 2")))
HAS_RT_3 = Has("Hells") & HAS_RT_3_HELLS & HAS_RT_3_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Relic Thief", count=3)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Relic Thief: 3")))

HAS_GS_1_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS & HAS_PERSEPHONE & HAS_THE_HOUNDS)
HAS_GS_2_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS & HAS_THE_HOUNDS & HAS_HELLCROW)
HAS_GS_3_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS & HAS_PERSEPHONE & HAS_THE_HOUNDS)
HAS_GS_1_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_STYGIA)
HAS_GS_2_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_INCAUSTIS)
HAS_GS_3_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_NIHIL)
HAS_GS_1 = Has("Hells") & HAS_GS_1_HELLS & HAS_GS_1_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Giantslayer", count=1)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Giantslayer: 1")))
HAS_GS_2 = Has("Hells") & HAS_GS_2_HELLS & HAS_GS_2_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Giantslayer", count=2)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Giantslayer: 2")))
HAS_GS_3 = Has("Hells") & HAS_GS_3_HELLS & HAS_GS_3_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Giantslayer", count=3)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Giantslayer: 3")))

HAS_DE_1_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_PAZ & HAS_TERMINUS & HAS_PERSEPHONE & HAS_THE_HOUNDS)
HAS_DE_2_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_PAZ & HAS_TERMINUS & HAS_PERSEPHONE & HAS_THE_HOUNDS)
HAS_DE_3_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_PAZ & HAS_TERMINUS & HAS_VULCAN & HAS_HELLCROW)
HAS_DE_1_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_STYGIA)
HAS_DE_2_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_GEHENNA)
HAS_DE_3_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_ACHERON)
HAS_DE_1 = Has("Hells") & HAS_DE_1_HELLS & HAS_DE_1_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Death's Edge", count=1)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Death's Edge: 1")))
HAS_DE_2 = Has("Hells") & HAS_DE_2_HELLS & HAS_DE_2_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Death's Edge", count=2)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Death's Edge: 2")))
HAS_DE_3 = Has("Hells") & HAS_DE_3_HELLS & HAS_DE_3_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Death's Edge", count=3)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Death's Edge: 3")))

HAS_UM_1_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS_WITH_ULTIMATE & HAS_PERSEPHONE_WITH_ULTIMATE)
HAS_UM_2_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS_WITH_ULTIMATE & HAS_PERSEPHONE_WITH_ULTIMATE & HAS_HELLCROW_WITH_ULTIMATE)
HAS_UM_3_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_TERMINUS_WITH_ULTIMATE & HAS_PERSEPHONE_WITH_ULTIMATE & HAS_THE_HOUNDS_WITH_ULTIMATE)
HAS_UM_1_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_YHELM)
HAS_UM_2_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_NIHIL)
HAS_UM_3_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_ACHERON)
HAS_UM_1 = Has("Hells") & HAS_UM_1_HELLS & HAS_UM_1_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Ultimate Mastery", count=1)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Ultimate Mastery: 1")))
HAS_UM_2 = Has("Hells") & HAS_UM_2_HELLS & HAS_UM_2_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Ultimate Mastery", count=2)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Ultimate Mastery: 2")))
HAS_UM_3 = Has("Hells") & HAS_UM_3_HELLS & HAS_UM_3_WEAPONS & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Ultimate Mastery", count=3)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Ultimate Mastery: 3")))

HAS_SM_1_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_PAZ & HAS_TERMINUS & HAS_THE_HOUNDS)
HAS_SM_2_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_PAZ & HAS_TERMINUS & HAS_THE_HOUNDS)
HAS_SM_3_WEAPONS = REQUIRES_NO_TORMENT_WEAPONS | (REQUIRES_TORMENT_WEAPONS & HAS_PAZ & HAS_TERMINUS & HAS_THE_HOUNDS)
HAS_SM_1_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_INCAUSTIS)
HAS_SM_2_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_NIHIL)
HAS_SM_3_HELLS = REQUIRE_NO_STAGE_OF_HELL | (REQUIRE_STAGE_OF_HELL & HAS_ACHERON)
HAS_SM_1 = Has("Hells") & HAS_SM_1_HELLS & HAS_SM_1_WEAPONS & HAS_SLAUGHTER & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Slaughter Mastery", count=1)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Slaughter Mastery: 1")))
HAS_SM_2 = Has("Hells") & HAS_SM_2_HELLS & HAS_SM_2_WEAPONS & HAS_SLAUGHTER & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Slaughter Mastery", count=2)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Slaughter Mastery: 2")))
HAS_SM_3 = Has("Hells") & HAS_SM_3_HELLS & HAS_SM_3_WEAPONS & HAS_SLAUGHTER & ((IS_PROGRESSIVE_TORMENT & Has("Progressive Slaughter Mastery", count=3)) | (IS_NOT_PROGRESSIVE_TORMENT & Has("Slaughter Mastery: 3")))

HAS_CHAOS_ACCESS = (
    CanReachRegion("Voke Arena2")
    | CanReachRegion("Stygia Arena2")
    | CanReachRegion("Yhelm Arena2")
    | CanReachRegion("Incaustis Arena1")
    | CanReachRegion("Gehenna Arena1")
    | CanReachRegion("Nihil Arena1")
    | CanReachRegion("Acheron Arena1")
    | CanReachRegion("Sheol Arena1")
)


CAN_REACH_MARIONETTE = (
    CanReachRegion("Tutorial")
    | CanReachRegion("Voke Arena1")
    | CanReachRegion("Stygia Arena1")
    | CanReachRegion("Yhelm Arena1")
    | CanReachRegion("Incaustis Arena1")
    | CanReachRegion("Gehenna Arena1")
    | CanReachRegion("Nihil Arena1")
    | CanReachRegion("Acheron Arena1")
    | CanReachRegion("Sheol Arena1")
)

CAN_REACH_CAMBION = (
    CanReachRegion("Voke Arena1")
    | CanReachRegion("Stygia Arena1")
    | CanReachRegion("Yhelm Arena1")
    | CanReachRegion("Incaustis Arena1")
    | CanReachRegion("Gehenna Arena1")
    | CanReachRegion("Nihil Arena1")
    | CanReachRegion("Acheron Arena1")
    | CanReachRegion("Sheol Arena1")
)

CAN_REACH_BEHEMOTH = (
    HAS_NON_ARCHDEVIL
    & (
        CanReachRegion("Voke Arena3")
        | CanReachRegion("Stygia Arena2")
        | CanReachRegion("Yhelm Arena3")
        | CanReachRegion("Incaustis Arena1")
        | CanReachRegion("Gehenna Arena1")
        | CanReachRegion("Nihil Arena3")
        | CanReachRegion("Acheron Arena2")
        | CanReachRegion("Sheol Arena2")
    )
) | (
    (HAS_ARCHDEVIL | HAS_ARCHDEVIL_SPAWNS)
    & (
        CanReachRegion("Voke Arena3")
        | CanReachRegion("Stygia Arena2")
        | CanReachRegion("Yhelm Arena1")
        | CanReachRegion("Incaustis Arena2")
        | CanReachRegion("Gehenna Arena2")
        | CanReachRegion("Nihil Arena2")
        | CanReachRegion("Acheron Arena2")
        | CanReachRegion("Sheol Arena2")
    )
)

CAN_REACH_STALKER = (HAS_BASE_MOVEMENT | OUT_OF_LOGIC) & (
    (
        HAS_NON_ARCHDEVIL
        & (
            CanReachRegion("Stygia Arena3")
            | CanReachRegion("Yhelm Arena2")
            | CanReachRegion("Incaustis Arena1")
            | CanReachRegion("Gehenna Arena2")
            | CanReachRegion("Nihil Arena2")
            | CanReachRegion("Acheron Arena2")
            | CanReachRegion("Sheol Arena2")
        )
    )
    | (
        (HAS_ARCHDEVIL | HAS_ARCHDEVIL_SPAWNS)
        & (
            CanReachRegion("Stygia Arena1")
            | CanReachRegion("Yhelm Arena2")
            | CanReachRegion("Incaustis Arena2")
            | CanReachRegion("Gehenna Arena2")
            | CanReachRegion("Nihil Arena2")
            | CanReachRegion("Acheron Arena2")
            | CanReachRegion("Sheol Arena2")
        )
    )
)

CAN_REACH_EYELESS = (
    HAS_NON_ARCHDEVIL
    & (
        CanReachRegion("Yhelm Arena2")
        | CanReachRegion("Incaustis Arena1")
        | CanReachRegion("Gehenna Arena1")
        | CanReachRegion("Nihil Arena2")
        | CanReachRegion("Acheron Arena1")
        | CanReachRegion("Sheol Arena1")
    )
) | (
    (HAS_ARCHDEVIL | HAS_ARCHDEVIL_SPAWNS)
    & (
        CanReachRegion("Voke Arena2")
        | CanReachRegion("Stygia Arena3")
        | CanReachRegion("Yhelm Arena1")
        | CanReachRegion("Incaustis Arena1")
        | CanReachRegion("Gehenna Arena1")
        | CanReachRegion("Nihil Arena2")
        | CanReachRegion("Acheron Arena2")
        | CanReachRegion("Sheol Arena1")
    )
)

CAN_REACH_HIEROPHANT = (
    HAS_NON_ARCHDEVIL
    & (
        CanReachRegion("Incaustis Arena2")
        | CanReachRegion("Gehenna Arena1")
        | CanReachRegion("Nihil Arena2")
        | CanReachRegion("Acheron Arena1")
        | CanReachRegion("Sheol Arena1")
    )
) | (
    (HAS_ARCHDEVIL | HAS_ARCHDEVIL_SPAWNS)
    & (
        CanReachRegion("Voke Arena3")
        | CanReachRegion("Yhelm Arena2")
        | CanReachRegion("Incaustis Arena2")
        | CanReachRegion("Gehenna Arena1")
        | CanReachRegion("Nihil Arena2")
        | CanReachRegion("Acheron Arena2")
        | CanReachRegion("Sheol Arena1")
    )
)

CAN_REACH_LESSER_SERAPH = (HAS_LONG_RANGE_WEAPON | OUT_OF_LOGIC) & (
    (
        HAS_NON_ARCHDEVIL
        & (
            CanReachRegion("Gehenna Arena2")
            | CanReachRegion("Nihil Arena2")
            | CanReachRegion("Acheron Arena1")
            | CanReachRegion("Sheol Arena2")
        )
    )
    | (
        (HAS_ARCHDEVIL | HAS_ARCHDEVIL_SPAWNS)
        & (
            CanReachRegion("Voke Arena1")
            | CanReachRegion("Yhelm Arena1")
            | CanReachRegion("Incaustis Arena1")
            | CanReachRegion("Gehenna Arena2")
            | CanReachRegion("Nihil Arena1")
            | CanReachRegion("Acheron Arena2")
            | CanReachRegion("Sheol Arena2")
        )
    )
)

CAN_REACH_SHIELD_CAMBION = (HAS_BASE_MOVEMENT | OUT_OF_LOGIC) & (
    (
        HAS_NON_ARCHDEVIL
        & (
            CanReachRegion("Yhelm Arena1")
            | CanReachRegion("Incaustis Arena2")
            | CanReachRegion("Gehenna Arena2")
            | CanReachRegion("Nihil Arena2")
            | CanReachRegion("Acheron Arena2")
            | CanReachRegion("Sheol Arena1")
        )
    )
    | (
        (HAS_ARCHDEVIL | HAS_ARCHDEVIL_SPAWNS)
        & (
            CanReachRegion("Stygia Arena1")
            | CanReachRegion("Yhelm Arena1")
            | CanReachRegion("Incaustis Arena2")
            | CanReachRegion("Gehenna Arena2")
            | CanReachRegion("Nihil Arena2")
            | CanReachRegion("Acheron Arena2")
            | CanReachRegion("Sheol Arena1")
        )
    )
)


CAN_REACH_SIEGE_BEHEMOTH = ((HAS_BASE_MOVEMENT & HAS_ANY_HEAL) | OUT_OF_LOGIC) & (
    (
        HAS_NON_ARCHDEVIL
        & (
            CanReachRegion("Incaustis Arena4")
            | CanReachRegion("Gehenna Arena1")
            | CanReachRegion("Nihil Arena2")
            | CanReachRegion("Acheron Arena3")
            | CanReachRegion("Sheol Arena1")
        )
    )
    | (
        (HAS_ARCHDEVIL | HAS_ARCHDEVIL_SPAWNS)
        & (
            CanReachRegion("Voke Arena3")
            | CanReachRegion("Yhelm Arena3")
            | CanReachRegion("Incaustis Arena2")
            | CanReachRegion("Gehenna Arena1")
            | CanReachRegion("Nihil Arena1")
            | CanReachRegion("Acheron Arena2")
            | CanReachRegion("Sheol Arena1")
        )
    )
)

CAN_REACH_VOID_STALKER = ((HAS_BASE_MOVEMENT & HAS_ANY_HEAL) | OUT_OF_LOGIC) & (
    (
        HAS_NON_ARCHDEVIL
        & (CanReachRegion("Nihil Arena3") | CanReachRegion("Acheron Arena2") | CanReachRegion("Sheol Arena2"))
    )
    | (
        (HAS_ARCHDEVIL | HAS_ARCHDEVIL_SPAWNS)
        & (
            CanReachRegion("Stygia Arena3")
            | CanReachRegion("Yhelm Arena2")
            | CanReachRegion("Gehenna Arena2")
            | CanReachRegion("Nihil Arena3")
            | CanReachRegion("Acheron Arena1")
            | CanReachRegion("Sheol Arena2")
        )
    )
)


CAN_REACH_ANNIHILATOR_SERAPH = (
    ((HAS_BASE_MOVEMENT & HAS_ANY_HEAL & HAS_LONG_RANGE_WEAPON) | OUT_OF_LOGIC)
    & (HAS_ARCHDEVIL | HAS_ARCHDEVIL_SPAWNS)
    & (
        CanReachRegion("Voke Arena4")
        | CanReachRegion("Stygia Arena2")
        | CanReachRegion("Incaustis Arena2")
        | CanReachRegion("Gehenna Arena3")
        | CanReachRegion("Nihil Arena2")
        | CanReachRegion("Acheron Arena1")
        | CanReachRegion("Sheol Arena2")
    )
)


JUMP_OUT_OF_LOGIC = HAS_BASE_MOVEMENT & (Has("Vulcan") | Has("The Lost Hounds")) & OUT_OF_LOGIC

def set_all_rules(world: MetalHellsingerWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: MetalHellsingerWorld) -> None:
    global_to_tutorial = world.get_entrance("Global to Tutorial")
    world.set_rule(global_to_tutorial, HAS_TUTORIAL & HAS_BASE_MOVEMENT)

    global_to_voke_arena1 = world.get_entrance("Global to Voke Arena1")
    world.set_rule(global_to_voke_arena1, HAS_VOKE)
    voke_arena1_to_voke_arena2 = world.get_entrance("Voke Arena1 to Voke Arena2")
    world.set_rule(voke_arena1_to_voke_arena2, HAS_GENERIC_ARENA_2_ACCESS & (HAS_DOUBLE_JUMP | HAS_DASH | JUMP_OUT_OF_LOGIC))
    voke_arena2_to_voke_arena3 = world.get_entrance("Voke Arena2 to Voke Arena3")
    world.set_rule(voke_arena2_to_voke_arena3, HAS_GENERIC_ARENA_3_ACCESS & (HAS_DOUBLE_JUMP | HAS_DASH | JUMP_OUT_OF_LOGIC))
    voke_arena3_to_voke_arena4 = world.get_entrance("Voke Arena3 to Voke Arena4")
    world.set_rule(voke_arena3_to_voke_arena4, HAS_GENERIC_ARENA_4_ACCESS & (HAS_DOUBLE_JUMP | HAS_DASH | JUMP_OUT_OF_LOGIC))
    voke_arena4_to_voke_boss = world.get_entrance("Voke Arena4 to Voke Boss")
    world.set_rule(voke_arena4_to_voke_boss, HAS_GENERIC_BOSS_ACCESS & HAS_VOKE_ASPECT)

    global_to_stygia_arena1 = world.get_entrance("Global to Stygia Arena1")
    world.set_rule(global_to_stygia_arena1, HAS_STYGIA)
    stygia_arena1_to_stygia_arena2 = world.get_entrance("Stygia Arena1 to Stygia Arena2")
    world.set_rule(stygia_arena1_to_stygia_arena2, HAS_GENERIC_ARENA_2_ACCESS)
    stygia_arena2_to_stygia_arena3 = world.get_entrance("Stygia Arena2 to Stygia Arena3")
    world.set_rule(stygia_arena2_to_stygia_arena3, HAS_GENERIC_ARENA_3_ACCESS)
    stygia_arena3_to_stygia_arena4 = world.get_entrance("Stygia Arena3 to Stygia Arena4")
    world.set_rule(stygia_arena3_to_stygia_arena4, HAS_GENERIC_ARENA_4_ACCESS)
    stygia_arena4_to_stygia_boss = world.get_entrance("Stygia Arena4 to Stygia Boss")
    world.set_rule(stygia_arena4_to_stygia_boss, HAS_GENERIC_BOSS_ACCESS & (HAS_STYGIA_ASPECT | (HAS_PAZ & OUT_OF_LOGIC)))

    global_to_yhelm_arena1 = world.get_entrance("Global to Yhelm Arena1")
    world.set_rule(global_to_yhelm_arena1, HAS_YHELM)
    yhelm_arena1_to_yhelm_arena2 = world.get_entrance("Yhelm Arena1 to Yhelm Arena2")
    world.set_rule(yhelm_arena1_to_yhelm_arena2, HAS_GENERIC_ARENA_2_ACCESS & (HAS_BASE_MOVEMENT))
    yhelm_arena2_to_yhelm_arena3 = world.get_entrance("Yhelm Arena2 to Yhelm Arena3")
    world.set_rule(yhelm_arena2_to_yhelm_arena3, HAS_GENERIC_ARENA_3_ACCESS & (HAS_BASE_MOVEMENT))
    yhelm_arena3_to_yhelm_arena4 = world.get_entrance("Yhelm Arena3 to Yhelm Arena4")
    world.set_rule(yhelm_arena3_to_yhelm_arena4, HAS_GENERIC_ARENA_4_ACCESS & (HAS_BASE_MOVEMENT))
    yhelm_arena4_to_yhelm_boss = world.get_entrance("Yhelm Arena4 to Yhelm Boss")
    world.set_rule(yhelm_arena4_to_yhelm_boss, HAS_GENERIC_BOSS_ACCESS & HAS_YHELM_ASPECT)

    global_to_incaustis_arena1 = world.get_entrance("Global to Incaustis Arena1")
    world.set_rule(global_to_incaustis_arena1, HAS_INCAUSTIS)
    incaustis_arena1_to_incaustis_arena2 = world.get_entrance("Incaustis Arena1 to Incaustis Arena2")
    world.set_rule(incaustis_arena1_to_incaustis_arena2, HAS_GENERIC_ARENA_2_ACCESS)
    incaustis_arena2_to_incaustis_arena3 = world.get_entrance("Incaustis Arena2 to Incaustis Arena3")
    world.set_rule(incaustis_arena2_to_incaustis_arena3, HAS_GENERIC_ARENA_3_ACCESS & (HAS_BASE_MOVEMENT))
    incaustis_arena3_to_incaustis_arena4 = world.get_entrance("Incaustis Arena3 to Incaustis Arena4")
    world.set_rule(incaustis_arena3_to_incaustis_arena4, HAS_GENERIC_ARENA_4_ACCESS & (HAS_BASE_MOVEMENT))
    incaustis_arena4_to_incaustis_boss = world.get_entrance("Incaustis Arena4 to Incaustis Boss")
    world.set_rule(incaustis_arena4_to_incaustis_boss, HAS_GENERIC_BOSS_ACCESS & HAS_INCAUSTIS_ASPECT)

    global_to_gehenna_arena1 = world.get_entrance("Global to Gehenna Arena1")
    world.set_rule(global_to_gehenna_arena1, HAS_GEHENNA)
    gehenna_arena1_to_gehenna_arena2 = world.get_entrance("Gehenna Arena1 to Gehenna Arena2")
    world.set_rule(gehenna_arena1_to_gehenna_arena2, HAS_GENERIC_ARENA_2_ACCESS & (HAS_BASE_MOVEMENT))
    gehenna_arena2_to_gehenna_arena3 = world.get_entrance("Gehenna Arena2 to Gehenna Arena3")
    world.set_rule(gehenna_arena2_to_gehenna_arena3, HAS_GENERIC_ARENA_3_ACCESS & (HAS_BASE_MOVEMENT))
    gehenna_arena3_to_gehenna_arena4 = world.get_entrance("Gehenna Arena3 to Gehenna Arena4")
    world.set_rule(gehenna_arena3_to_gehenna_arena4, HAS_GENERIC_ARENA_4_ACCESS & (HAS_BASE_MOVEMENT))
    gehenna_arena4_to_gehenna_boss = world.get_entrance("Gehenna Arena4 to Gehenna Boss")
    world.set_rule(gehenna_arena4_to_gehenna_boss, HAS_GENERIC_BOSS_ACCESS & HAS_GEHENNA_ASPECT)

    global_to_nihil_arena1 = world.get_entrance("Global to Nihil Arena1")
    world.set_rule(global_to_nihil_arena1, HAS_NIHIL)
    nihil_arena1_to_nihil_arena2 = world.get_entrance("Nihil Arena1 to Nihil Arena2")
    world.set_rule(nihil_arena1_to_nihil_arena2, HAS_GENERIC_ARENA_2_ACCESS)
    nihil_arena2_to_nihil_arena3 = world.get_entrance("Nihil Arena2 to Nihil Arena3")
    world.set_rule(nihil_arena2_to_nihil_arena3, HAS_GENERIC_ARENA_3_ACCESS & (HAS_BASE_MOVEMENT))
    nihil_arena3_to_nihil_arena4 = world.get_entrance("Nihil Arena3 to Nihil Arena4")
    world.set_rule(nihil_arena3_to_nihil_arena4, HAS_GENERIC_ARENA_4_ACCESS & (HAS_BASE_MOVEMENT))
    nihil_arena4_to_nihil_boss = world.get_entrance("Nihil Arena4 to Nihil Boss")
    world.set_rule(nihil_arena4_to_nihil_boss, HAS_GENERIC_BOSS_ACCESS & HAS_NIHIL_ASPECT)

    global_to_acheron_arena1 = world.get_entrance("Global to Acheron Arena1")
    world.set_rule(global_to_acheron_arena1, HAS_ACHERON)
    acheron_arena1_to_acheron_arena2 = world.get_entrance("Acheron Arena1 to Acheron Arena2")
    world.set_rule(acheron_arena1_to_acheron_arena2, HAS_GENERIC_ARENA_2_ACCESS)
    acheron_arena2_to_acheron_arena3 = world.get_entrance("Acheron Arena2 to Acheron Arena3")
    world.set_rule(acheron_arena2_to_acheron_arena3, HAS_GENERIC_ARENA_3_ACCESS)
    acheron_arena3_to_acheron_arena4 = world.get_entrance("Acheron Arena3 to Acheron Arena4")
    world.set_rule(acheron_arena3_to_acheron_arena4, HAS_GENERIC_ARENA_4_ACCESS)
    acheron_arena4_to_acheron_boss = world.get_entrance("Acheron Arena4 to Acheron Boss")
    world.set_rule(acheron_arena4_to_acheron_boss, HAS_GENERIC_BOSS_ACCESS & HAS_ACHERON_ASPECT)

    global_to_sheol_arena1 = world.get_entrance("Global to Sheol Arena1")
    world.set_rule(global_to_sheol_arena1, HAS_SHEOL & HAS_SHEOL_EXTRA_CONDITIONS)
    sheol_arena1_to_sheol_arena2 = world.get_entrance("Sheol Arena1 to Sheol Arena2")
    world.set_rule(sheol_arena1_to_sheol_arena2, HAS_GENERIC_ARENA_2_ACCESS)
    sheol_arena2_to_sheol_arena3 = world.get_entrance("Sheol Arena2 to Sheol Arena3")
    world.set_rule(sheol_arena2_to_sheol_arena3, HAS_GENERIC_ARENA_3_ACCESS)
    sheol_arena3_to_sheol_arena4 = world.get_entrance("Sheol Arena3 to Sheol Arena4")
    world.set_rule(sheol_arena3_to_sheol_arena4, HAS_GENERIC_ARENA_4_ACCESS)
    sheol_arena4_to_sheol_boss = world.get_entrance("Sheol Arena4 to Sheol Boss")
    world.set_rule(sheol_arena4_to_sheol_boss, HAS_GENERIC_BOSS_ACCESS & HAS_LONG_RANGE_WEAPON & HAS_CLOSE_RANGE_WEAPON)


    if world.options.include_section_clears_with_weapons_checks:
        global_to_weapon_basegame = world.get_entrance("Global to Weapon Basegame")
        world.set_rule(global_to_weapon_basegame, CAN_REACH_ANY_BOSS)

        if world.options.include_dream_of_the_beast_weapon:
            global_to_weapon_dreamofthebeast = world.get_entrance("Global to Weapon DreamOfTheBeast")
            world.set_rule(global_to_weapon_dreamofthebeast, CAN_REACH_ANY_BOSS)

        if world.options.include_purgatory_weapon:
            global_to_weapon_purgatory = world.get_entrance("Global to Weapon Purgatory")
            world.set_rule(global_to_weapon_purgatory, CAN_REACH_ANY_BOSS)

        if world.options.include_additional_weapon_variants:
            global_to_weapon_extra = world.get_entrance("Global to Weapon Extra")
            world.set_rule(global_to_weapon_extra, CAN_REACH_ANY_BOSS)


    if world.options.include_section_clears_with_outfits_checks:
        global_to_outfit_basegame = world.get_entrance("Global to Outfit Basegame")
        world.set_rule(global_to_outfit_basegame, CAN_REACH_ANY_BOSS)

        if world.options.include_dream_of_the_beast_outfits:
            global_to_outfit_dreamofthebeast = world.get_entrance("Global to Outfit DreamOfTheBeast")
            world.set_rule(global_to_outfit_dreamofthebeast, CAN_REACH_ANY_BOSS)

        if world.options.include_purgatory_outfits:
            global_to_outfit_purgatory = world.get_entrance("Global to Outfit Purgatory")
            world.set_rule(global_to_outfit_purgatory, CAN_REACH_ANY_BOSS)


    if world.options.include_section_clears_with_songs_checks:
        global_to_song_basegame = world.get_entrance("Global to Song Basegame")
        world.set_rule(global_to_song_basegame, CAN_REACH_ANY_BOSS)

        if world.options.include_dream_of_the_beast_songs:
            global_to_song_dreamofthebeast = world.get_entrance("Global to Song DreamOfTheBeast")
            world.set_rule(global_to_song_dreamofthebeast, CAN_REACH_ANY_BOSS)

        if world.options.include_purgatory_songs:
            global_to_song_purgatory = world.get_entrance("Global to Song Purgatory")
            world.set_rule(global_to_song_purgatory, CAN_REACH_ANY_BOSS)

        if world.options.include_dusk_soundtrack_songs:
            global_to_song_dusksoundtrack = world.get_entrance("Global to Song DuskSoundtrack")
            world.set_rule(global_to_song_dusksoundtrack, CAN_REACH_ANY_BOSS)

        if world.options.include_essential_hits_soundtrack_songs:
            global_to_song_essentialhits = world.get_entrance("Global to Song EssentialHits")
            world.set_rule(global_to_song_essentialhits, CAN_REACH_ANY_BOSS)


    if world.options.randomized_torments_enabled:
        global_to_killingwithrhythm_torment1 = world.get_entrance("Global to KillingWithRhythm Torment1")
        global_to_killingwithrhythm_torment2 = world.get_entrance("Global to KillingWithRhythm Torment2")
        global_to_killingwithrhythm_torment3 = world.get_entrance("Global to KillingWithRhythm Torment3")
        world.set_rule(global_to_killingwithrhythm_torment1, HAS_KWR_1)
        world.set_rule(global_to_killingwithrhythm_torment2, HAS_KWR_2)
        world.set_rule(global_to_killingwithrhythm_torment3, HAS_KWR_3)

        global_to_giantslayer_torment1 = world.get_entrance("Global to Giantslayer Torment1")
        global_to_giantslayer_torment2 = world.get_entrance("Global to Giantslayer Torment2")
        global_to_giantslayer_torment3 = world.get_entrance("Global to Giantslayer Torment3")
        world.set_rule(global_to_giantslayer_torment1, HAS_GS_1)
        world.set_rule(global_to_giantslayer_torment2, HAS_GS_2)
        world.set_rule(global_to_giantslayer_torment3, HAS_GS_3)

        global_to_ultimatemastery_torment1 = world.get_entrance("Global to UltimateMastery Torment1")
        global_to_ultimatemastery_torment2 = world.get_entrance("Global to UltimateMastery Torment2")
        global_to_ultimatemastery_torment3 = world.get_entrance("Global to UltimateMastery Torment3")
        world.set_rule(global_to_ultimatemastery_torment1, HAS_UM_1)
        world.set_rule(global_to_ultimatemastery_torment2, HAS_UM_2)
        world.set_rule(global_to_ultimatemastery_torment3, HAS_UM_3)

        global_to_slaughtermastery_torment1 = world.get_entrance("Global to SlaughterMastery Torment1")
        global_to_slaughtermastery_torment2 = world.get_entrance("Global to SlaughterMastery Torment2")
        global_to_slaughtermastery_torment3 = world.get_entrance("Global to SlaughterMastery Torment3")
        world.set_rule(global_to_slaughtermastery_torment1, HAS_SM_1)
        world.set_rule(global_to_slaughtermastery_torment2, HAS_SM_2)
        world.set_rule(global_to_slaughtermastery_torment3, HAS_SM_3)

        global_to_relicthief_torment1 = world.get_entrance("Global to RelicThief Torment1")
        global_to_relicthief_torment2 = world.get_entrance("Global to RelicThief Torment2")
        global_to_relicthief_torment3 = world.get_entrance("Global to RelicThief Torment3")
        world.set_rule(global_to_relicthief_torment1, HAS_RT_1)
        world.set_rule(global_to_relicthief_torment2, HAS_RT_2)
        world.set_rule(global_to_relicthief_torment3, HAS_RT_3)

        global_to_weapontrickery_torment1 = world.get_entrance("Global to WeaponTrickery Torment1")
        global_to_weapontrickery_torment2 = world.get_entrance("Global to WeaponTrickery Torment2")
        global_to_weapontrickery_torment3 = world.get_entrance("Global to WeaponTrickery Torment3")
        world.set_rule(global_to_weapontrickery_torment1, HAS_WT_1)
        world.set_rule(global_to_weapontrickery_torment2, HAS_WT_2)
        world.set_rule(global_to_weapontrickery_torment3, HAS_WT_3)

        global_to_deathsedge_torment1 = world.get_entrance("Global to DeathsEdge Torment1")
        global_to_deathsedge_torment2 = world.get_entrance("Global to DeathsEdge Torment2")
        global_to_deathsedge_torment3 = world.get_entrance("Global to DeathsEdge Torment3")
        world.set_rule(global_to_deathsedge_torment1, HAS_DE_1)
        world.set_rule(global_to_deathsedge_torment2, HAS_DE_2)
        world.set_rule(global_to_deathsedge_torment3, HAS_DE_3)

def set_all_location_rules(world: MetalHellsingerWorld) -> None:
    locations: Collection[Location] = world.multiworld.get_locations(world.player)
    for location in locations:
        if location.name in world.location_name_groups["LevelAmmostashCompletion"]:
            world.set_rule(location, HAS_DESTRUCTIBLE_AMMOSTASHES)
        elif location.name in world.location_name_groups["LevelHealthCrystalCompletion"]:
            world.set_rule(location, HAS_DESTRUCTIBLE_HEALTH_CRYSTALS)
        elif location.name in world.location_name_groups["LevelChaosCrystalCompletion"]:
            world.set_rule(location, HAS_DESTRUCTIBLE_CHAOS_CRYSTALS)
        elif location.name in world.location_name_groups["ArenaAmmostashCompletion"]:
            world.set_rule(location, HAS_DESTRUCTIBLE_AMMOSTASHES)
        elif location.name in world.location_name_groups["ArenaHealthCrystalCompletion"]:
            world.set_rule(location, HAS_DESTRUCTIBLE_HEALTH_CRYSTALS)
        elif location.name in world.location_name_groups["ArenaChaosCrystalCompletion"]:
            world.set_rule(location, HAS_DESTRUCTIBLE_CHAOS_CRYSTALS)
        elif location.name in world.location_name_groups["ArenaDestructibleCompletion"]:
            world.set_rule(location, HAS_ALL_DESCTRUCTIBLES)
        elif location.name in world.location_name_groups["Ammostash"]:
            world.set_rule(location, HAS_DESTRUCTIBLE_AMMOSTASHES)
        elif location.name in world.location_name_groups["HealthCrystal"]:
            world.set_rule(location, HAS_DESTRUCTIBLE_HEALTH_CRYSTALS)
        elif location.name in world.location_name_groups["ChaosCrystal"]:
            world.set_rule(location, HAS_DESTRUCTIBLE_CHAOS_CRYSTALS)
        elif location.name in world.location_name_groups["LevelSpeed"]:
            world.set_rule(location, (HAS_SOAR & HAS_DOUBLE_JUMP & HAS_QUICK_RELOAD & (HAS_BEAST | HAS_GOAT | HAS_LAMB)) | OUT_OF_LOGIC)
        elif location.name in world.location_name_groups["TormentGold"]:
            world.set_rule(location, (HAS_QUICK_RELOAD & HAS_ADVANCED_MOVEMENT & HAS_ANY_HEAL) | OUT_OF_LOGIC)


    world.set_rule(world.get_location("Hells First Kill - Marionette"), CAN_REACH_MARIONETTE)
    world.set_rule(world.get_location("Hells First Kill - Cambion"), CAN_REACH_CAMBION)
    world.set_rule(world.get_location("Hells First Kill - Behemoth"), CAN_REACH_BEHEMOTH)
    world.set_rule(world.get_location("Hells First Kill - Stalker"), CAN_REACH_STALKER)
    world.set_rule(world.get_location("Hells First Kill - Eyeless"), CAN_REACH_EYELESS)
    world.set_rule(world.get_location("Hells First Kill - Hierophant"), CAN_REACH_HIEROPHANT)
    world.set_rule(world.get_location("Hells First Kill - Lesser Seraph"), CAN_REACH_LESSER_SERAPH)
    world.set_rule(world.get_location("Hells First Kill - Shield Cambion"), CAN_REACH_SHIELD_CAMBION)
    world.set_rule(world.get_location("Hells First Kill - Siege Behemoth"), CAN_REACH_SIEGE_BEHEMOTH)
    world.set_rule(world.get_location("Hells First Kill - Void Stalker"), CAN_REACH_VOID_STALKER)
    world.set_rule(world.get_location("Hells First Kill - Annihilator Seraph"), CAN_REACH_ANNIHILATOR_SERAPH)

    world.set_rule(world.get_location("Bestiary Entry - Marionette"), HAS_TUTORIAL & HAS_BASE_MOVEMENT)
    world.set_rule(world.get_location("Bestiary Entry - Cambion"), HAS_VOKE | HAS_STYGIA)
    world.set_rule(world.get_location("Bestiary Entry - Behemoth"), CanReachRegion("Voke Arena4") | CanReachRegion("Stygia Arena2"))
    world.set_rule(world.get_location("Bestiary Entry - Stalker"), CanReachRegion("Stygia Arena3"))
    world.set_rule(world.get_location("Bestiary Entry - Eyeless"), CanReachRegion("Yhelm Arena2"))
    world.set_rule(world.get_location("Bestiary Entry - Hierophant"), CanReachRegion("Incaustis Arena2"))
    world.set_rule(world.get_location("Bestiary Entry - Lesser Seraph"), CanReachRegion("Gehenna Arena2"))
    world.set_rule(world.get_location("Bestiary Entry - Shield Cambion"), HAS_YHELM)
    world.set_rule(world.get_location("Bestiary Entry - Siege Behemoth"), CanReachRegion("Incaustis Arena4"))
    world.set_rule(world.get_location("Bestiary Entry - Void Stalker"), CanReachRegion("Nihil Arena3"))
    world.set_rule(world.get_location("Bestiary Entry - Annihilator Seraph"), CanReachRegion("Voke Arena4") & (Has("Archdevil") | Has("Regressive Difficulty")))

    world.set_rule(world.get_location("Stygia - Next Multiplier in Arena 1 on pillar"), HAS_BASE_MOVEMENT)
    world.set_rule(world.get_location("Nihil - Max Multiplier in Arena 1"), HAS_BASE_MOVEMENT)
    world.set_rule(world.get_location("Sheol - Next Multiplier in Arena 2 on back Pillar"), HAS_BASE_MOVEMENT)
    world.set_rule(world.get_location("Sheol - Next Multiplier in Arena 3"), (HAS_DASH | HAS_DOUBLE_JUMP) | JUMP_OUT_OF_LOGIC)

    if(world.options.include_fury_combo_checks):
        world.set_rule(world.get_location("Fury Combo - Styx Reload discovered"), (HAS_ANY_HELL & HAS_QUICK_RELOAD & HAS_DESTRUCTIBLE_HEALTH_CRYSTALS & HAS_RELOADABLE_WEAPON))
        world.set_rule(world.get_location("Fury Combo - Hells's Heartbeat discovered"), (HAS_ANY_HELL & HAS_QUICK_RELOAD & HAS_RELOADABLE_WEAPON))
        world.set_rule(world.get_location("Fury Combo - Basilisk Mode discovered"), (HAS_SOAR & HAS_ANY_HELL))
        world.set_rule(world.get_location("Fury Combo - Double Hit and Run discovered"), (HAS_ANY_HELL & (HAS_DESTRUCTIBLE_AMMOSTASHES | HAS_DESTRUCTIBLE_HEALTH_CRYSTALS | (HAS_DESTRUCTIBLE_CHAOS_CRYSTALS & OUT_OF_LOGIC)) & HAS_DASH))
        world.set_rule(world.get_location("Fury Combo - Shatter Two discovered"), (HAS_ANY_HELL & (HAS_DESTRUCTIBLE_AMMOSTASHES | HAS_DESTRUCTIBLE_HEALTH_CRYSTALS | (HAS_DESTRUCTIBLE_CHAOS_CRYSTALS & OUT_OF_LOGIC))))
        world.set_rule(world.get_location("Fury Combo - Devil's Flight discovered"), (HAS_ANY_HELL & HAS_DASH & HAS_SOAR & HAS_JUMP))
        world.set_rule(world.get_location("Fury Combo - Double Slaughter discovered"), (HAS_ANY_HELL & HAS_SLAUGHTER))
        world.set_rule(world.get_location("Fury Combo - Chaos and Slaughter discovered"), (HAS_CHAOS_ACCESS & HAS_DESTRUCTIBLE_CHAOS_CRYSTALS & HAS_SLAUGHTER))
        world.set_rule(world.get_location("Fury Combo - Unholy Mess discovered"), (HAS_ANY_HELL & HAS_SLAUGHTER))
        world.set_rule(world.get_location("Fury Combo - Five Endings discovered"), (((HAS_CHAOS_ACCESS & HAS_DESTRUCTIBLE_CHAOS_CRYSTALS) | HAS_PAZ) & HasGroup("Weapon", count=3)) | (HasGroup("Weapon", count=1) & OUT_OF_LOGIC))
        world.set_rule(world.get_location("Fury Combo - Slaughter and Kill discovered"), (HAS_ANY_HELL & HAS_SLAUGHTER))
        world.set_rule(world.get_location("Fury Combo - Chaos Flight discovered"), (HAS_CHAOS_ACCESS & HAS_SOAR & HAS_JUMP & HAS_DESTRUCTIBLE_CHAOS_CRYSTALS))
        world.set_rule(world.get_location("Fury Combo - Death from Above discovered"), (HAS_ANY_HELL & HAS_SOAR & HAS_SLAUGHTER))
        world.set_rule(world.get_location("Fury Combo - Lethal Cycle discovered"), (HAS_ANY_HELL & HasGroup("Weapon", count=3)))
        world.set_rule(world.get_location("Fury Combo - Kill Trio discovered"), HAS_ANY_HELL & (HasGroup("Weapon", count=2)| OUT_OF_LOGIC))
        world.set_rule(world.get_location("Fury Combo - Triple Dash discovered"), (HAS_ANY_HELL & HAS_DASH))

    if(world.options.include_first_slaughter_checks):
        world.set_rule(world.get_location("Hells First Slaughter - Marionette"), HAS_SLAUGHTER & CAN_REACH_MARIONETTE)
        world.set_rule(world.get_location("Hells First Slaughter - Cambion"), HAS_SLAUGHTER & CAN_REACH_CAMBION)
        world.set_rule(world.get_location("Hells First Slaughter - Behemoth"), HAS_SLAUGHTER & CAN_REACH_BEHEMOTH)
        world.set_rule(world.get_location("Hells First Slaughter - Stalker"), HAS_SLAUGHTER & CAN_REACH_STALKER)
        world.set_rule(world.get_location("Hells First Slaughter - Eyeless"), HAS_SLAUGHTER & CAN_REACH_EYELESS)
        world.set_rule(world.get_location("Hells First Slaughter - Hierophant"), HAS_SLAUGHTER & CAN_REACH_HIEROPHANT)
        world.set_rule(world.get_location("Hells First Slaughter - Lesser Seraph"), HAS_SLAUGHTER & CAN_REACH_LESSER_SERAPH)
        world.set_rule(world.get_location("Hells First Slaughter - Shield Cambion"), HAS_SLAUGHTER & CAN_REACH_SHIELD_CAMBION)
        world.set_rule(world.get_location("Hells First Slaughter - Siege Behemoth"), HAS_SLAUGHTER & CAN_REACH_SIEGE_BEHEMOTH)
        world.set_rule(world.get_location("Hells First Slaughter - Void Stalker"), HAS_SLAUGHTER & CAN_REACH_VOID_STALKER)
        world.set_rule(world.get_location("Hells First Slaughter - Annihilator Seraph"), HAS_SLAUGHTER & CAN_REACH_ANNIHILATOR_SERAPH)

    if(world.options.randomized_boons_enabled):
        world.set_rule(world.get_location("Voke - Boon Completion"), CanReachRegion("Voke Boss"))
        world.set_rule(world.get_location("Stygia - Boon Completion"), CanReachRegion("Stygia Boss"))
        world.set_rule(world.get_location("Incaustis - Boon Completion"), CanReachRegion("Incaustis Boss"))
        world.set_rule(world.get_location("Nihil - Boon Completion"), CanReachRegion("Nihil Boss"))
        world.set_rule(world.get_location("Activate Enduring Fury for the first time"), Has("Enduring Fury"))
        world.set_rule(world.get_location("Activate Faster Ultimate Gain for the first time"),  (Has("Faster Ultimate Gain") & (HAS_BASE_MOVEMENT| OUT_OF_LOGIC)))
        world.set_rule(world.get_location("Activate Deadlier Dash for the first time"), (Has("Deadlier Dash") & (HAS_BASE_MOVEMENT | OUT_OF_LOGIC)))
        world.set_rule(world.get_location("Activate Explosive Slaughter for the first time"), (Has("Explosive Slaughter") & (HAS_ADVANCED_MOVEMENT | OUT_OF_LOGIC)))

    if(world.options.include_miscellaneous_checks):
        world.set_rule(world.get_location("First Miscellaneous - Slaughter"), HAS_SLAUGHTER)
        world.set_rule(world.get_location("First Miscellaneous - Jump"), HAS_JUMP)
        world.set_rule(world.get_location("First Miscellaneous - Double Jump"), HAS_DOUBLE_JUMP)
        world.set_rule(world.get_location("First Miscellaneous - Quick Reload"), HAS_QUICK_RELOAD & HAS_RELOADABLE_WEAPON)
        world.set_rule(world.get_location("First Miscellaneous - Dash"), HAS_DASH)
        world.set_rule(world.get_location("First Miscellaneous - Soar"), HAS_SOAR)
        world.set_rule(world.get_location("First Miscellaneous - Ammostash"), HAS_DESTRUCTIBLE_AMMOSTASHES)
        world.set_rule(world.get_location("First Miscellaneous - Health Crystal"), HAS_DESTRUCTIBLE_HEALTH_CRYSTALS)
        world.set_rule(world.get_location("First Miscellaneous - Chaos Crystal"), HAS_CHAOS_ACCESS & HAS_DESTRUCTIBLE_CHAOS_CRYSTALS)
        world.set_rule(world.get_location("Activate Paz' Ultimate for the first time"), HAS_ANY_HELL & HAS_PAZ_WITH_ULTIMATE)
        world.set_rule(world.get_location("Activate Terminus' Ultimate for the first time"), HAS_ANY_HELL & HAS_TERMINUS_WITH_ULTIMATE)
        world.set_rule(world.get_location("Activate Persephones Ultimate for the first time"), HAS_ANY_HELL & HAS_PERSEPHONE_WITH_ULTIMATE)
        world.set_rule(world.get_location("Activate the Hounds Ultimate for the first time"), HAS_ANY_HELL & HAS_THE_HOUNDS_WITH_ULTIMATE)
        world.set_rule(world.get_location("Activate Vulcans Ultimate for the first time"), HAS_ANY_HELL & HAS_VULCAN_WITH_ULTIMATE)
        world.set_rule(world.get_location("Activate Hellcrows Ultimate for the first time"), HAS_ANY_HELL & HAS_HELLCROW_WITH_ULTIMATE)

        if world.options.include_dream_of_the_beast_weapon:
            world.set_rule(world.get_location("Activate the Red Right Hands Ultimate for the first time"), HAS_ANY_HELL & HAS_THE_RED_RIGHT_HAND_WITH_ULTIMATE)
        if world.options.include_purgatory_weapon:
            world.set_rule(world.get_location("Activate Telos' Ultimate for the first time"), HAS_ANY_HELL & HAS_TELOS_WITH_ULTIMATE)
        if(world.options.randomized_jump_enabled):
            world.set_rule(world.get_location("First Miscellaneous - Infinite Jump"), HAS_INFINITE_JUMP)

    if(world.options.include_randomized_weapon_skins_checks):
        world.set_rule(world.get_location("Collect 2 Coat of Arms"), Has("Coat of Arms", count=2))
        world.set_rule(world.get_location("Collect 8 Coat of Arms"), Has("Coat of Arms", count=8))
        world.set_rule(world.get_location("Collect 14 Coat of Arms"), Has("Coat of Arms", count=14))
        world.set_rule(world.get_location("Collect 20 Coat of Arms"), Has("Coat of Arms", count=20))
        world.set_rule(world.get_location("Collect 26 Coat of Arms"), Has("Coat of Arms", count=26))
        world.set_rule(world.get_location("Collect 32 Coat of Arms"), Has("Coat of Arms", count=32))

    if(world.options.include_section_clears_with_weapons_checks):
        world.set_rule(world.get_location("Section Cleared with: Paz"), HAS_PAZ)
        world.set_rule(world.get_location("Section Cleared with: Terminus"), HAS_TERMINUS)
        world.set_rule(world.get_location("Section Cleared with: Persephone"), Has("Persephone"))
        world.set_rule(world.get_location("Section Cleared with: The Hounds"), Has("The Hounds"))
        world.set_rule(world.get_location("Section Cleared with: Vulcan"), Has("Vulcan"))
        world.set_rule(world.get_location("Section Cleared with: Hellcrow"), HAS_HELLCROW)

        if(world.options.include_dream_of_the_beast_weapon):
            world.set_rule(world.get_location("Section Cleared with: The Red Right Hand"), Has("The Red Right Hand"))

        if(world.options.include_purgatory_weapon):
            world.set_rule(world.get_location("Section Cleared with: Telos"), Has("Telos"))

        if(world.options.include_additional_weapon_variants):
            world.set_rule(world.get_location("Section Cleared with: Lost Persephone"), Has("Lost Persephone"))
            world.set_rule(world.get_location("Section Cleared with: Manifested Persephone"), Has("Manifested Persephone"))
            world.set_rule(world.get_location("Section Cleared with: The Lost Hounds"), Has("The Lost Hounds"))
            world.set_rule(world.get_location("Section Cleared with: Lost Vulcan"), Has("Lost Vulcan"))

    if(world.options.randomized_outfits_enabled and world.options.include_section_clears_with_outfits_checks):
        world.set_rule(world.get_location("Section Cleared with: Outfit of the Unknown"), Has("Outfit of the Unknown"))
        world.set_rule(world.get_location("Section Cleared with: Outfit of the Leviathan"), Has("Outfit of the Leviathan"))

        if(world.options.include_dream_of_the_beast_outfits):
            world.set_rule(world.get_location("Section Cleared with: Outfit of the Dark Devotee"), Has("Outfit of the Dark Devotee"))
            world.set_rule(world.get_location("Section Cleared with: Outfit of the Morning Star"), Has("Outfit of the Morning Star"))
            world.set_rule(world.get_location("Section Cleared with: Outfit of the Angel Eyes"), Has("Outfit of the Angel Eyes"))

        if(world.options.include_purgatory_outfits):
            world.set_rule(world.get_location("Section Cleared with: Outfit of the Obsidian"), Has("Outfit of the Obsidian"))
            world.set_rule(world.get_location("Section Cleared with: Outfit of the Amethyst"), Has("Outfit of the Amethyst"))
            world.set_rule(world.get_location("Section Cleared with: Outfit of the Chromatica"), Has("Outfit of the Chromatica"))

    if(world.options.randomized_songs_enabled and world.options.include_section_clears_with_songs_checks):
        world.set_rule(world.get_location("Section Cleared with: This is the End"), Has("This is the End"))
        world.set_rule(world.get_location("Section Cleared with: Stygia (Song)"), Has("Stygia (Song)"))
        world.set_rule(world.get_location("Section Cleared with: Burial At Night"), Has("Burial At Night"))
        world.set_rule(world.get_location("Section Cleared with: This Devastation"), Has("This Devastation"))
        world.set_rule(world.get_location("Section Cleared with: Poetry of Cinder"), Has("Poetry of Cinder"))
        world.set_rule(world.get_location("Section Cleared with: Dissolution"), Has("Dissolution"))
        world.set_rule(world.get_location("Section Cleared with: Acheron (Song)"), Has("Acheron (Song)"))
        world.set_rule(world.get_location("Section Cleared with: Silent No More"), Has("Silent No More"))
        world.set_rule(world.get_location("Section Cleared with: Blood and Law"), Has("Blood and Law"))
        world.set_rule(world.get_location("Section Cleared with: Infernal Invocation I: Hopes and Fears"), Has("Infernal Invocation I: Hopes and Fears"))
        world.set_rule(world.get_location("Section Cleared with: Infernal Invocation II: Defiance"), Has("Infernal Invocation II: Defiance"))
        world.set_rule(world.get_location("Section Cleared with: Infernal Invocation III: Dreaming in Distortion"), Has("Infernal Invocation III: Dreaming in Distortion"))
        world.set_rule(world.get_location("Section Cleared with: No Tomorrow"), Has("No Tomorrow"))

        if(world.options.include_dream_of_the_beast_songs):
            world.set_rule(world.get_location("Section Cleared with: Leviathan (Song)"), Has("Leviathan (Song)"))
            world.set_rule(world.get_location("Section Cleared with: Dream of the Beast"), Has("Dream of the Beast"))

        if(world.options.include_purgatory_songs):
            world.set_rule(world.get_location("Section Cleared with: Swallow the Fire"), Has("Swallow the Fire"))
            world.set_rule(world.get_location("Section Cleared with: Mouth of Hell"), Has("Mouth of Hell"))
            world.set_rule(world.get_location("Section Cleared with: Goodbye, Morning Star"), Has("Goodbye, Morning Star"))

        if(world.options.include_essential_hits_soundtrack_songs):
            world.set_rule(world.get_location("Section Cleared with: Down With the Sickness"), Has("Down With the Sickness"))
            world.set_rule(world.get_location("Section Cleared with: Uprising"), Has("Uprising"))
            world.set_rule(world.get_location("Section Cleared with: Misery Business"), Has("Misery Business"))
            world.set_rule(world.get_location("Section Cleared with: Tsunami (Original Mix)"), Has("Tsunami (Original Mix)"))
            world.set_rule(world.get_location("Section Cleared with: Runaway (U&I)"), Has("Runaway (U&I)"))
            world.set_rule(world.get_location("Section Cleared with: Feel Good Inc."), Has("Feel Good Inc."))
            world.set_rule(world.get_location("Section Cleared with: I Love It feat. Charli XCX"), Has("I Love It feat. Charli XCX"))
            world.set_rule(world.get_location("Section Cleared with: Personal Jesus"), Has("Personal Jesus"))

        if(world.options.include_dusk_soundtrack_songs):
            world.set_rule(world.get_location("Section Cleared with: Departure to Destruction"), Has("Departure to Destruction"))
            world.set_rule(world.get_location("Section Cleared with: Hand Cannon"), Has("Hand Cannon"))
            world.set_rule(world.get_location("Section Cleared with: Burn in Hell"), Has("Burn in Hell"))
            world.set_rule(world.get_location("Section Cleared with: Murder Machine Inc"), Has("Murder Machine Inc"))
            world.set_rule(world.get_location("Section Cleared with: Endless"), Has("Endless"))
            world.set_rule(world.get_location("Section Cleared with: Mine Control"), Has("Mine Control"))
            world.set_rule(world.get_location("Section Cleared with: Sacrifice"), Has("Sacrifice"))
            world.set_rule(world.get_location("Section Cleared with: Erebus Reaction"), Has("Erebus Reaction"))
            world.set_rule(world.get_location("Section Cleared with: Bleeding Out"), Has("Bleeding Out"))

    if world.options.require_coat_of_arms_for_sheol or world.options.include_coat_of_arms_checks or world.options.include_randomized_weapon_skins_checks:
        world.set_rule(world.get_location("Voke - Coat of Arms before Arena 1"), HAS_DASH | JUMP_OUT_OF_LOGIC)
        world.set_rule(world.get_location("Stygia - Coat of Arms between Arena 1 & 2"), HAS_DASH | JUMP_OUT_OF_LOGIC)
        world.set_rule(world.get_location("Yhelm - Coat of Arms between Arena 3 & 4"), HAS_DASH | JUMP_OUT_OF_LOGIC)
        world.set_rule(world.get_location("Yhelm - Coat of Arms in Arena 3"), HAS_DASH | JUMP_OUT_OF_LOGIC)
        world.set_rule(world.get_location("Yhelm - Coat of Arms in Arena 1"), HAS_BASE_MOVEMENT)
        world.set_rule(world.get_location("Gehenna - Coat of Arms between Arena 1 & 2"), CanReachRegion("Gehenna Arena2") | OUT_OF_LOGIC)
        world.set_rule(world.get_location("Gehenna - Coat of Arms between Arena 2 & 3"), HAS_BASE_MOVEMENT)
        world.set_rule(world.get_location("Nihil - Coat of Arms between Arena 3 & 4"), HAS_BASE_MOVEMENT)
        world.set_rule(world.get_location("Nihil - Coat of Arms between Arena 1 & 2"), HAS_DASH | JUMP_OUT_OF_LOGIC)
        world.set_rule(world.get_location("Acheron - Coat of Arms between Arena 1 & 2"), HAS_BASE_MOVEMENT)
        world.set_rule(world.get_location("Acheron - Coat of Arms in Arena 3"), HAS_DASH | JUMP_OUT_OF_LOGIC)
        world.set_rule(world.get_location("Sheol - Coat of Arms before Arena 1"), HAS_DASH | HAS_DOUBLE_JUMP | JUMP_OUT_OF_LOGIC)
        world.set_rule(world.get_location("Sheol - Coat of Arms between Arena 1 & 2"), HAS_DASH | HAS_DOUBLE_JUMP | JUMP_OUT_OF_LOGIC)
        world.set_rule(world.get_location("Sheol - Coat of Arms between Arena 2 & 3"), HAS_DASH | JUMP_OUT_OF_LOGIC)

    if world.options.include_secret_multiplier_checks:
        world.set_rule(world.get_location("Stygia - Secret Max Multiplier"), HAS_DASH | JUMP_OUT_OF_LOGIC)
        world.set_rule(world.get_location("Yhelm - Secret Max Multiplier"), HAS_DASH | HAS_DOUBLE_JUMP | JUMP_OUT_OF_LOGIC)
        world.set_rule(world.get_location("Gehenna - Secret Max Multiplier"), HAS_DASH | HAS_DOUBLE_JUMP | JUMP_OUT_OF_LOGIC)
        world.set_rule(world.get_location("Acheron - Secret Max Multiplier"), HAS_BASE_MOVEMENT)
        world.set_rule(world.get_location("Sheol - Secret Max Multiplier"), HAS_DASH | JUMP_OUT_OF_LOGIC)


def set_completion_condition(world: MetalHellsingerWorld) -> None:
    has_requires_bosses = OptionFilter(WinCondition, WinCondition.option_hells_completion)
    has_requires_sheol = OptionFilter(WinCondition, WinCondition.option_sheol_completion)
    has_completed = (has_requires_bosses & Has("Aspect Slain", count=FromOption(RequiredHellsCompletion))) | (
        has_requires_sheol & Has("Red Judge Slain")
    )
    world.set_completion_rule(has_completed)
