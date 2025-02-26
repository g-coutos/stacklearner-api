import os
from flask import Blueprint, request, session, make_response, jsonify

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']

	if username == os.getenv('USER_NAME') and password == os.getenv('USER_PASSWORD'):
		if 'user' not in session:
			session['user'] = username

		return jsonify({
			'message': f'Welcome {username}!',
		}), 200
	
	return jsonify({
		'error': 'Unauthorized',
		'message': 'Invalid credentials',
	}), 401

@auth.route('/logout', methods=['POST'])
def logout():
	session.pop('session', None)
	session.clear()

	return jsonify({
			'message': 'Logout completed successfully'
	}), 200