from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome Page</h1>"

@app.route("/greet")
def greet():
    value = request.args.get('name')
    return render_template('greet.html', name = value)

@app.route("/jsdemo")
def jsdemo():
    return render_template('jsdemo.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=True)