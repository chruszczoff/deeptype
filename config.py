import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost/soccer_predictions')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_FOOTBALL_KEY = os.getenv('API_FOOTBALL_KEY')
    API_FOOTBALL_URL = 'https://v3.football.api-sports.io'