from flask import Blueprint, request, session, jsonify
from app.errors import ItemNotFoundError, ItemAlreadyExists
from app.services.post_service import get_all, create, delete

post = Blueprint('post', __name__, url_prefix='/posts/')

@post.route('/', methods=['OPTIONS'])
def handle_options():
    return '', 204

@post.route('/', methods=['GET'])
def list_posts():
	posts = get_all()
		
	return jsonify([post.to_dict() for post in posts]), 200


@post.route('/', methods=['POST'])
def create_post():
	try:
		data = request.get_json()
		print(data)
		post = create(data)

		return jsonify(post.to_dict()), 201
	
	except ItemAlreadyExists as e:
		return jsonify({
			'error': 'Item with same title already exists',
			'message': str(e)
		}), 500

@post.route('/', methods=['DELETE'])
def delete_post():
	try:
		_id = request.args.get('id')

		delete(_id)

		return jsonify({'message': 'Post deleted'}), 200
	
	except ItemNotFoundError as e:
		return jsonify({
			'error': 'Item not found',
			'message': str(e)
		}), 404
	


	