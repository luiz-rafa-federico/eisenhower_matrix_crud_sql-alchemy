from flask import Flask
from app.routes.tasks_blueprint import bp as bp_tasks
from app.routes.categories_blueprint import bp as bp_categories, bp_cat_tasks


def init_app(app: Flask):
    app.register_blueprint(bp_tasks)
    app.register_blueprint(bp_categories)
    app.register_blueprint(bp_cat_tasks)