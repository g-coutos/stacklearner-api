from app.models.tag import Tag
from app.database import db_session

import datetime as dt

def search(search_term):
	if not search_term or len(search_term) <= 0:
		return []
	
	search_term = search_term.lower().strip()

	tags = Tag.query.filter(
		Tag.name.ilike(f'%{search_term}%')
	).order_by(Tag.name).all()

	if not tags:
		return []

	for tag in tags:
		tag['_id'] = str(tag['_id'])
		tag['name'] = tag['name'].lower()

	return tags

def get_or_create(data):
		formatted = []
		new_tags = []
		final = []

		if len(data) <= 0:
			return final
		
		for tag in data:
			formatted.append(tag.lower())
		
		for name in formatted:
			tag = Tag.query.filter_by(name=name).first()

			if tag:
				final.append(tag)
			else:
				new_tag = Tag(
					name=name,
				)

				new_tags.append(new_tag)

				final.append(new_tag)

		db_session.add_all(new_tags)

		return final