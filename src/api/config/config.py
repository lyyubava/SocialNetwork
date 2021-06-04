class Configuration:
    DB_USER = None  # provide db username!
    DB_HOST = None  # provide db hostname!
    DB_PASSWORD = None  # provide password!
    # and last but not least
    DB_NAME = None  # provide name of your db

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'some-secret-string'
    DEBUG = True
