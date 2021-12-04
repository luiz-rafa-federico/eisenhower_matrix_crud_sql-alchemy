from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, validates
from app.exc.tasks_exc import PrioritiesError
from flask import request


@dataclass
class Tasks(db.Model):

    id: int
    name: str
    description: str 
    duration: int
    importance: int
    urgency: int
    eisenhower_id: int

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    duration = db.Column(db.Integer)
    importance = db.Column(db.Integer)
    urgency = db.Column(db.Integer)
    eisenhower_id = db.Column(db.Integer, db.ForeignKey('eisenhowers.id'), nullable=False)

    eisenhower = relationship('Eisenhowers', backref="task", uselist=False)

    @validates('importance', 'urgency')
    def validate_priorities(self, key, value):
        if value != 1 and value != 2:
            raise PrioritiesError()
        return value