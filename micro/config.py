import logging


class EnvironmentConfig:
    """ Base class for config that is shared between environments """
    LOG_DIR = 'logs'


class ProdConfig(EnvironmentConfig):
    """ Production Environment Config """
    LOG_LEVEL = logging.ERROR


class DevConfig(EnvironmentConfig):
    """ Production Environment Config """
    API_DOCS_URL = 'http://localhost:5000/api-docs/swagger-ui-v2/index.html?url=http://localhost:5000/api/docs'
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = 'postgresql://flaskgis:fubarfubar42@pmligvvl3on8j3.cdgmafxlcggw.us-east-2.rds.amazonaws.com/MyDatabase'
