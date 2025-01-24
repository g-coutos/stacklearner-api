from flask import Blueprint, request, jsonify
from app.services.post_service import get_all_posts, create_new_post

post_bp = Blueprint('post', __name__, url_prefix='/posts')

@post_bp.route('/', methods=['GET'])
def list_posts():
	posts = get_all_posts()
	return jsonify([post.to_dict() for post in posts])

@post_bp.route('/', methods=['POST'])
def create_post():
	data = request.get_json()
	post = create_new_post(data)

	return jsonify(post.to_dict()), 201
	