from flask import Blueprint
from app.controllers.categories_controller import (
    create_category,
    update_category,
    delete_category,
    get_all
)

bp = Blueprint('bp_categories', __name__, url_prefix="/category")

bp.post("")(create_category)
bp.patch("/<int:id>")(update_category)
bp.delete("/<int:id>")(delete_category)


bp_cat_tasks = Blueprint('bp_cat_tasks', __name__, url_prefix="/")

bp_cat_tasks.get("")(get_all)