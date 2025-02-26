from dotenv import load_dotenv

from flask import Flask
from flask_session import Session
from flask_cors import CORS, cross_origin
from . import database, config
from app import controllers

load_dotenv()

def create_app():
	app = Flask(__name__)
	app.config.from_object(config.Config)

	Session(app)
	CORS(app, supports_credentials=True)
	
	database.init_db()
	database.init_app(app)

	for bp in controllers.blueprints:
		app.register_blueprint(bp)

	return app