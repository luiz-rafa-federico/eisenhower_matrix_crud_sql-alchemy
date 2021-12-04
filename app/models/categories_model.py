from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from app.models.tasks_categories_table import tasks_categories


@dataclass
class Categories(db.Model):

    id: int
    name: str
    description: str 
    
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)

    tasks = db.relationship("Tasks", secondary=tasks_categories, backref="categories")