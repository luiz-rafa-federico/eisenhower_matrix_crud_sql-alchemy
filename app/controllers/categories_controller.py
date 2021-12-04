from flask import jsonify, request, current_app
from app.models.categories_model import Categories
from app.models.eisenhowers_model import Eisenhowers
from sqlalchemy import exc


def create_category(categ=None):
    try:
        data = request.get_json()

        if categ:
            category = Categories(name=categ)
        else:
            category = Categories(**data)

        current_app.db.session.add(category)
        current_app.db.session.commit()

        return jsonify(category), 201
    except exc.IntegrityError:
        return jsonify({'msg': 'Category already exists'}), 409


def update_category(id: int):

    data = request.get_json()

    category_found = Categories.query.filter_by(id=id).update(data)

    if not category_found:
        return {'msg': 'Category not found'}, 404

    current_app.db.session.commit()
    category_updated = Categories.query.get(id)
    return jsonify(category_updated)


def delete_category(id: int):
    category = Categories.query.get(id)
    
    if not category:
        return {'msg': 'Category not found'}, 404

    current_app.db.session.delete(category)
    current_app.db.session.commit()
    return "", 204


def get_all():
    ...