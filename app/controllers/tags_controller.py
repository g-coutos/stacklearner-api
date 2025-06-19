from flask import Blueprint, request, jsonify
from app.services.tag_service import search

tags = Blueprint('tags', __name__, url_prefix='/tags')

@tags.route('', methods=['GET'], strict_slashes=False)
def search_tags():
		search_term = request.args.get('search')

		try:
				tags = search(search_term)

				return jsonify(tags), 200
		except Exception as e:
				return jsonify({'error': str(e)}), 500