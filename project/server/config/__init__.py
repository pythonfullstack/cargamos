import os


class BasicConfig:
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BasicConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'


class ProductionConfig(BasicConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://cargamos:cargamos_password@db:5432/cargamos'


class TestingConfig(BasicConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
