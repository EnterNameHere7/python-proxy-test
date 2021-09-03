class Civilizations(object):
    civilizations: []

    def __init__(self, civilizations: []):
        self.civilizations = civilizations


class Civilization(object):
    id: int
    name: str
    expansion: str
    team_bonus: str
    civilization_bonus: []

    def __init__(self, id: int, name: str, expansion: str, team_bonus: str, civilization_bonus: []):
        self.id = id
        self.name = name
        self.expansion = expansion
        self.team_bonus = team_bonus
        self.civilization_bonus = civilization_bonus
