from flask import Flask, jsonify

'''
Author: Anthoniraj Amalanathan
Date Last Modified: 19-Apr-2023
Description: Flask Web Services for Demonstrating the following Web Penetration Testing
1. Bruteforce Login Attack using Hydra
'''

app = Flask(__name__)

@app.route("/")
def home():
    return "Sample Web Service"

@app.route("/welcome/<string:name>")
def welcome(name):
    '''
    Simple Web Service for Greeting User
    '''
    data="Welcome "+name
    return jsonify(data=data),200

@app.route("/login/<username>/<password>")
def verify_login(username, password):
    if username == "admin" and password == "123456":
        return "Welcome to Admin Portal"
    else:
        return "Unauthorised User"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=True)