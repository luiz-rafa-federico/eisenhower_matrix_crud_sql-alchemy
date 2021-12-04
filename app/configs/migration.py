from flask_migrate import Migrate
from flask import Flask

def init_app(app: Flask):
    from app.models.tasks_model import Tasks
    from app.models.categories_model import Categories
    from app.models.eisenhowers_model import Eisenhowers
    from app.models.tasks_categories_table import tasks_categories
    Migrate(app, app.db)
