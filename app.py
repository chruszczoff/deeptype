from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Konfiguracja
    app.config.from_object('config.Config')
    
    # Sprawdzenie czy URI bazy danych jest poprawne
    if not app.config['SQLALCHEMY_DATABASE_URI']:
        raise ValueError("Nie skonfigurowano SQLALCHEMY_DATABASE_URI")
    
    # Inicjalizacja rozszerzeń
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Proste endpointy
    @app.route('/')
    def home():
        return "Aplikacja do typowania wyników piłkarskich działa poprawnie!"
    
    @app.route('/healthcheck')
    def healthcheck():
        return "OK", 200
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run()