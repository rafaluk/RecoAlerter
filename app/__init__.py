from flask import Flask
from app.scheduling import Scheduling

def create_app():
    app = Flask(__name__)

    with app.app_context():
        scheduling = Scheduling()
        scheduling.run()
        return app
