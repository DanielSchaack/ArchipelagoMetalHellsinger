from dataclasses import dataclass
from functools import cached_property
from itertools import accumulate

from Options import (
    Choice,
    DefaultOnToggle,
    ItemDict,
    OptionGroup,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
)


class WinCondition(Choice):
    """
    Hells Completion - To complete the game, slay the required amount of Aspects
    Sheol Completion - To complete the game, require the completion of the Hell 'Sheol'
    """
    display_name = "Win Condition"
    option_hells_completion = 0
    option_sheol_completion = 1
    default = 1

class RequiredHellsCompletion(Range):
    """
    If Hells completions are required, select the number of slain Aspects that are required for completion.
    """
    display_name = "Required Number of Aspects Slain"
    range_start = 1
    range_end = 8
    default = 5


# ---

class RegressiveDifficulty(Toggle):
    """
    If enabled, starts the game in the highest difficulty (Archdevil) and can be lowered by collecting regressive difficulty items.

    Warning: This IS difficult, especially with some randomized abilities.
    """

    display_name = "Regressive Difficulty"


class StartingDifficulty(Choice):
    """
    The individual difficulties are their own items while regressive difficulty is disabled.
    If Archdevil is chosen while it isn't added using "Include Archdevil Difficulty", Beast is chosen instead.

    - Lamb = Easy
    - Goat = Medium
    - Beast = Hard
    - Archdevil = Very Hard
    """

    display_name = "Starting Difficulty"
    option_lamb = 0
    option_goat = 1
    option_beast = 2
    option_archdevil = 3
    default = 1


class IncludeArchdevilDifficulty(Toggle):
    """
    If enabled, includes the Archdevil difficulty as an item.

    Note: Archdevil is not beginner friendly.
    Note: Archdevil may make certain 'First Kill' and 'First Slaughter' checks available earlier than expected, forcing you to play on said difficulty.
    """

    display_name = "Include Archdevil Difficulty"


class MinimalDifficulty(Choice):
    """
    Collecting locations requires atleast this difficulty.
    If the starting difficulty is below the required one, the needed difficulty will be given instead.
    Logic respects this option.

    - Lamb = Easy
    - Goat = Medium
    - Beast = Hard
    - Archdevil = Very Hard
    """

    display_name = "Minimally Required Difficulty"
    option_lamb = 0
    option_goat = 1
    option_beast = 2
    option_archdevil = 3
    default = 0



class StartingHells(Choice):
    """
    If Hells are randomized as individual unlocks, select your starting Hell.
    """

    display_name = "Starting Hell"
    option_voke = 0
    option_stygia = 1
    option_yhelm = 2
    option_incaustis = 3
    option_gehenna = 4
    option_nihil = 5
    option_acheron = 6
    default = 0


class HellsUnlocksAsProgressive(Toggle):
    """
    Hells are included as progressive instead of individual unlocks.

    The order of Hells is: Voke - Stygia - Yhelm - Incaustis - Gehenna - Nihil - Acheron - Sheol
    Tutorial is its own item.
    """

    display_name = "Hells Unlocks as Progressive"


class RandomizedTormentsEnabled(DefaultOnToggle):
    """
    Includes the Torments as unlockables.
    """

    display_name = "Randomized Torments"


class TormentUnlocksAsProgressive(Toggle):
    """
    When Torments are included as unlockables, change these to be progressive instead of individual unlocks.

    Each Torment progresses on its own, with progressive 'Killing with Rhythm', 'Weapon Trickery' as items.
    """

    display_name = "Torment Unlocks as Progressive"


class RequireStageForTorments(Toggle):
    """
    If enabled, unlocks Torments only when their respective Hell is unlocked.
    I.e. to play 'Killing with Rhythm: 1', 'Voke' is also required to start KwR1
    """

    display_name = "Require the Hell associated with Torments"


class RequireWeaponsForTorments(Toggle):
    """
    If enabled, unlocks Torments only when their weapons are unlocked.
    I.e. to play 'Killing with Rhythm: 1', 'Paz' and 'Persephone' are also required to start KwR1
    Note: For Ultimate Mastery, this includes weapon ultimates
    """

    display_name = "Require associated Weapons for Torments"


