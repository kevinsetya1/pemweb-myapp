# config.py

class Config:
    SECRET_KEY = 'P@ssw0rd'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:P%40ssw0rd@localhost/users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
