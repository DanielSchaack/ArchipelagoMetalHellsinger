from collections.abc import Mapping
from typing import Any

from BaseClasses import Tutorial
from Options import Option
from rule_builder.cached_world import CachedRuleBuilderWorld
from worlds.AutoWorld import WebWorld
from worlds.metal_hellsinger.items import MetalHellsingerItem
from worlds.metal_hellsinger.locations import location_region_mapping

from . import items, locations, regions, rules
from .options import MetalHellsingerOptions, option_groups


class MetalHellsingerWebWorld(WebWorld):
    game = "Metal: Hellsinger"
    theme = "partyTime"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Metal: Hellsinger for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Schaackii"],
    )
    tutorials = [setup_en]
    option_groups = option_groups


class MetalHellsingerWorld(CachedRuleBuilderWorld):
    """
    Metal: Hellsinger is a rhythm FPS, where your ability to shoot on the beat will enhance your gameplay experience.
    The more in sync you are with the rhythm, the more intense the music will become and the more destruction you will cause.
    """
    game = "Metal: Hellsinger"
    origin_region_name = "Global"
    options_dataclass = MetalHellsingerOptions
    options: MetalHellsingerOptions

    item_name_to_id = items.item_name_to_id
    location_name_to_id = locations.location_name_to_id

    item_name_groups = items.item_name_groups
    location_name_groups = locations.location_name_groups

    ut_can_gen_without_yaml = True
    glitches_item_name = "Out of Logic"

    web = MetalHellsingerWebWorld()

    def generate_early(self) -> None:
        if not self.player_name.isascii():
            raise Exception("Metal: Hellsingers yaml's slot name has invalid character(s).")

        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]
            slot_options: dict[str, Any] = slot_data.get("options", {})
            for key, value in slot_options.items():
                opt: Option|None = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def create_item(self, name: str) -> MetalHellsingerItem:
        return items.create_item(self, name)

    def create_items(self) -> None:
        items.create_all_items(self)
        locations.create_events(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def get_filler_item_name(self) -> str:
        if self.options.filler_items_distribution.weights_pair:
            return items.create_random_items( self, self.options.filler_items_distribution.weights_pair, 1)[0]
        return items.create_random_items( self, self.options.filler_items_distribution.default, 1)[0]

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "options": self.options.as_dict(
                "win_condition",
                "required_hells_completion",
                "regressive_difficulty",
                "starting_difficulty",
                "include_archdevil_difficulty",
                "minimal_difficulty",
                "hells_unlocks_as_progressive",
                "require_aspect_for_boss_arena",
                "starting_hells",
                "randomized_torments_enabled",
                "torment_unlocks_as_progressive",
                "require_stage_for_torments",
                "require_weapons_for_torments",
                # "randomized_levels_enabled",
                "require_no_tomorrow_for_sheol",
                "require_coat_of_arms_for_sheol",
                "required_coat_of_arms_for_sheol",
                "archdevil_enemies_enabled",
                "randomized_boons_enabled",
                "randomized_dash_enabled",
                "randomized_jump_enabled",
                "randomized_reload_enabled",
                "randomized_weapon_ultimates_enabled",
                "randomized_slaughter_enabled",
                "destructible_as_unlocks",
                "starting_weapon",
                "include_dream_of_the_beast_weapon",
                "include_purgatory_weapon",
                "include_additional_weapon_variants",
                "randomized_outfits_enabled",
                "starting_outfit",
                "include_dream_of_the_beast_outfits",
                "include_purgatory_outfits",
                "randomized_songs_enabled",
                "starting_main_song",
                "starting_boss_song",
                "include_dream_of_the_beast_songs",
                "include_purgatory_songs",
                "include_essential_hits_soundtrack_songs",
                "include_dusk_soundtrack_songs",
                "filler_items_distribution",
                "include_coat_of_arms_checks",
                "torment_medaillons_enabled",
                "include_secret_multiplier_checks",
                "include_randomized_weapon_skins_checks",
                "include_section_clears_with_weapons_checks",
                "include_section_clears_with_outfits_checks",
                "include_section_clears_with_songs_checks",
                "include_progressive_anguish_gate_skips",
                "destructible_locations_enabled",
                "singular_destructible_locations_enabled",
                "hells_destructible_locations_enabled",
                "include_miscellaneous_checks",
                "include_first_slaughter_checks",
                "include_fury_combo_checks",
            )
        }

    def custom_ut_sort(self, region_label: str, location_label: str) -> str:
        if region_label == "Global":
            region_priority = 0
        elif region_label.startswith("Weapon"):
            region_priority = 1
        elif region_label.startswith("Outfit"):
            region_priority = 2
        elif region_label.startswith("Song"):
            region_priority = 3
        elif region_label.startswith("Tutorial"):
            region_priority = 40
        elif region_label.startswith("Voke"):
            region_priority = 41
        elif region_label.startswith("Stygia"):
            region_priority = 42
        elif region_label.startswith("Yhelm"):
            region_priority = 43
        elif region_label.startswith("Incaustis"):
            region_priority = 44
        elif region_label.startswith("Gehenna"):
            region_priority = 45
        elif region_label.startswith("Nihil"):
            region_priority = 46
        elif region_label.startswith("Acheron"):
            region_priority = 47
        elif region_label.startswith("Sheol"):
            region_priority = 48
        else:
            region_priority = 5

        loc_data = location_region_mapping.get(region_label, {}).get(location_label)
        loc_id = loc_data.id if loc_data is not None else 99999999

        return f"{region_priority:02d}_{region_label}_{loc_id:08d}"