class RandomizedLevelsEnabled(Toggle):
    """
    Randomly mixes Hells and Torments with eachother.

    The original unlock requirements still apply to the newly shuffled levels.

    If 'Sheol' is now at 'Killing with Rhythm: 1', then it still requires either atleast 1 progressive 'Killing with Rhythm'
    or its unlock directly, and potentially its Hell and weapons, depending on other options enabled.
    """

    display_name = "Mix Hells and Torments with eachother"


# ---


class RequireAspectForBossArena(Toggle):
    """
    If enabled, adds the Aspects as unlockables to the item pool.

    Without the Aspect of a Hell, the boss arena can't be entered.
    Hells with Aspects: Voke - Stygia - Yhelm - Incaustis - Gehenna - Nihil - Acheron
    """

    display_name = "Require the Aspect of a Hell to access its Boss"


class RequireNoTomorrowForSheol(Toggle):
    """
    If enabled with randomized songs, requires the boss song 'No Tomorrow' to access 'Sheol'
    """

    display_name = "Require Boss Song 'No Tomorrow' for Sheol"


class RequireCoatOfArmsForSheol(Toggle):
    """
    If enabled, requires a certain amount of Coat of Arms to access 'Sheol'

    If no other option randomizes Coat of Arms, adds each Coat of Arms as a location that grant a Coat of Arms for each non-Sheol Hell (28),
    as well as 4 randomized ones (those from Sheol) into the item pool.
    """

    display_name = "Require Coat of Arms for Sheol"


class RequiredCoatOfArmsForSheol(Range):
    """
    The required amount of Coat of Arms to access 'Sheol'
    """

    display_name = "Required Coat of Arms for Sheol"
    range_start = 1
    range_end = 32
    default = 26


# ---

class ArchdevilEnemiesEnabled(Toggle):
    """
    If enabled, adds all Archdevil enemy spawn _on top of_ the regular enemy spawns, resulting in more difficult encounters.
    """

    display_name = "Enable Archdevil Enemy Spawns in all Difficulties"


class RandomizedBoonsEnabled(Toggle):
    """
    If enabled, adds all 4 Beatstreak Boons as items and locations to the pool.
    """

    display_name = "Randomize Beatstreak Boons"


class RandomizedDashEnabled(Toggle):
    """
    If enabled, adds the ability to Dash and Soar as progressive items to the pool.

    Note: The randomizer includes "soft logic" as to requiring certain abilities to access certain parts of hells.
    Warning: Randomizing too many abilities may lead to very restrictive and difficult starting scenarios.
    """

    display_name = "Randomize Dash and Soar"


class RandomizedJumpEnabled(Toggle):
    """
    If enabled, adds the ability to Jump and Double Jump as progressive items to the pool.

    Note: The randomizer includes "soft logic" as to requiring certain abilities to access certain parts of hells.
    Warning: Randomizing too many abilities may lead to very restrictive and difficult starting scenarios.
    """

    display_name = "Randomize Jump and Double Jump"


class RandomizedReloadEnabled(Toggle):
    """
    If enabled, adds the ability to Quick and Manual Reload as progressive items to the pool.

    Note: The randomizer includes "soft logic" as to requiring certain abilities to access certain parts of hells.
    Warning: Randomizing too many abilities may lead to very restrictive and difficult starting scenarios.
    """

    display_name = "Randomize Quick and Manual Reload"


class RandomizedWeaponUltimatesEnabled(Toggle):
    """
    If enabled, adds the ability to use weapons ultimates as an individual item for each weapon to the pool.

    Note: Ultimate Mastery Torments won't be in logic until all of the required weapons can use their ultimates in them.
    """

    display_name = "Randomize Weapon Ultimates"


class RandomizedSlaughterEnabled(Toggle):
    """
    If enabled, adds the ability to Slaughter as an item to the pool.

    Note: Slaughter Mastery Torments won't be doable until Slaughter is unlocked.
    Note: The randomizer includes "soft logic" as to requiring certain abilities to access certain parts of hells.
    Warning: Randomizing too many abilities may lead to very restrictive and difficult starting scenarios.
    """

    display_name = "Randomize Slaughter"


