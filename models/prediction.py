from app import db
from datetime import datetime

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    home_pred = db.Column(db.Integer, nullable=False)
    away_pred = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def calculate_points(self, actual_home, actual_away):
        # Prosty system punktacji
        if self.home_pred == actual_home and self.away_pred == actual_away:
            self.points = 3
        elif (self.home_pred - self.away_pred) == (actual_home - actual_away):
            self.points = 1
        else:
            self.points = 0
        db.session.commit()