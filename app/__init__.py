from dotenv import load_dotenv

from flask import Flask
from . import database, config
from app import controllers

load_dotenv()

def create_app():
	app = Flask(__name__)
	app.config.from_object(config.Config)
	
	database.init_db()
	database.init_app(app)

	for bp in controllers.blueprints:
		app.register_blueprint(bp)

	return app