import os
class Configuration:
    DB_USER = 'root'
    DB_HOST = 'db'
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_NAME = 'SN'

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'some-secret-string'
    DEBUG = True
