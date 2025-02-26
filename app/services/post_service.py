from app.models.post import Post
from app.errors import ItemNotFoundError, ItemAlreadyExists
from app.database import db_session

def get_all():
	return Post.query.order_by(Post.created.desc()).all()

def  create(data):
	post = Post(
		title=data['title'],
		body=data['body']
	)

	db_session.add(post)
	db_session.commit()

	return post

def delete(_id):
	post = Post.query.get(_id)

	if not post:
		raise ItemNotFoundError(f'Post with id {_id} not found')

	db_session.delete(post)
	db_session.commit()
