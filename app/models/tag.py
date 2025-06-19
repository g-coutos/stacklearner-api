import uuid
import datetime as dt

from sqlalchemy import Column, UUID, String, DateTime
from sqlalchemy.orm import relationship
from app.models.post_tag import post_tag
from app.database import Base

class Tag(Base):
	__tablename__ = 'tags'
	
	_id = Column(UUID(as_uuid=True), primary_key=True)
	name = Column(String(50), unique=True, nullable=False)
	created = Column(DateTime)
	posts = relationship('Post', secondary=post_tag, back_populates='tags', passive_deletes=True)

	def __init__(self, name):
		self._id = uuid.uuid4()
		self.name = name
		self.created = dt.datetime.now()

	def __repr__(self):
		return f'{self.name}'
	
	def to_dict(self):
		return {
			"_id": self._id,
			'name': self.name,
			'created': self.created,
		}