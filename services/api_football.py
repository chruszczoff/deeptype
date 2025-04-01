import requests
from app import app
from models.match import Match
from datetime import datetime

class APIFootballService:
    def __init__(self):
        self.base_url = app.config['API_FOOTBALL_URL']
        self.headers = {
            'x-rapidapi-key': app.config['API_FOOTBALL_KEY'],
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }

    def get_fixtures(self, league_id, season):
        url = f"{self.base_url}/fixtures"
        params = {
            'league': league_id,
            'season': season
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def update_matches(self, league_id, season):
        data = self.get_fixtures(league_id, season)
        fixtures = data.get('response', [])
        
        for fixture in fixtures:
            match_data = fixture['fixture']
            teams_data = fixture['teams']
            league_data = fixture['league']
            score_data = fixture['score']
            
            match = Match.query.filter_by(api_match_id=fixture['fixture']['id']).first()
            
            if not match:
                match = Match(api_match_id=fixture['fixture']['id'])
            
            match.home_team = teams_data['home']['name']
            match.away_team = teams_data['away']['name']
            match.league = league_data['name']
            match.match_date = datetime.strptime(match_data['date'], '%Y-%m-%dT%H:%M:%S%z')
            match.status = match_data['status']['short']
            
            if score_data['fulltime']['home'] is not None:
                match.home_score = score_data['fulltime']['home']
                match.away_score = score_data['fulltime']['away']
            
            db.session.add(match)
        
        db.session.commit()
        return len(fixtures)