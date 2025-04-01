from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from services.api_football import APIFootballService
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.secret_key = app.config['SECRET_KEY']

    db.init_app(app)
    migrate.init_app(app, db)

    # Import modeli
    from models.user import User
    from models.match import Match
    from models.prediction import Prediction

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/matches')
    def matches():
        matches = Match.query.order_by(Match.match_date).all()
        return render_template('matches.html', matches=matches)

    @app.route('/update-matches', methods=['POST'])
    def update_matches():
        if request.method == 'POST':
            try:
                service = APIFootballService()
                success = service.update_matches()
                if success:
                    flash('Mecze zostały zaktualizowane!', 'success')
                else:
                    flash('Błąd podczas aktualizacji meczów', 'danger')
            except Exception as e:
                flash(f'Błąd: {str(e)}', 'danger')
        return redirect(url_for('matches'))

    return app

app = create_app()