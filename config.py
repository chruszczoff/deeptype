import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key-123456')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', '').replace('postgres://', 'postgresql://') or 'postgresql:///deeptype'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_FOOTBALL_KEY = os.getenv('API_FOOTBALL_KEY')
    API_FOOTBALL_URL = 'https://v3.football.api-sports.io'