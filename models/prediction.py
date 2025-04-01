from app import db

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    home_prediction = db.Column(db.Integer, nullable=False)
    away_prediction = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Prediction {self.home_prediction}-{self.away_prediction}>'