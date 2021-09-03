from dotenv import dotenv_values


class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    config = dotenv_values("../.env")

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI")


app_config = {
    'development': DevelopmentConfig
}
