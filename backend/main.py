from flask import Flask, abort
from flask import request, Response, session, redirect
from flask_cors import CORS
import json
from login import tokens
from users import users

app = Flask(__name__)

# 跨域
CORS(app)

@app.route('/hello', methods=['get'])
def hello_world():
    return 'Hello, World!'

@app.route('/vue-admin-template/user/login', methods=['post'])
def login():

    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')
    token = tokens[username]
    if not token:
      return {
        'code': 60204,
        'message': 'Account and password are incorrect.'
      }

    return {
        'code': 20000,
        'data': token
      }

@app.route('/vue-admin-template/user/info', methods=['get'])
def get_user_info():
    # data = json.loads(request.data)
    data = request.args.to_dict()
    token = data['token']
    try:
      info = users[token]
      return {
        'code': 20000,
        'data': info
      }
    except KeyError:
      return {
        'code': 50008,
        'message': 'Login failed, unable to get user details.'
      }

@app.route('/vue-admin-template/user/logout', methods=['post'])
def logout():
    print(request)
    return {
      'code': 20000,
      'data': 'success'
    }


if __name__ == '__main__':
    # 监听在所有 IP 地址上
    app.run(port=5000)
