from extensions import db
from models.match import Match
from datetime import datetime
import requests
from time import sleep
from flask import current_app

class APIFootballService:
    def __init__(self):
        self.base_url = current_app.config['API_FOOTBALL_URL']
        self.headers = {
            'x-rapidapi-key': current_app.config['API_FOOTBALL_KEY'],
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

    def update_matches(self, league_id=39, season=2023):
        """Pobiera i aktualizuje mecze z API"""
        try:
            url = f"{self.base_url}/fixtures"
            params = {'league': league_id, 'season': season}
            
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()

            updated_count = 0
            for fixture in data.get('response', []):
                updated_count += self._process_fixture(fixture)
                sleep(0.1)  # Ochrona przed rate limiting

            current_app.logger.info(f"Zaktualizowano {updated_count} meczów")
            return True

        except Exception as e:
            current_app.logger.error(f"Błąd podczas aktualizacji meczów: {str(e)}")
            return False

    def _process_fixture(self, fixture):
        """Przetwarza pojedynczy mecz z API"""
        try:
            fixture_data = fixture['fixture']
            teams_data = fixture['teams']
            score_data = fixture['score']['fulltime']
            
            match = Match.query.filter_by(api_match_id=fixture_data['id']).first()
            
            if not match:
                match = Match(api_match_id=fixture_data['id'])
                db.session.add(match)
            
            match.home_team = teams_data['home']['name']
            match.away_team = teams_data['away']['name']
            match.league = fixture['league']['name']
            match.match_date = datetime.strptime(fixture_data['date'], '%Y-%m-%dT%H:%M:%S%z')
            match.status = fixture_data['status']['short']
            
            if score_data['home'] is not None:
                match.home_score = score_data['home']
                match.away_score = score_data['away']
            
            db.session.commit()
            return 1
        
        except Exception as e:
            current_app.logger.error(f"Błąd przetwarzania meczu {fixture_data.get('id')}: {str(e)}")
            db.session.rollback()
            return 0