from flask import Flask, jsonify, request
from flask_cors import CORS

from Class.City import City
from Class.DB import DB
from Class.Strength import Strength
from Class.User_Old import User_Old

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<userID>', methods = ['POST', 'GET'])
def user(userID):
    if request.method == 'POST':
        userInfo = request.get_json()
        return userInfo["strengths"]
    else:
        user = User_Old(userID)
        return jsonify(user.__dict__)

@app.route('/allStrengths')
def allStrengths():
    db = DB()
    cursor = db.createCursor()
    cursor.execute("select * from strengthDM_new")
    Strengths = []
    result = cursor.fetchall()
    i = 0
    while i < len(result):
        row = result[i]
        s = Strength(row[0], row[1])
        Strengths.append(s.__dict__)
        i = i + 1
    db.close()
    return jsonify(Strengths)

@app.route('/allCities')
def allCities():
    db = DB()
    cursor = db.createCursor()
    cursor.execute("select * from cityDM_new")
    cities = []
    result = cursor.fetchall()
    i = 0
    while i < len(result):
        row = result[i]
        c = City(row[0], row[1])
        cities.append(c.__dict__)
        i = i + 1
    db.close()
    return jsonify(cities)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
