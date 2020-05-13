import sqlite3
from sqlite3 import Error
import bcrypt

database = r"C:\Users\dusti_000\Desktop\ILPH-master\ILPH_Flask\static\database\ILPH_database.db"
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

   # for row in rows:
       # print(row)

    return rows

def authenticate(username, inputPassword):
    auth = False

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
def getUserName(priority):
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT name, staff_ID FROM staff_db WHERE username=?", (priority,))
    rows = cur.fetchall()    
  #  print(rows)
    return rows
    
def getAllActiveCases():

    # create a database connection
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT cases.Case_ID, staff.name, cases.Date, cases.Status, cases.Vehicle_Plate, cases.Vehicle_Type FROM cases_db cases INNER JOIN staff_db staff ON cases.Posted_By = staff.staff_ID WHERE Status != 'Close' ;")
    rows = cur.fetchall()    
 #   print(rows)
    return rows

def getAllClosedCases():

    # create a database connection
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT cases.Case_ID, staff.name, cases.Date, cases.Status, cases.Vehicle_Plate, cases.Vehicle_Type FROM cases_db cases INNER JOIN staff_db staff ON cases.Posted_By = staff.staff_ID WHERE Status = 'Close' ;")
    rows = cur.fetchall()    
  #  print(rows)
    return rows

def getCloseDescription():
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT case_ID, description FROM cases_db WHERE Status = 'Close' ;")
    rows = cur.fetchall()    
    #print(rows)
    return rows

def getActiveDescription():
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT case_ID, description FROM cases_db WHERE Status != 'Close' ;")
    rows = cur.fetchall()    
   # print(rows)
    return rows

def insertNewCase(userID, date, status, vPlate, vType, desc):
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("INSERT INTO cases_db (Posted_By, Date, Status, Vehicle_Plate, Vehicle_Type, Description) VALUES (?,?,?,?,?,?)", (userID, date, status, vPlate, vType, desc,))
    conn.commit()
    print("ADDDDDDD SUCCESSFULLY")