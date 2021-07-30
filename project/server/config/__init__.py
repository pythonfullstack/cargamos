import os

basedir = os.getcwd()


class BasicConfig:
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    TESTING = False


class DevelopmentConfig(BasicConfig):
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BasicConfig):
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'mysql://dt_admin:dt2016@localhost/dreamteam_db'


class TestingConfig(BasicConfig):
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
