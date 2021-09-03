import jsonpickle

from src.models.api.civilization import CivilizationApiModel


def mocked_get_value(key):
    if key == "C-NAME-test-name" or key == "C-ID-1":
        return jsonpickle.encode(CivilizationApiModel(id=1, name="test-name",
                                                      expansion="test-expansion",
                                                      team_bonus="team_bonus",
                                                      civ_bonus=[]), unpicklable=False)
    elif key == "C-NAME-test-object-name":
        return "{\"py/object\": \"src.models.api.civilization.CivilizationApiModel\",\"id\": 1,\"name\": \"test-name\"," \
               "\"expansion\": \"test-expansion\",\"team_bonus\": \"team_bonus\",\"civ_bonus\": []}"
    elif key == "C-NAME-test-name-skip-redis" or key == "C-ID-0":
        return None
