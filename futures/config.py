import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'trades.db')
    SQLALCHEMY_BINDS = {
        'variables_db': 'sqlite:///' + os.path.join(basedir, 'variables.db'),
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
