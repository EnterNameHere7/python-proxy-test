from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class DatabaseService:
    engine: object
    _sessionFactory: object
    base: object

    def __init__(self, host: str):
        self.engine = create_engine(host)
        self._sessionFactory = sessionmaker(bind=self.engine)
        self.base = declarative_base()

    def session_factory(self):
        self.base.metadata.create_all(self.engine)
        return self._sessionFactory()
