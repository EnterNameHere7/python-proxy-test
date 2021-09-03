from sqlalchemy import Column, String, Integer, ForeignKey

from src.models.database.civilization import CivilizationModel
from src.services.DatabaseService import Base
from sqlalchemy.orm import relationship


class CivilizationBonusModel(Base):
    __tablename__ = 'CIVILIZATION_BONUS'

    bonus_id = Column(Integer, name="BONUS_ID", primary_key=True, autoincrement=True)
    bonus_description = Column(String(60), name="BONUS_DISCRIPTION", index=False, unique=False)

    civilization_id = Column(Integer, ForeignKey('CIVILIZATION.ID'))
    civilization = relationship("CivilizationModel", back_populates="civilization_bonus")

    def __init__(self, civilization: CivilizationModel, bonus_description: str):
        self.civilization = civilization
        self.bonus_description = bonus_description


