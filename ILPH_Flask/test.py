import os
from flask import Flask, render_template, redirect, url_for, request
from database_queries import *


app = Flask(__name__)

# create a database connection
conn = None
username = None
changePass = None
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
    changePass = None
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
    changePass = None

    if 'add_case' in request.form:
        userID = request.form['case_user_id']
        date = request.form['case_date']
        status = request.form['case_status']
        vPlate = request.form['case_vPlate']
        vType = request.form['case_vType']
        desc = request.form['case_description']
        """
        print("Newly add: ", userID)
        print("Newly add: ", date)
        print("Newly add: ", status)
        print("Newly add: ", vPlate)
        print("Newly add: ", vType)
        print("Newly add: ", desc)
        """
        insertNewCase(userID, date, status, vPlate, vType, desc)
    if 'update_case' in request.form:
        caseID = request.form['caseID']
        status = request.form['update_status']
        updateCaseStatus(caseID,status)
        """
        print("The CASE ID: " + caseID)
        print("The Status: " + status)
        """
    
    if 'personal_info' in request.form:
        print("THIS IS THE FORM")
        
        uname = request.form['info_username']
        uname = uname.lower()
        oldPass = request.form['info_prevPassword']
        newPass = request.form['info_newPass']

        check = authenticate(uname, oldPass)

        if check == True: 
            
            updatePassword(user_id, newPass)
            changePass = "Successfully Changed Password"
        else:
            print("Not OKKKKKK")
            changePass = "Failed to Change Password. Please recheck your current password and refill form"


    ActiveResult = getAllActiveCases()
    activeDescription = getActiveDescription()
    activeCoordinate = getActiveCoordinate()
    ClosedResult = getAllClosedCases()
    closeDescription = getCloseDescription()
    closeCoordinate = getClosedCoordinate()
    userInfo = getUserInfo(user_id)

    return render_template("staff/main_staffs.html",  active_list = ActiveResult, close_list = ClosedResult, activeDescription = activeDescription, active_coor = activeCoordinate, closeDescription = closeDescription, close_coor = closeCoordinate, username = username, user_id = user_id, userInfo = userInfo, changePass = changePass);

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)