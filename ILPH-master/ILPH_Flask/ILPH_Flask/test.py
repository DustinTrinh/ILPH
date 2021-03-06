import os
from flask import Flask, render_template, redirect, url_for, request
from database_queries import *


app = Flask(__name__)

# create a database connection
conn = None
username = None
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
            username = getUserName(request.form['username'])
            username_pass = username[0][0]
            user_id = username[0][1]
          #  print("Username 1111111 ", username)
            return redirect(url_for('home', username = username_pass, user_id = user_id))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('staff/login.html', error=error);



@app.route('/home/<username>/<user_id>', methods=['GET', 'POST'])
def home(username, user_id):


    if 'add_case' in request.form:
        userID = request.form['case_user_id']
        date = request.form['case_date']
        status = request.form['case_status']
        vPlate = request.form['case_vPlate']
        vType = request.form['case_vType']
        desc = request.form['case_description']
        print("Newly add: ", userID)
        print("Newly add: ", date)
        print("Newly add: ", status)
        print("Newly add: ", vPlate)
        print("Newly add: ", vType)
        print("Newly add: ", desc)
        insertNewCase(userID, date, status, vPlate, vType, desc)
        

    ActiveResult = getAllActiveCases()
    activeDescription = getActiveDescription()
    ClosedResult = getAllClosedCases()
    closeDescription = getCloseDescription()
    return render_template("staff/main_staffs.html",  active_list = ActiveResult, close_list = ClosedResult, activeDescription = activeDescription, closeDescription = closeDescription, username = username, user_id = user_id);

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)