import uuid
import datetime as dt

from sqlalchemy import Column, UUID, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

from .post_tag import post_tag

class Post(Base):
	__tablename__ = 'posts'

	_id = Column(UUID(as_uuid=True), primary_key=True)
	title = Column(String(100))
	body = Column(String)
	slug = Column(String(100))
	publish = Column(DateTime)
	created = Column(DateTime)
	updated = Column(DateTime)
	tags = relationship('Tag', secondary=post_tag, back_populates='posts', passive_deletes=True)

	def __init__(self, title, body, slug, updated, publish, tags):
		self._id = uuid.uuid4()
		self.title = title
		self.body = body
		self.slug = slug
		self.created = dt.datetime.now()
		self.updated = updated
		self.publish = publish
		self.tags = tags

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
			'updated': self.updated,
			'tags': [tag.to_dict() for tag in self.tags]
		}