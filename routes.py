from flask import Blueprint, render_template, redirect, url_for, flash, request
from extensions import db
from models.match import Match
from services.api_football import APIFootballService

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return render_template('index.html')

@main_routes.route('/matches')
def matches():
    matches = Match.query.order_by(Match.match_date).all()
    return render_template('matches.html', matches=matches)

@main_routes.route('/update-matches', methods=['POST'])
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
    return redirect(url_for('main.matches'))