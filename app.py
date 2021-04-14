from flask import Flask, jsonify, request
from flask_cors import CORS

from Class.User_Old import User_Old

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<userID>')
def user(userID):
    user = User_Old(userID)
    return jsonify(user.__dict__)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
