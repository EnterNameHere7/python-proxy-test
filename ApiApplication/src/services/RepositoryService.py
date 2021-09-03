from src.models.database.civilization import CivilizationModel
from src.models.database.civilizationBonus import CivilizationBonusModel
from src.services.DatabaseService import DatabaseService


class RepositoryService:
    databaseService: DatabaseService

    def __init__(self, d: DatabaseService):
        self.databaseService = d

    def find_civilization_by_id(self, civ_id: int):
        session = self.databaseService.session_factory()
        query = session.query(CivilizationModel). \
            filter(CivilizationModel.id == civ_id)
        session.close()
        return query.all()

    def find_civilization_by_name(self, civ_name: str):
        session = self.databaseService.session_factory()
        query = session.query(CivilizationModel). \
            filter(CivilizationModel.name == civ_name)
        session.close()
        return query.all()

    def insert_into_database(self, model: any):
        session = self.databaseService.session_factory()
        session.add(model)
        session.commit()
        session.close()

    def find_civilization_bonus_by_civ_id(self, civ_id: int):
        session = self.databaseService.session_factory()
        query = session.query(CivilizationBonusModel). \
            filter(CivilizationBonusModel.civilization_id == civ_id)
        session.close()
        return query.all()
