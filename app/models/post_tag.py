from sqlalchemy import Table, Column, UUID, ForeignKey
from app.database import Base

post_tag = Table(
		'post_tag',
		Base.metadata,
		Column('post_id', UUID(as_uuid=True), ForeignKey('posts._id', ondelete='CASCADE'), primary_key=True),
		Column('tag_id', UUID(as_uuid=True), ForeignKey('tags._id', ondelete='CASCADE'), primary_key=True)
)
