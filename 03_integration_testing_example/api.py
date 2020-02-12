from abc import abstractmethod
from flask import Flask, jsonify


app = Flask(__name__)

class UserBroker:
    """In a real application this would probably be a database connection."""

    def __init__(self):
        self._users = [
            {
             'id': 1,
             'first_name': 'Martin',
             'last_name': 'Leiermann',
             'mail': 'martin.leiermann@sample.ch',
             'age': 23,
             'gender': 'm'
            },
            {
             'id': 2,
             'first_name': 'Martina',
             'last_name': 'Leiermann',
             'mail': 'martina.leiermann@sample.ch',
             'age': 26,
             'gender': 'f'
            }
        ]

    def get_users(self):
        return [{'first_name': u['first_name'], 'last_name': u['last_name'], 'id': u['id']} for u in self._users]

    def get_user_by_id(self, user_id):
        u = None

        for user in self._users:
            if user['id'] == user_id:
                u = user

        return u

user_broker = UserBroker()

@app.route("/api/v0/users", methods=['GET'])
def users_get():
    return jsonify({'items': user_broker.get_users()})

@app.route("/api/v0/users/<int:user_id>", methods=['GET'])
def users_get_by_id(user_id):
    return jsonify(user_broker.get_user_by_id(user_id))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7070)