class DestructibleAsUnlocks(Toggle):
    """
    If enabled, adds the abilities to destroy each destructible type as unlocks to the item pool.

    Note: This includes the ability to destroy Health Crystals, removing one source of healing
    Note: The randomizer includes "soft logic" as to requiring certain abilities to access certain parts of hells.
    Warning: Randomizing too many abilities may lead to very restrictive and difficult starting scenarios.
    """

    display_name = "Randomize Destructible Object Types"


class StartingWeapon(Choice):
    """
    The Randomizer always starts with just one weapon.

    If the weapon is not included, a fallback weapon from the available ones is chosen.
    Note: The randomizer expects you to own the DLC yourself and won't grant them on its own.
    """

    display_name = "Starting Weapon"
    option_persephone = 2
    option_the_hounds = 3
    option_vulcan = 4
    option_hellcrow = 5
    option_the_red_right_hand = 6
    option_telos = 7
    option_lost_persephone = 8
    option_manifested_persephone = 9
    option_the_lost_hounds = 10
    option_lost_vulcan = 11
    default = 2


class IncludeDreamOfTheBeastWeapon(Toggle):
    """
    If enabled, adds the Red Right Hand to the item pool.

    Note: The randomizer expects you to own the DLC yourself and won't grant them on its own.
    """

    display_name = "Include 'Dream of the Beast' DLCs The Red Right Hand"


class IncludePurgatoryWeapon(Toggle):
    """
    If enabled, adds the Telos to the item pool.

    Note: The randomizer expects you to own the DLC yourself and won't grant them on its own.
    """

    display_name = "Include 'Purgatory' DLCs Telos as a Weapon"


class IncludeAdditionalWeaponVariants(Toggle):
    """
    If enabled, adds the 'Lost' and 'Manifested' weapons from the Leviathan Mode to the item pool.

    Important: Adjust your Randomizer Configuration to access these alternate versions!
    """

    display_name = "Include additional Weapon Variants"


class RandomizedOutfitsEnabled(Toggle):
    """
    If enabled, adds the outfits as items to the pool.
    """

    display_name = "Randomize Outfits"


class StartingOutfit(Choice):

    """
    If randomized outfits are enabled, pick your starting outfit.

    If the outfit is not included, a fallback outfit from the available ones is chosen.
    Note: The randomizer expects you to own the DLC yourself and won't grant them on its own.
    """

    display_name = "Starting Outfit"
    option_the_unknown = 0
    option_the_leviathan = 1
    option_the_dark_devotee = 2
    option_the_morning_star = 3
    option_the_angel_eyes = 4
    option_the_obsidian = 5
    option_the_amethyst = 6
    option_the_chromatica = 7
    default = 0


class IncludeDreamOfTheBeastOutfits(Toggle):
    """
    If enabled, add all 3 DLC outfits as items to the pool.

    Note: The randomizer expects you to own the DLC yourself and won't grant them on its own.
    """

    display_name = "Include Dream of the Beast Outfits"


class IncludePurgatoryOutfits(Toggle):
    """
    If enabled, add all 3 DLC outfits as items to the pool.

    Note: The randomizer expects you to own the DLC yourself and won't grant them on its own.
    """

    display_name = "Include Purgatory Outfits"


class RandomizedSongsEnabled(Toggle):
    """
    If enabled, adds the game's songs as items to the pool.
    """

    display_name = "Randomize Main and Boss Songs"


class StartingMainSong(Choice):
    """
    If randomized songs are enabled, pick your starting main song.
    """

    display_name = "Starting Main Song"
    option_this_is_the_end = 0
    option_stygia = 1
    option_burial_at_night = 2
    option_this_devastation = 3
    option_poetry_of_cinder = 4
    option_dissolution = 5
    option_acheron = 6
    option_silent_no_more = 7
    default = 0


class StartingBossSong(Choice):
    """
    If randomized songs are enabled, pick your starting boss song.
    """

    display_name = "Starting Boss Song"
    option_blood_and_law = 0
    option_infernal_invocation_i_hopes_and_fears = 1
    option_infernal_invocation_ii_defiance = 2
    option_infernal_invocation_iii_dreaming_in_distortion = 3
    option_no_tomorrow = 4
    default = 0


class IncludeDuskSoundtrackSongs(Toggle):
    """
    If enabled, adds all 9 Dusk Soundtrack songs as items to the pool.
    """

    display_name = "Include Dusk Soundtrack Songs"


