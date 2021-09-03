from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from src.services.DatabaseService import Base


class CivilizationModel(Base):
    __tablename__ = 'CIVILIZATION'

    id = Column(Integer, name="ID", primary_key=True)
    name = Column(String(60), name="NAME", index=False, unique=False)
    expansion = Column(String(60), name="EXPANSION", index=False, unique=False)
    team_bonus = Column(String(60), name="TEAM_BONUS", index=False)

    civilization_bonus = relationship("CivilizationBonusModel", back_populates="civilization")

    def __init__(self, civ_id: int = None, name: str = None, expansion: str = None, team_bonus: str = None):
        self.id = civ_id
        self.name = name
        self.expansion = expansion
        self.team_bonus = team_bonus

    def __repr__(self):
        return "<Civilization {}>".format(self.name)
