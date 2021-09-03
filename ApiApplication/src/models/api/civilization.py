class CivilizationApiModel(object):
    id = int
    name = str
    expansion = str
    team_bonus = str
    civ_bonus = []

    def __init__(self, id: int, name: str, expansion: str, team_bonus: str, civ_bonus: []):
        self.id = id
        self.name = name
        self.expansion = expansion
        self.team_bonus = team_bonus
        self.civ_bonus = civ_bonus
