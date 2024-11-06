# app/config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://pass:1212@localhost:5432/roamly')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
