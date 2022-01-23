"""Temp file used for testing new logic system."""
import random

import pytest

from randomizer.Fill import Generate_Spoiler
from randomizer.Settings import Settings
from randomizer.Spoiler import Spoiler


@pytest.fixture
def generate_settings():
    # Setting test settings
    data = {}
    data["seed"] = random.randint(0, 100000000)
    # important things
    data["shuffle_levels"] = True
    data["blocker_0"] = 0
    data["blocker_1"] = 0
    data["blocker_2"] = 0
    data["blocker_3"] = 0
    data["blocker_4"] = 0
    data["blocker_5"] = 0
    data["blocker_6"] = 0
    data["blocker_7"] = 100
    data["troff_0"] = 100
    data["troff_1"] = 100
    data["troff_2"] = 100
    data["troff_3"] = 100
    data["troff_4"] = 100
    data["troff_5"] = 100
    data["troff_6"] = 100

    data["unlock_all_moves"] = False
    data["unlock_all_kongs"] = False
    data["crown_door_open"] = False
    data["coin_door_open"] = False
    data["unlock_fairy_shockwave"] = False
    data["krool_phase_count"] = 4

    # not important things
    data["download_json"] = True

    data["music_bgm"] = True
    data["music_fanfares"] = True
    data["music_events"] = True

    data["generate_spoilerlog"] = True
    data["fast_start_beginning_of_game"] = False
    data["fast_start_hideout_helm"] = False
    data["quality_of_life"] = True
    data["enable_tag_anywhere"] = False
    data["random_krool_phase_order"] = True
    return data


def test_forward(generate_settings):
    generate_settings["algorithm"] = "forward"
    settings = Settings(generate_settings)
    settings.shuffle_items = False
    settings.shuffle_loading_zones = "all"
    settings.decoupled_loading_zones = True
    spoiler = Spoiler(settings)
    Generate_Spoiler(spoiler)
    spoiler.toJson()


def test_assumed(generate_settings):
    generate_settings["algorithm"] = "assumed"
    settings = Settings(generate_settings)
    spoiler = Spoiler(settings)
    try:
        Generate_Spoiler(spoiler)
        spoiler.toJson()
    except Exception:
        pass