import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', u'DnfhKSY3ALkNsnaxkVg2GXAQU1nQu/AjwwMTjRL+pQg==')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///:memory:')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
