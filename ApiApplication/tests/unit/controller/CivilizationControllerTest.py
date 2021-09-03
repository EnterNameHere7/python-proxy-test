import unittest
from unittest import mock
from unittest.mock import patch

from src.models.api.civilization import CivilizationApiModel
# from src.models.database.civilization import CivilizationModel
from tests.stubs.repositoryservice import mocked_find_civilization_by_name, mocked_find_civilization_by_id
from tests.stubs.redisservice import mocked_get_value
from tests.stubs.requests import mocked_requests_get


class CivilizationControllerTest(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('src.services.RedisService.RedisService.get_value')
    @mock.patch('src.services.RepositoryService.RepositoryService')
    def test_fetch_civilization_by_name_from_redis_successfully(self, mocked_requests, mocked_redis_service,
                                                                mocked_repository_service):
        # redis mocks
        mocked_redis_service.get_value = mocked_get_value

        from src.controller.CivilizationController import CivilizationController
        civ_controller = CivilizationController(endpoint="test-name",
                                                redis_service=mocked_redis_service,
                                                repository_service=mocked_repository_service)

        response = civ_controller.fetch_and_load_all_civilizations()

        self.assertEqual("{\"civilizations\": [{\"id\": 1, \"name\": \"test-name\", \"expansion\": "
                         "\"test-expansion\", \"team_bonus\": \"team_bonus\", \"civ_bonus\": []}]}", response)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('src.services.RedisService.RedisService.get_value')
    @mock.patch('src.services.RepositoryService.RepositoryService')
    def test_fetch_civilization_by_name_from_api_successfully(self, mocked_requests, mocked_redis_service,
                                                              mocked_repository_service):
        # redis mocks
        mocked_redis_service.get_value = mocked_get_value

        from src.controller.CivilizationController import CivilizationController
        civ_controller = CivilizationController(endpoint="test-name",
                                                redis_service=mocked_redis_service,
                                                repository_service=mocked_repository_service)

        response = civ_controller.fetch_civilization_by_name("test-object-name")

        self.assertEqual("test-name", response.name)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('src.services.RedisService.RedisService.get_value')
    @mock.patch('src.services.RepositoryService.RepositoryService')
    def test_invalid_name_from_api_successfully(self, mocked_requests, mocked_redis_service,
                                                              mocked_repository_service):
        # redis mocks
        mocked_redis_service.get_value = mocked_get_value

        # database mock
        mocked_repository_service.find_civilization_by_name = mocked_find_civilization_by_name

        from src.controller.CivilizationController import CivilizationController
        civ_controller = CivilizationController(endpoint="test-name",
                                                redis_service=mocked_redis_service,
                                                repository_service=mocked_repository_service)

        response = civ_controller.fetch_civilization_by_name("test-name-skip-all")

        self.assertEqual("Couldn't find civilization by name", response.error_message)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('src.services.RedisService.RedisService.get_value')
    @mock.patch('src.services.RepositoryService.RepositoryService.find_civilization_by_name')
    def test_fetch_civilization_by_name_from_DB_successfully(self, mocked_requests, mocked_redis_service,
                                                             mocked_repository_service):
        # redis mocks
        mocked_redis_service.get_value = mocked_get_value

        # database mock
        mocked_repository_service.find_civilization_by_name = mocked_find_civilization_by_name

        from src.controller.CivilizationController import CivilizationController
        civ_controller = CivilizationController(endpoint="test-name-skip-redis",
                                                redis_service=mocked_redis_service,
                                                repository_service=mocked_repository_service)

        response = civ_controller.fetch_and_load_all_civilizations()

        self.assertEqual("{\"civilizations\": [{\"id\": 1, \"name\": \"test-name-skip-redis\", \"expansion\": "
                         "\"test-expansion\", \"team_bonus\": \"team_bonus\", \"civ_bonus\": []}]}", response)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('src.services.RedisService.RedisService.get_value')
    @mock.patch('src.services.RepositoryService.RepositoryService')
    def test_insert_civilization_successfully(self, mocked_requests, mocked_redis_service,
                                              mocked_repository_service):
        # redis mocks
        mocked_redis_service.get_value = mocked_get_value

        # database mock
        mocked_repository_service.find_civilization_by_name = mocked_find_civilization_by_name
        mocked_repository_service.find_civilization_by_id = mocked_find_civilization_by_id

        from src.controller.CivilizationController import CivilizationController
        civ_controller = CivilizationController(endpoint="test-name-skip-all",
                                                redis_service=mocked_redis_service,
                                                repository_service=mocked_repository_service)

        response = civ_controller.fetch_and_load_all_civilizations()

        self.assertEqual("{\"civilizations\": [{\"id\": 0, \"name\": \"test-name-skip-all\", \"expansion\": "
                         "\"test-expansion\", \"team_bonus\": \"team_bonus\", \"civ_bonus\": []}]}", response)


if __name__ == '__main__':
    unittest.main()
