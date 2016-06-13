import os

class BaseConfig(object):
    DEBUG = False
    # SECRET_KEY = u'DnfhKSY3ALkNsnaxkVg2GXAQU1nQu/AjwwMTjRL+pQg=='
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
