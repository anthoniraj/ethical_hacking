from flask import Flask, jsonify
import sqlite3

'''
Author: Anthoniraj Amalanathan
Date Last Modified: 19-Apr-2023
Description: Flask Web Services for Demonstrating the following Web Penetration Testing
1. Bruteforce Login Attack using Hydra
SQL Injection
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

@app.route("/user/<string:name>")
def search_user(name):
    '''
    SQL Injection Attack
    '''
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute("select * from test where username = '%s'" % name)
    data = str(cur.fetchall())
    con.close()    
    return jsonify(data=data),200

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=True)