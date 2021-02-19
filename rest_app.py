from flask import Flask, request
from db_connector import get_specific_user, adding_user, update_user, delete_user
from web_app import get_user_name_from_db

app = Flask(__name__)


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        user_name = get_specific_user(user_id)
        if user_name:
            return {'status': 'ok', 'user_name': user_name[0]}, 200
        else:
            return {'status': 'error', 'reason': 'no such id'}, 500

    elif request.method == 'POST':
        request_data = request.json
        try:
            user_name = request_data.get('user_name')
        except Exception:
            return 'Wrong format'
        if not adding_user(user_id, user_name):
            return {'status': 'error', 'reason': 'id already exists'}, 500
        else:
            return {'status': 'ok', 'user added': user_name}, 200

    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        if user_name:
            if not update_user(user_id, user_name):
                return {'status': 'error', 'user updated': 'no such id'}, 500
            else:
                return {'status': 'ok', 'user updated': user_name}, 200

    elif request.method == 'DELETE':
        user_name = get_specific_user(user_id)
        if user_name:
            delete_user(user_id)
            return {'status': 'ok', 'user_deleted': user_id}, 200
        else:
            return {'status': 'error', 'reason': 'no such id'}, 500


@app.route('/users/get_user_data/<user_id>')
def get_user_data(user_id):
    user_name = get_user_name_from_db(user_id)
    if user_name:
        return "<H1 id='user'>" + user_name + "</H1>", 200
    else:
        return "<H1 id='error'>" + 'no such user:' + user_name + "</H1>", 500


app.run(host='127.0.0.1', debug=True, port=5000)
