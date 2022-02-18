from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/users')


@bp.route('/')
def user_list():
    return "user list"
