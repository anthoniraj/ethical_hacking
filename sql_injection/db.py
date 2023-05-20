import sqlite3
'''
Author: Anthoniraj Amalanathan
Date Last Modified: 29-Apr-2023
'''
def check_user_login(username, password):
    conn = sqlite3.connect('note.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password))  
    #cursor.execute("SELECT * FROM users WHERE username = (?) AND password = (?)", (username, password))  
    record = cursor.fetchone()  
    conn.close()
    return record

def add_note(user_id, content, timestamp):
    conn = sqlite3.connect('note.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notes (user_id, content, timestamp) VALUES (?,?,?)',(user_id, content, timestamp))
    conn.commit()
    conn.close()