class IncludeDreamOfTheBeastSongs(Toggle):
    """
    If enabled, adds both Dream of the Beast songs as items to the pool.

    Note: The randomizer expects you to own the DLC yourself and won't grant them on its own.
    """

    display_name = "Include Dream of the Beast Songs"


class IncludePurgatorySongs(Toggle):
    """
    If enabled, adds all 3 Purgatory songs as items to the pool.

    Note: The randomizer expects you to own the DLC yourself and won't grant them on its own.
    """

    display_name = "Include Purgatory Songs"


class IncludeEssentialHitsSoundtrackSongs(Toggle):
    """
    If enabled, adds all 8 Essential Hits songs as items to the pool.

    Note: The randomizer expects you to own the DLC yourself and won't grant them on its own.
    """

    display_name = "Include Essential Hits Songs"

class IncludeProgressiveAnguishGateSkips(Choice):
    """
    If enabled, includes items that allow to skip already completed encounters.

    'Encounter Skips For Completions' places these items at the finishing point of encounters.
    'Randomized Progressive Encounter Skips' adds the skips as progressive items into the item pool.
    'Randomized Individual Encounter Skips' adds the skips as individual items into the item pool, i.e. 'Voke Anguish Gate 1 Skip' instead of 'Progressive Voke Anguish Gate'.
    """

    display_name = "Include Progressive Anguish Gate Skips"
    option_no_encounter_skips = 0
    option_encounter_skips_for_completions = 1
    option_randomized_progressive_encounter_skips = 2
    option_randomized_individual_encounter_skips = 3
    default = 0

filler_item_default = {
    "Next Multiplier": 50,
    "Max Multiplier": 50,
    "Reset Multiplier": 20,
    "Trigger Ultimate": 35,
    "Compliment": 50,
    "Encouragement": 50,
    "Failure": 50,
    "Double Time": 20,
    "Half Time": 20,
    "Always on Beat": 35,
    "Invisible Weapons": 35,
    "Weapon Trickery": 35,
    "Death": 1,
}

class FillerItemsDistribution(ItemDict):
    """
    Controls the relative probability of each filler item being generated.
    """

    default = filler_item_default.copy()
    valid_keys = default.keys()
    display_name = "Filler/Trap Items Distribution"

    @cached_property
    def weights_pair(self) -> dict[str, int]:
        return dict(zip(self.value.keys(), accumulate(self.value.values()), strict=False))

# ---

class IncludeFuryComboChecks(Toggle):
    """
    If enabled, adds the first time activations of each Fury Combo as Checks.

    This includes such actions as Triple Dash, Slaughter and Kill, Five Endings and so on.
    """

    display_name = "Enable Fury Combo First Time Activations as Checks"


class IncludeTormentMedaillonsChecks(DefaultOnToggle):
    """
    Includes the individual medals on each Torment as locations.
    """

    display_name = "Include Torment Medals as Locations"


class IncludeSectionClearsWithWeaponsChecks(Toggle):
    """
    If enabled, adds for each randomized weapon a location for clearing a section with them.

    A section is either finishing all four encounters AND entering the boss fight, or finishing the boss fight itself.
    Warning: This may become tedious to do for each available weapon
    """

    display_name = "Include Section Clears for Weapons"


class IncludeSectionClearsWithOutfitsChecks(Toggle):
    """
    If enabled, adds for each randomized outfit a location for clearing a section with them.

    A section is either finishing all four encounters AND entering the boss fight, or finishing the boss fight itself.
    Warning: This may become tedious to do for each available outfit
    """

    display_name = "Include Section Clears for Outfits"


class IncludeSectionClearsWithSongsChecks(Toggle):
    """
    If enabled, adds for each randomized main and boss song a location for clearing a section with them.

    A section is either finishing all four encounters AND entering the boss fight, or finishing the boss fight itself.
    Warning: This may become tedious to do for each available song
    """

    display_name = "Include Section Clears for Songs"


class IncludeWeaponSkinsChecks(Toggle):
    """
    If enabled, adds the unlockable weapon skins as locations to the pool, including the skins themself as items.

    Also adds each Coat of Arms as a location that grant a Coat of Arms if no other options randomize them.
    """

    display_name = "Enable Weapon Skins as Checks"


