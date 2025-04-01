from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

migrate = Migrate(app, db)
app = Flask(__name__)
app.config.from_object('config.Config')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from models.user import User
from models.match import Match
from models.prediction import Prediction

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)