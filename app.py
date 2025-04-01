from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Inicjalizacja rozszerzeń
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Konfiguracja aplikacji
    app.config.from_object('config.Config')
    
    # Inicjalizacja rozszerzeń z aplikacją
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import modeli (musi być po inicjalizacji db)
    with app.app_context():
        from models.user import User
        from models.match import Match
        from models.prediction import Prediction
    
    # Proste trasy testowe
    @app.route('/')
    def home():
        return "Aplikacja do typowania wyników piłkarskich działa poprawnie!"
    
    @app.route('/healthcheck')
    def healthcheck():
        return "OK", 200
    
    return app

# Utworzenie aplikacji
app = create_app()

if __name__ == '__main__':
    app.run()