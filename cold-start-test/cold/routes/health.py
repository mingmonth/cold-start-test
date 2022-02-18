import datetime

from flask import Blueprint, jsonify
from cold.models.user import User

bp = Blueprint('health', __name__, url_prefix='/health')


@bp.route('/')
def health_check():
    return "health check"


@bp.route('/2')
def health_check2():
    '''
        include db select
    '''
    result_dict = {}
    query_result = User.query.all()
    if len(query_result) > 0:
        result_dict['id'] = query_result[0].id
        result_dict['username'] = query_result[0].username
        result_dict['email'] = query_result[0].email
        result_dict['timestamp'] = datetime.datetime.utcnow()
    print(result_dict)
    return jsonify(result_dict)
