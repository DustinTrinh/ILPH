import sqlite3
from sqlite3 import Error
import bcrypt

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM staff_db")

    rows = cur.fetchall()

    for row in rows:
        print(row)

"""Specific command """
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def getUser(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT password FROM staff_db WHERE username=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    return rows

def authenticate(username, inputPassword):
    auth = False
    database = r"C:\Users\dusti_000\Desktop\ILPH-master\ILPH_Flask\static\database\ILPH_database.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        password = getUser(conn, username)
        
        
        
        if password:
            dbPass = password[0][0]
            dbPass = dbPass[2:]
            dbPass = dbPass[:-1]
            dbPass = dbPass.encode('utf-8')
            encodePassword = inputPassword.encode('utf-8')
            """
            print("HEY 1 ", type(dbPass))
            print("HEY 2 ", type(encodePassword))
            print("HEY 3 ", type(password[0][0]))
            print("HEY 4 ", dbPass)
            print("HEY 5 ", encodePassword)
            print("HEY 6 ", password[0][0])
            print("HEY Final 1 ", test)
            print("HEY Final 2 ", finalTest)
            print("HEY Final 3 ", type(finalTest))

            """
            if bcrypt.checkpw(encodePassword, dbPass):
                auth = True
            else:
                auth = False

        else:
            auth = False
    return auth

def getAllActiveCases():
    database = r"C:\Users\dusti_000\Desktop\ILPH-master\ILPH_Flask\static\database\ILPH_database.db"

    # create a database connection
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT cases.Case_ID, staff.name, cases.Date, cases.Status, cases.Vehicle_Plate, cases.Vehicle_Type FROM cases_db cases INNER JOIN staff_db staff ON cases.Posted_By = staff.staff_ID WHERE Status != 'Close' ;")
    rows = cur.fetchall()    
    print(rows)
    return rows

def getAllClosedCases():
    database = r"C:\Users\dusti_000\Desktop\ILPH-master\ILPH_Flask\static\database\ILPH_database.db"

    # create a database connection
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT cases.Case_ID, staff.name, cases.Date, cases.Status, cases.Vehicle_Plate, cases.Vehicle_Type FROM cases_db cases INNER JOIN staff_db staff ON cases.Posted_By = staff.staff_ID WHERE Status = 'Close' ;")
    rows = cur.fetchall()    
    print(rows)
    return rows