from flask import Blueprint, request, session, jsonify
from app.errors import ItemNotFoundError, ItemAlreadyExists
from app.services.post_service import get_all, get_one, create, edit, delete

post = Blueprint('post', __name__, url_prefix='/posts')

@post.route('/', methods=['OPTIONS'])
def handle_options():
    return '', 204
	
@post.route('/', methods=['GET'])
def list_posts():
	_id = request.args.get('_id')

	if _id:
		try:
			post = get_one(_id)

			return jsonify(post.to_dict()), 200
	
		except ItemNotFoundError as e:
			return jsonify({
				'error': str(e)
			})
	else:
		posts = get_all()
		
		return jsonify([post.to_dict() for post in posts]), 200

@post.route('/', methods=['POST'])
def create_post():
	try:
		data = request.get_json()
		post = create(data)

		return jsonify(post.to_dict()), 201
	
	except ItemAlreadyExists as e:
		return jsonify({
			'error': str(e)
		}), 409
	
@post.route('/', methods=['PUT'])
def edit_post():
	try:
		data = request.get_json()
		post = edit(data)

		return jsonify(post.to_dict()), 200
	
	except ItemAlreadyExists as e:
		return jsonify({
			'error': str(e),
		}), 409

@post.route('/', methods=['DELETE'])
def delete_post():
	_id = request.args.get('_id')

	try:
		delete(_id)

		return jsonify({'message': 'Post deleted'}), 200
	
	except ItemNotFoundError as e:
		return jsonify({
			'error': str(e)
		}), 404
	


	