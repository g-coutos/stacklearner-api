from .auth_controller import auth
from .post_controller import post
from .tags_controller import tags


blueprints = [
	auth,
	post,
	tags
]