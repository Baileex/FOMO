import sqlite3
from flask_restful import Resource, reqparse

class User:
  def __init__(self, _id, username, email, age, password, location,option_1, option_2, option_3, option_4):
    self.id = _id
    self.username = username
    self.password = password

  @classmethod
  def find_by_username(cls, username):
    connection = sqlite3.connect('fomo.db')
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username=?"
    result = cursor.execute(query, (username,))
    row = result.fetchone()
    if row:
      user = cls(*row)
    else:
        user = None

    connection.close()
    return user

  @classmethod
  def find_by_id(cls, _id):
    connection = sqlite3.connect('fomo.db')
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE id=?"
    result = cursor.execute(query, (_id,))
    row = result.fetchone()
    if row:
      user = cls(*row)
    else:
        user = None

    connection.close()
    return user


class UserRegister(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('username', type=str, required=True, help="This field cannot be blank")
  parser.add_argument('email', type=str, required=True, help="This field cannot be blank")
  parser.add_argument('age', type=int, required=True, help="This field cannot be blank")
  parser.add_argument('password', type=str, required=True, help="This field cannot be blank")
  parser.add_argument('location', type=str, required=True, help="This field cannot be blank")
  parser.add_argument('option_1', type=str, help="This field cannot be blank")
  parser.add_argument('option_2', type=str, help="This field cannot be blank")
  parser.add_argument('option_3', type=str, help="This field cannot be blank")
  parser.add_argument('option_4', type=str, help="This field cannot be blank")

  def post(self):
    data = UserRegister.parser.parse_args()

    if User.find_by_username(data['username']):
      return {"message": "A User with that username already exists"}

    connection = sqlite3.connect('fomo.db')
    cursor = connection.cursor()

    query = "INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, (data['username'], data['email'], data['age'], data['password'], data['location'], data['option_1'], data['option_2'],data['option_3'],data['option_4']))

    connection.commit()
    connection.close()

    return {"message": "User created successfully."}, 201
  
  
class GetUser(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('location', type=str, required=True, help="This field cannot be blank")
  parser.add_argument('option_1', type=str, required=True, help="This field cannot be blank")
  parser.add_argument('option_2', type=str, required=True, help="This field cannot be blank")
  parser.add_argument('option_3', type=str, required=True, help="This field cannot be blank")
  parser.add_argument('option_4', type=str, required=True, help="This field cannot be blank")


  def get(self, username):
    connection = sqlite3.connect('fomo.db')
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username=?"
    result = cursor.execute(query, (username,))
    row = result.fetchone()
  
    connection.commit()
    connection.close()
    return row



  def patch(self, username):
    data = GetUser.parser.parse_args()

    connection = sqlite3.connect('fomo.db')
    cursor = connection.cursor()
    
    if data['location']:
      query = "UPDATE users SET location = ?, option_1 = ?, option_2 = ?, option_3 = ?, option_4 = ? WHERE username=?"
      cursor.execute(query, (data['location'], data['option_1'], data['option_2'], data['option_3'], data['option_4'], username))

      connection.commit()
      connection.close()

      return {"message": "User successfully updated"}
  

 