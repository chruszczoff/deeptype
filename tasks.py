from app import create_app
from services.api_football import APIFootballService

app = create_app()
with app.app_context():
    service = APIFootballService()
    service.update_matches()