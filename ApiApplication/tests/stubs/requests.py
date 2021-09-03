import jsonpickle

from tests.models.Civilization import Civilization, Civilizations


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

        def text(self):
            return self.text

    if kwargs["url"] == 'test-name/api/v1/civilizations':
        test_civ = Civilization(id=1, name="test-name", team_bonus="team_bonus", expansion="test-expansion",
                                civilization_bonus=[])
        return MockResponse(jsonpickle.encode(Civilizations([test_civ]), unpicklable=False), 200)
    elif kwargs["url"] == 'test-id/api/v1/civilizations' or kwargs[
        "url"] == 'test-name-skip-redis/api/v1/civilizations':
        test_civ = Civilization(id=1, name="test-name-skip-redis", team_bonus="team_bonus", expansion="test-expansion",
                                civilization_bonus=[])
        return MockResponse(jsonpickle.encode(Civilizations([test_civ]), unpicklable=False), 200)
    elif kwargs["url"] == 'test-name-skip-all/api/v1/civilizations':
        test_civ = Civilization(id=0, name="test-name-skip-all", team_bonus="team_bonus", expansion="test-expansion",
                                civilization_bonus=[])
        return MockResponse(jsonpickle.encode(Civilizations([test_civ]), unpicklable=False), 200)

    return MockResponse(None, 404)
