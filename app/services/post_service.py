from app.models.post import Post
from app.errors import ItemNotFoundError, ItemAlreadyExists
from app.database import db_session
import datetime as dt

def get_all():
	return Post.query.order_by(Post.created.desc()).all()

def get_one(_id):
	post = Post.query.get(_id)

	if not post:
		raise ItemNotFoundError(f'Post with id {_id} not found')
	
	return post

def create(data):
	post = Post(
		title=data['title'],
		body=data['body'],
		slug=data['title'].replace(' ', '-').lower(),
		updated=dt.datetime.now(),
		publish=dt.datetime.now()
	)

	db_session.add(post)
	db_session.commit()

	return post

def edit(data):
	Post.query.filter_by(_id=data['_id']).update(dict(
		title=data['title'],
		body=data['body'],
		slug=data['title'].replace(' ', '-').lower(),
		updated=dt.datetime.now(),
		publish=dt.datetime.now()
	))

	db_session.commit()

	post = Post.query.get(data['_id'])

	return post

def delete(_id):
	post = Post.query.get(_id)

	if not post:
		raise ItemNotFoundError(f'Post with id {_id} not found')

	db_session.delete(post)
	db_session.commit()
