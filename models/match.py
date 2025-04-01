from app import db

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_match_id = db.Column(db.Integer, unique=True)
    home_team = db.Column(db.String(100), nullable=False)
    away_team = db.Column(db.String(100), nullable=False)
    league = db.Column(db.String(100))
    match_date = db.Column(db.DateTime)
    home_score = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
    status = db.Column(db.String(50))
    predictions = db.relationship('Prediction', backref='match', lazy=True)

    def __repr__(self):
        return f'<Match {self.home_team} vs {self.away_team}>'