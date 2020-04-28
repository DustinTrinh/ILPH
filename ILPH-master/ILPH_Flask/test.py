import os
from flask import Flask, render_template, redirect, url_for, request
from authentication import *


app = Flask(__name__)

# create a database connection
conn = None
 
""" use with conn to do select 
    with conn:

        print("1. Query all tasks")
        select_all_tasks(conn) 
"""


@app.route("/")
def general():
    return render_template("general/general.html");

@app.route('/statistics/')
def statistics():
    return render_template('general/general_Statistics.html');

@app.route('/technology/')
def technology():
    return render_template('general/general_Technology.html');

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':


        if authenticate(request.form['username'], request.form['password']):
            return redirect(url_for('home'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('staff/login.html', error=error);



@app.route('/home/')
def home():
    ActiveResult = getAllActiveCases()
    ClosedResult = getAllClosedCases()
    return render_template("staff/main_staffs.html",  active_list = ActiveResult, close_list = ClosedResult);

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)