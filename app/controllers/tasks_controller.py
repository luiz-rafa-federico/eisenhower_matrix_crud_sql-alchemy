from flask import jsonify, current_app, request
from app.models.tasks_model import Tasks
from app.models.eisenhowers_model import Eisenhowers
from app.models.categories_model import Categories
from app.controllers.categories_controller import create_category
from pdb import set_trace
from app.exc.tasks_exc import PrioritiesError
from sqlalchemy import exc


def define_priority(importance, urgency):
    priority = ""
    if importance == 1 and urgency == 1:
        priority = 'Do It First'
    elif importance == 1 and urgency == 2:
        priority = 'Schedule It'
    elif importance == 2 and urgency == 1:
        priority = 'Delegate It'
    elif importance == 2 and urgency == 2:
        priority = 'Delete It'
    return priority


def create_task():
    try:
        session = current_app.db.session

        data = request.get_json()
    
        importance = data['importance']
        urgency = data['urgency']

        priority = define_priority(importance, urgency)

        eisenhower = Eisenhowers.query.filter_by(type=priority).first()
        data['eisenhower_id'] = eisenhower.id

        categories_list = data.pop('categories')

        for category in categories_list:
            category_found = Categories.query.filter_by(name=category['name']).first()

            if not category_found:
                create_category(category['name'])

        new_task = Tasks(**data)
        
        for category in categories_list:
            category_found = Categories.query.filter_by(name=category['name']).first()
            new_task.categories.append(category_found)

        session.add(new_task)
        session.commit()

        return jsonify({
            "id": new_task.id,
            "name": new_task.name,
            "description": new_task.description,
            "duration": new_task.duration,
            "eisenhower_classification": eisenhower.type,
            "category": [{"name": category.name} for category in new_task.categories]
        }), 201
    except PrioritiesError as e:
        return {'error': {
                "valid_options" : {
                    "importance": [1, 2],
                    "urgency": [1, 2]
                },
                "received_options": {
                    "importance": data['importance'],
                    "urgency": data['urgency']
                }
            }}, 404
    except exc.IntegrityError:
        return jsonify({'msg': 'Task already exists'}), 409
    

def update_task(id: int):
    ...
    

def delete_task(id: int):
    ...