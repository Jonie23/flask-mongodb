import os


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')

    MONGODB_SETTINGS = {'db': 'students'}


'''
class Config(object):
    DEBUG = False
    TESTING = False
   

SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

# IMAGE_UPLOADS = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True

# this class inherits the config class


class ProductionConfig(Config):
   
    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

# never run debug=true in a production environment


class DevelopmentConfig(Config):
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"
    

    MONGODB_DB = "development-db"
    MONGODB_USERNAME = "enrollment-app"
    MONGODB_PASSWORD = "pwd123"
    

    DEBUG = True


class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False

    '''
