# third party
from dotenv import dotenv_values

import redis
import flask

# local
from src.config import app_config
from src.controller.CivilizationController import CivilizationController
from src.router.router import Router as Router
from src.services.DatabaseService import DatabaseService
from src.services.RedisService import RedisService
from src.services.RepositoryService import RepositoryService

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config.from_object(app_config["development"])
app.config.from_pyfile('src/config.py')

# load configuration
config = dotenv_values(".env")

print(config.get("REDIS_HOST"))

# initialise redis
r = redis.Redis(host=config.get("REDIS_HOST"), db=0)
redis_service = RedisService(r)

# initialise database repository
d = DatabaseService(host=config.get("SQLALCHEMY_DATABASE_URI"))
rs = RepositoryService(d)

# initialise controllers
civilization_c = CivilizationController(endpoint=config.get("API_DOMAIN"), redis_service=redis_service,
                                        repository_service=rs)

Router(app, civilization_c)

# comment out for docker run since its run by flask
app.run()
