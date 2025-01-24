import os
from dotenv import load_dotenv

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

load_dotenv()

engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	from app.models import post
	Base.metadata.create_all(bind=engine)

def init_app(app: Flask):
	@app.teardown_appcontext
	def shutdown_session(exception=None):
		db_session.remove()
