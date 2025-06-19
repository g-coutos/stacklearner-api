from dotenv import load_dotenv

from flask import Flask
from flask_session import Session
from flask_cors import CORS
from . import database, config
from app import controllers
import os

load_dotenv()

def create_app():
	app = Flask(__name__)
	app.config.from_object(config.Config)

	Session(app)
	CORS(
		app, 
		origins=[os.getenv("WEB_HOST")], 
		supports_credentials=True,
		methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"]
	)

	database.init_db()
	database.init_app(app)

	for bp in controllers.blueprints:
		app.register_blueprint(bp)

	return app