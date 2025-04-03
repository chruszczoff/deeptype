from flask import Blueprint, render_template

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return render_template('index.html', title='Strona główna')

@main_routes.route('/matches')
def matches():
    test_matches = [
        {'home_team': 'Team A', 'away_team': 'Team B', 'date': '2023-01-01'},
        {'home_team': 'Team C', 'away_team': 'Team D', 'date': '2023-01-02'}
    ]
    return render_template('matches.html', matches=test_matches)