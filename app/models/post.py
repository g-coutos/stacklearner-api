import uuid
import datetime as dt

from sqlalchemy import Column, UUID, String, DateTime
from app.database import Base

class Post(Base):
	__tablename__ = 'posts'

	_id = Column(UUID, primary_key=True)
	title = Column(String(100), unique=True)
	body = Column(String)
	slug = Column(String(100), unique=True)
	publish = Column(DateTime)
	created = Column(DateTime)
	updated = Column(DateTime)

	def __init__(self, title, body, slug, updated, publish):
		self._id = uuid.uuid4()
		self.title = title
		self.body = body
		self.slug = slug
		self.created = dt.datetime.now()
		self.updated = updated
		self.publish = publish

	def __repr__(self):
		return f'{self.title}'

	def to_dict(self):
		return {
			"_id": self._id,
			'title': self.title,
			'body': self.body,
			'slug': self.slug,
			'publish': self.publish,
			'created': self.created,
			'updated': self.updated
		}