class IncludeSecretMultiplierChecks(Toggle):
    """
    If enabled, adds the secret Multiplier of each Hells as a location.

    Good luck finding them!
    """

    display_name = "Enable Secret Multipliers as Checks"


class IncludeCoatOfArmsChecks(Toggle):
    """
    If enabled, adds all Coat of Arms as collectibles into the item pool.
    Also adds each Coat of Arms as a location.
    """

    display_name = "Enable Coat of Arms as Checks"


class IncludeMiscellaneousChecks(Toggle):
    """
    If enabled, adds various first time actions such as using ultimates, reaching beat streaks, slaughtering and so on.

    Synergistic for enabling various ability randomizations.
    """

    display_name = "Enable Miscellaneous First Time Actions as Checks"


class IncludeFirstSlaughterChecks(Toggle):
    """
    If enabled, adds the first time slaughter kill of each enemy as a check.
    """

    display_name = "Enable First Time Slaughter Kills as Checks"


# class HellsLevelSpeedEnabled(Toggle):
#     """"""
#     display_name = ""


class DestructibleLocationsEnabled(Toggle):
    """
    If enabled, adds a location to destroy all destructibles of each type (Ammostash, Health/Chaos Crystal) in each encounter.
    Note: Each Destructible only needs to be destroyed once. Destruction status is saved between runs.
    """

    display_name = "Destructible Completionist per Encounter"


class SingularDestructibleLocationsEnabled(Toggle):
    """
    Requires 'Destructible Completionist per Encounter' to be enabled
    If enabled, adjusts the destructible checks to be per type per encounter, instead of one check for all destructibles per encounter.
    Note: Each Destructible only needs to be destroyed once. Destruction status is saved between runs.
    """

    display_name = "Destructible Completionist per Type per Encounter"


class HellsDestructibleLocationsEnabled(Toggle):
    """
    If enabled, adds additional locations to destroy all of each type of destructible in a Hell.
    Note: Each Destructible only needs to be destroyed once. Destruction status is saved between runs.
    """

    display_name = "Destructible Completionist per Hell"


@dataclass
class MetalHellsingerOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    win_condition: WinCondition
    required_hells_completion: RequiredHellsCompletion
    regressive_difficulty: RegressiveDifficulty
    starting_difficulty: StartingDifficulty
    include_archdevil_difficulty: IncludeArchdevilDifficulty
    minimal_difficulty: MinimalDifficulty
    hells_unlocks_as_progressive: HellsUnlocksAsProgressive
    require_aspect_for_boss_arena: RequireAspectForBossArena
    starting_hells: StartingHells
    randomized_torments_enabled: RandomizedTormentsEnabled
    torment_unlocks_as_progressive: TormentUnlocksAsProgressive
    require_stage_for_torments: RequireStageForTorments
    require_weapons_for_torments: RequireWeaponsForTorments
    # randomized_levels_enabled: RandomizedLevelsEnabled
    require_no_tomorrow_for_sheol: RequireNoTomorrowForSheol
    require_coat_of_arms_for_sheol: RequireCoatOfArmsForSheol
    required_coat_of_arms_for_sheol: RequiredCoatOfArmsForSheol
    archdevil_enemies_enabled: ArchdevilEnemiesEnabled
    randomized_boons_enabled: RandomizedBoonsEnabled
    randomized_dash_enabled: RandomizedDashEnabled
    randomized_jump_enabled: RandomizedJumpEnabled
    randomized_reload_enabled: RandomizedReloadEnabled
    randomized_weapon_ultimates_enabled: RandomizedWeaponUltimatesEnabled
    randomized_slaughter_enabled: RandomizedSlaughterEnabled
    destructible_as_unlocks: DestructibleAsUnlocks
    starting_weapon: StartingWeapon
    include_dream_of_the_beast_weapon: IncludeDreamOfTheBeastWeapon
    include_purgatory_weapon: IncludePurgatoryWeapon
    include_additional_weapon_variants: IncludeAdditionalWeaponVariants
    randomized_outfits_enabled: RandomizedOutfitsEnabled
    starting_outfit: StartingOutfit
    include_dream_of_the_beast_outfits: IncludeDreamOfTheBeastOutfits
    include_purgatory_outfits: IncludePurgatoryOutfits
    randomized_songs_enabled: RandomizedSongsEnabled
    starting_main_song: StartingMainSong
    starting_boss_song: StartingBossSong
    include_dream_of_the_beast_songs: IncludeDreamOfTheBeastSongs
    include_purgatory_songs: IncludePurgatorySongs
    include_essential_hits_soundtrack_songs: IncludeEssentialHitsSoundtrackSongs
    include_dusk_soundtrack_songs: IncludeDuskSoundtrackSongs
    include_progressive_anguish_gate_skips: IncludeProgressiveAnguishGateSkips
    filler_items_distribution: FillerItemsDistribution
    include_coat_of_arms_checks: IncludeCoatOfArmsChecks
    torment_medaillons_enabled: IncludeTormentMedaillonsChecks
    include_secret_multiplier_checks: IncludeSecretMultiplierChecks
    include_randomized_weapon_skins_checks: IncludeWeaponSkinsChecks
    include_section_clears_with_weapons_checks: IncludeSectionClearsWithWeaponsChecks
    include_section_clears_with_outfits_checks: IncludeSectionClearsWithOutfitsChecks
    include_section_clears_with_songs_checks: IncludeSectionClearsWithSongsChecks
    destructible_locations_enabled: DestructibleLocationsEnabled
    singular_destructible_locations_enabled: SingularDestructibleLocationsEnabled
    hells_destructible_locations_enabled: HellsDestructibleLocationsEnabled
    include_miscellaneous_checks: IncludeMiscellaneousChecks
    include_first_slaughter_checks: IncludeFirstSlaughterChecks
    include_fury_combo_checks: IncludeFuryComboChecks


