import os


class BasicConfig:
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    TESTING = False


class DevelopmentConfig(BasicConfig):
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(os.getcwd(), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BasicConfig):
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'postgresql://cargamos:cargamos_password@db/cargamos'


class TestingConfig(BasicConfig):
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
