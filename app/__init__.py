from flask import Flask
from app.scheduling import Scheduling

app = Flask(__name__)

scheduling = Scheduling()
scheduling.run()
