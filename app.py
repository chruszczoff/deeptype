from flask import Flask
from extensions import db, migrate
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicjalizacja rozszerzeń
    db.init_app(app)
    migrate.init_app(app, db)

    # Rejestracja blueprintów
    from routes import main_routes
    app.register_blueprint(main_routes)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)