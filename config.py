import os
from credentials import Credentials
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    BASIC_AUTH_USERNAME = Credentials.get_credentials()['basic_auth_username']
    BASIC_AUTH_PASSWORD = Credentials.get_credentials()['basic_auth_password']
    PROPAGATE_EXCEPTIONS = True
    BASIC_AUTH_FORCE = True
    SECRET_KEY = os.urandom(32)
    CSRF_ENABLE = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SQLALCHEMY_POOL_RECYCLE = 250