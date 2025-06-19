from app.models.post import Post
from app.errors import PaginationValueError, ItemNotFoundError, ItemAlreadyExists
from app.database import db_session

from .tag_service import get_or_create

import datetime as dt
from math import ceil

def get_all(page):
	posts = Post.query.order_by(Post.created.desc()).all()

	pagination_limit = 15
	posts_total = len(posts)
	pages_total = ceil(posts_total / pagination_limit)
	
	if posts_total < pagination_limit or page == None:
		return {
			'posts': posts,
		}
	
	page = int(page)
	
	if page <= 0:
		raise PaginationValueError("Page param can't be negative or zero")
	
	if page > pages_total:
		raise PaginationValueError("This page does not exist")
	
	paginated_posts = posts[(page - 1) * pagination_limit:page * pagination_limit]
	
	if not (page * pagination_limit) < posts_total:
		paginated_posts = posts[(page - 1) * pagination_limit:page * len(posts)]

	return {
		'posts': paginated_posts,
		'posts_total': posts_total,
		'pages_total': pages_total,
		'page': page,
		'has_previus_page': page > 1,
		'has_next_page': (page * pagination_limit) < posts_total,
	}

def get_one(_id):
	post = Post.query.get(_id)

	if not post:
		raise ItemNotFoundError(f'Post with id {_id} not found')
	
	return post

def get_all_by_tag(tag):
	posts = Post.query.filter(Post.tags.any(name=tag)).order_by(Post.created.desc()).all()

	return {
		'posts': posts,
	}

def create(data):
	post = Post.query.filter_by(title=data['title']).first()

	if post:
		raise ItemAlreadyExists(f'Post with title "{data["title"]}" already exists')
	
	post = Post(
		title=data['title'],
		body=data['body'],
		slug=data['title'].replace(' ', '-').lower(),
		updated=dt.datetime.now(),
		publish=dt.datetime.now(),
		tags=get_or_create(data['tags'])
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
		publish=dt.datetime.now(),
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
