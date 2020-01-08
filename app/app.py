from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister, GetUser

app = Flask(__name__)
app.secret_key = 'FOMO_team'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# users = [
#     {
#         'name': 'Jess',
#         'username': 'jessb',
#         'email': 'test@test.com',
#         'location': 'Manchester',
#         'quiz_terms': ['music', 'sport']
#     }
# ]


# class UserList(Resource):
#   # @jwt_required()
#     def get(self):
#       return users

#     def post(self):
#       data = request.get_json()
#       new_user = {
#                   'name': data['name'],
#                   'username': data['username'],
#                   'email': data['email'],
#                   'location': data['location'],
#                   'quiz_terms': []
#               }
#       users.append(new_user)
#       return new_user, 201

# class User(Resource):
        
#     def get(self, username):
#       user = next(filter(lambda x: x['username'] == username, users), None)
#       return {'user': user}, 200 if user is not None else 404  

    
#     def delete(self, username):
#       global users
#       users = list(filter(lambda x: x['username'] != username, users))
#       return {'message': 'Item deleted'}

#     def patch(self, username):
#       parser =reqparse.RequestParser()
#       parser.add_argument('quiz_terms', required=True)
#       data = parser.parse_args()

#       user = next(filter(lambda x: x['username'] == username, users), None)
#       if user is not None:
#         user.update(data)
#       return user
#       # note only reads first quiz term - needs fixing!


# api.add_resource(UserList, '/users')
# api.add_resource(User, '/users/<string:username>')
api.add_resource(UserRegister, '/register')
api.add_resource(GetUser, '/users/<string:username>')



# @app.route('/users')
# def get_users():
#     return jsonify({'users': users})



# @app.route('/users', methods=['POST'])
# def create_user():
#     request_data = request.get_json()
#     new_user = {
#         'name': request_data['name'],
#         'username': request_data['username'],
#         'email': request_data['email'],
#         'location': request_data['location'],
#         'quiz_terms': []
#     }
#     users.append(new_user)
#     return jsonify(new_user)


# @app.route('/users/<string:username>')
# def get_user_by_username(username):
#     for user in users:
#       if user['username'] == username:
#         return jsonify(user)
#     return jsonify({'message': 'user not found'})      


# @app.route('/business', methods=['POST'])
# def create_business():
#     pass


# @app.route('/business/<string:name>')
# def get_business():
#     pass

# @app.route('/events')
# def get_business_events():
#     pass

# get business events by location
# get business events by key terms

    
app.run(port=5000, debug=True)
