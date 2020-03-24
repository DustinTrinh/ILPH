import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def general():
    return render_template("general/general.html");

@app.route('/statistics/')
def statistics():
    return render_template('general/general_Statistics.html');

@app.route('/technology/')
def technology():
    return render_template('general/general_Technology.html');

@app.route('/login/')
def login():
    return render_template('staff/login.html');


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