option_groups = [
    OptionGroup(
        "Goal Options",
        [
            WinCondition,
            RequiredHellsCompletion,
            RequireNoTomorrowForSheol,
            RequireCoatOfArmsForSheol,
            RequiredCoatOfArmsForSheol,
        ],
    ),
    OptionGroup(
        "Hells and Torments Options",
        [
            HellsUnlocksAsProgressive,
            StartingHells,
            RequireAspectForBossArena,
            RegressiveDifficulty,
            IncludeArchdevilDifficulty,
            StartingDifficulty,
            MinimalDifficulty,
            ArchdevilEnemiesEnabled,
            RandomizedTormentsEnabled,
            TormentUnlocksAsProgressive,
            RequireStageForTorments,
            RequireWeaponsForTorments,
            # RandomizedLevelsEnabled,
        ],
    ),
    OptionGroup(
        "Randomized Items Options",
        [
            StartingWeapon,
            IncludeDreamOfTheBeastWeapon,
            IncludePurgatoryWeapon,
            IncludeAdditionalWeaponVariants,
            RandomizedOutfitsEnabled,
            StartingOutfit,
            IncludeDreamOfTheBeastOutfits,
            IncludePurgatoryOutfits,
            RandomizedSongsEnabled,
            StartingMainSong,
            StartingBossSong,
            IncludeDuskSoundtrackSongs,
            IncludeDreamOfTheBeastSongs,
            IncludePurgatorySongs,
            IncludeEssentialHitsSoundtrackSongs,
            IncludeProgressiveAnguishGateSkips,
            RandomizedSlaughterEnabled,
            RandomizedDashEnabled,
            RandomizedJumpEnabled,
            RandomizedReloadEnabled,
            RandomizedWeaponUltimatesEnabled,
            RandomizedBoonsEnabled,
            DestructibleAsUnlocks,
            FillerItemsDistribution,
        ],
    ),
    OptionGroup(
        "Location Options",
        [
            IncludeTormentMedaillonsChecks,
            IncludeSectionClearsWithWeaponsChecks,
            IncludeSectionClearsWithOutfitsChecks,
            IncludeSectionClearsWithSongsChecks,
            IncludeWeaponSkinsChecks,
            IncludeSecretMultiplierChecks,
            IncludeCoatOfArmsChecks,
            IncludeMiscellaneousChecks,
            IncludeFirstSlaughterChecks,
            IncludeFuryComboChecks,
            DestructibleLocationsEnabled,
            SingularDestructibleLocationsEnabled,
            HellsDestructibleLocationsEnabled,
        ],
    ),
]
