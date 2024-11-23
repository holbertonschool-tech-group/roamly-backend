import os

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://pass:1212@localhost/roamlydb')
    DEBUG = True

class ProductionConfig(BaseConfig):

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@host/db')
    DEBUG = False

class TestingConfig(BaseConfig):

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://dev_user:dev_password@localhost/dev_db')
    TESTING = True

def get_config(env):

    if env == 'development':
        return DevelopmentConfig
    elif env == 'production':
        return ProductionConfig
    elif env == 'testing':
        return TestingConfig
    else:
        raise ValueError(f"Unknown environment: {env}")
