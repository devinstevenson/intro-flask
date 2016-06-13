import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = u'DnfhKSYPnuKYK/Oqu56D6piX9bXan4XG5m35Mm9OeuM47sp+/rx3ALkNsnaxkVg2GXAQU1nQu/AjwwMTjRL+pQg=='
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
