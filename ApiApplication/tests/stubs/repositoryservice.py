from src.models.api.civilization import CivilizationApiModel
from src.models.database.civilization import CivilizationModel
from src.models.database.civilizationBonus import CivilizationBonusModel


def mocked_find_civilization_by_name(name: str):
    if name == "test-name-skip-redis":
        return [CivilizationModel(civ_id=1, name="test-name-skip-redis", team_bonus="team_bonus",
                                  expansion="test-expansion")]
    elif name == "test-name-skip-all":
        return []


def mocked_find_civilization_by_id(civ_id: int):
    if civ_id == 1:
        return [CivilizationModel(civ_id=1, name="test-name-skip-redis", team_bonus="team_bonus",
                                  expansion="test-expansion")]
    elif civ_id == 0:
        return []


def find_civilization_bonus_by_civ_id(civ_id: int):
    if civ_id == 1:
        return [CivilizationBonusModel(
            civilization=CivilizationModel(civ_id=1, name="test-name-skip-redis", team_bonus="team_bonus",
                                           expansion="test-expansion"), bonus_description="test-desc")]
