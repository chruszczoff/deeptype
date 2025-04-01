from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

# Inicjalizacja rozszerzeń
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Konfiguracja aplikacji
    app.config.from_object('config.Config')
    
    # Inicjalizacja rozszerzeń z aplikacją
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    # Rejestracja blueprintów (możesz dodać później)
    # from .auth import auth_blueprint
    # app.register_blueprint(auth_blueprint)
    
    # Import modeli (musi być po inicjalizacji db)
    from models.user import User
    from models.match import Match
    from models.prediction import Prediction
    
    # Prosta trasa testowa
    @app.route('/')
    def home():
        return "Aplikacja do typowania wyników piłkarskich działa poprawnie!"
    
    return app

# Utworzenie aplikacji
app = create_app()

if __name__ == '__main__':
    app.run()