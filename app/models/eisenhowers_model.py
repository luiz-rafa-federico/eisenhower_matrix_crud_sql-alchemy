from app.configs.database import db
from dataclasses import dataclass


@dataclass
class Eisenhowers(db.Model):

    id: int
    type: str
    
    __tablename__ = "eisenhowers"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))