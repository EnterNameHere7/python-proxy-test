import json
import jsonpickle

import requests
from src.services.RedisService import RedisService
from src.services.RepositoryService import RepositoryService

from src.models.api.civilization import CivilizationApiModel
from src.models.api.error import Error

from src.models.database.civilization import CivilizationModel
from src.models.database.civilizationBonus import CivilizationBonusModel


class CivilizationController:

    def __init__(self,
                 endpoint: str,
                 redis_service: RedisService,
                 repository_service: RepositoryService
                 ) -> None:
        self.endpoint = endpoint
        self.redis_service = redis_service
        self.repository_service = repository_service

    def fetch_and_load_all_civilizations(self) -> str:
        response = requests.get(url=f"{self.endpoint}/api/v1/civilizations")
        civilizations_json = json.loads(response.text)

        json_value = []
        for civ in civilizations_json["civilizations"]:
            try:
                value = self.fetch_civilization_by_name(civ['name'])
                if isinstance(value, Error):
                    value = self.fetch_civilization_by_id(civ['id'])
                    if isinstance(value, Error):
                        civ_model = CivilizationModel(
                            civ_id=civ["id"],
                            name=civ["name"],
                            expansion=civ["expansion"],
                            team_bonus=civ['team_bonus']
                        )

                        # CivilizationModel.insert_into_database(civ_model)
                        bonuses = []
                        if not civ["civilization_bonus"]:
                            self.repository_service.insert_into_database(civ_model)
                        else:
                            for bonus in civ["civilization_bonus"]:
                                bonuses.append(bonus)
                                self.repository_service.insert_into_database(CivilizationBonusModel(civ_model, bonus))

                        json_str = CivilizationApiModel(id=civ['id'], name=civ['name'], expansion=civ['expansion'],
                                                        team_bonus=civ['team_bonus'],
                                                        civ_bonus=bonuses)

                        json_value.append(json_str)
                        self.redis_service.set_key_value(key=f"C-ID-{civ['id']}", value=jsonpickle.encode(json_str))
                        self.redis_service.set_key_value(key=f"C-NAME-{civ['name']}", value=jsonpickle.encode(json_str))
                        continue

                json_value.append(value)
            except Exception as e:
                print(e)

        return jsonpickle.encode({'civilizations': json_value}, unpicklable=False)

    def fetch_civilization_by_id(self, civ_id: int) -> object:
        value = self.redis_service.get_value(key=f"C-ID-{civ_id}")
        if value is None:
            value = self.repository_service.find_civilization_by_id(civ_id)
            if not value:
                return Error("Couldn't find civilization by name")
            else:
                for row in value:
                    bonuses = []
                    for bonus in self.repository_service.find_civilization_bonus_by_civ_id(row.id):
                        bonuses.append(bonus.bonus_description)

                    civ_model = CivilizationApiModel(id=row.id, name=row.name, expansion=row.expansion,
                                                     team_bonus=row.team_bonus, civ_bonus=bonuses)

                    self.redis_service.set_key_value(key=f"C-ID-{civ_id}", value=jsonpickle.encode(civ_model))
                    return civ_model
        else:
            value = jsonpickle.decode(value)
        return value

    def fetch_civilization_by_name(self, civ_name: str) -> object:
        value = self.redis_service.get_value(key=f"C-NAME-{civ_name}")
        if value is None:
            value = self.repository_service.find_civilization_by_name(civ_name)
            if not value:
                return Error("Couldn't find civilization by name")
            else:
                for row in value:
                    bonuses = []
                    for bonus in self.repository_service.find_civilization_bonus_by_civ_id(row.id):
                        bonuses.append(bonus.bonus_description)

                    civ_model = CivilizationApiModel(id=row.id, name=row.name, expansion=row.expansion,
                                                     team_bonus=row.team_bonus, civ_bonus=bonuses)

                    self.redis_service.set_key_value(key=f"C-NAME-{civ_name}", value=jsonpickle.encode(civ_model))
                    return civ_model
        else:
            value = jsonpickle.decode(value)

        return value
