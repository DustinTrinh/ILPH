import string
import random
import datetime
import sqlite3
from sqlite3 import Error

database = "./static/databaseILPH_database.db"
cars = ["Acura", "Aston Martin", "Audi", "Bentley", "BMW", "Buick", "Cadillac", "Chevrolet", "Dodge", "Fiat", "Ford", "Jaguar", "Jeep", "Honda", "KIA", "Lexus", "Mazda", "MINI", "Toyota", "Tesla", "RAM"]
desc = ["Unclear due to Rainy Weather", "Unclear due to night vision", "Unclear due to Foggy weather", "unclear suspect", "Unclear due to fast speed"]
coor = [("43.7714", "-79.4988"), ("43.7952", "-79.3497"), ("43.9552", "-79.5186"), ("43.8500", "-79.3671"), ("43.7183", "-79.5098")]
stat = ["Searching", "Found", "Close"]
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

def License_Generator(size=7, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def Date_Generator():
    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2020, 4, 30)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def insertion(userID, date, status, vPlate, vType, desc, lat, long ):
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("INSERT INTO cases_db (Posted_By, Date, Status, Vehicle_Plate, Vehicle_Type, Description, Latitude, Longitude) VALUES (?,?,?,?,?,?,?,?)", (userID, date, status, vPlate, vType, desc, lat, long,))
    conn.commit()
	
def main():

    count = 0


    while count < 300:
	    
        print("------------ ROUND " + str(count) + "------------")
        postedBy = random.randint(1,2)
        date = Date_Generator()
        status = random.randint(0,2)
        license = License_Generator()
        carType = random.randint(0, len(cars)-1)
        description = random.randint(0, len(desc)-1)
        coordinate = random.randint(0, len(coor) - 1)
        print("Posted By: " + str(postedBy))	
        print("Date: " + str(date))
        print("Status: " + stat[status])
        print("License: " + license)
        print("Car Type: " + cars[carType])
        print("Description: " + desc[description])
        print("Latitude: " + coor[coordinate][0] + "---------Longitude: " + coor[coordinate][1])
        print("-------------------------------------------")
        insertion(postedBy, date, stat[status], license,  cars[carType], desc[description], coor[coordinate][0], coor[coordinate][1] )
        count += 1  
    
       


if __name__ == '__main__':
    main()