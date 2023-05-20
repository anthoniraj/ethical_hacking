from flask import Flask,render_template, request, session,redirect, url_for
from db import check_user_login, add_note
from datetime import datetime
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = '876a@2ecre7'
csrf = CSRFProtect(app)

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = request.args.get('error')
    if request.method == "POST":
        uname = request.form['username']
        pwd = request.form['password']
        record = check_user_login(uname, pwd)
        if record != None:
            # Login Matched and Success
            session['logged_in'] = True
            session['user_id'] = record[0]
            session['username'] = record[1]
            return render_template('home.html', username = session['username'])
        else:
            return render_template('login.html', error = "Invalid User")
    return render_template('login.html', error=error)

@app.route("/addNote", methods=['GET', 'POST'])
def add_note_page():
    if request.method == "POST":
        if session.get('logged_in') == True:
            content = request.form['content']
            user_id = session.get('user_id')
            timestamp = datetime.now()
            add_note(user_id, content, timestamp)
            return render_template('add_note.html', message="Note added successfully")
        return render_template('add_note.html', message="Invalid Session")
    return render_template('add_note.html')


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)