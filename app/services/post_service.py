from app.models.post import Post
from app.database import db_session

def get_all_posts():
	return Post.query.all()

def  create_new_post(data):
	post = Post(
		title=data['title'],
		body=data['body']
	)

	db_session.add(post)
	db_session.commit()

	return post
