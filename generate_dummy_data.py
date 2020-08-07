
import sqlite3
import names
import random
from random import sample
from os import path

Company = ['Microsoft','CocaCola','Samsung','Toyota','Dominos','Facebook','Apple','Google','Disney','Amazon']

DOB = ['2015','2010','2005','2000','1995','1990','1985','1980','1975','1970']

Location = ['Delhi','Banglore','Mumbai','Kolkata','Madras','Hydrabad','Bhopal','Jaipur','Goa','Agra']

Hobbies = ['Sports','Music','Dance','Reading','Gaming', 'Craft', 'Travel','Fishing','Acting','Gardening']


# Connect to Database using sqlite3
def connectdb(database):
    '''
    Input: String
    Output: sqlite3.Connection
    '''

    try:
        conn = sqlite3.connect(database)
        print("Open database successfully")
        return conn
    except:
        print("Open database unsuccessfully")
    

def createtable(conn):
    '''
    Input: sqlite3.Connection
    Output: Create the Table in the database
    '''

    curr = conn.cursor()
    try:
        curr.execute('''CREATE TABLE Data (
            ID INTEGER PRIMARY KEY, 
            Name	TEXT NOT NULL,
            DOB	TEXT NOT NULL,
            Location	TEXT NOT NULL,
            Company	TEXT NOT NULL,
            Hobbies	TEXT NOT NULL)''')
        print ("Table created successfully")
    except:
        print ("Table creation unsuccessfully.")
        print ("Table exist already")
    conn.commit()

def inserttable(database, n_size):
    '''
    Input: database, size of database
    Output: Insert the table with data
    '''

    con = sqlite3.connect(database)
    try:
        for i in range(n_size):
            curr = con.cursor()
            entry = ( i+1, names.get_full_name(), random.choice(DOB), random.choice(Location), random.choice(Company), \
                ' '.join(sample(Hobbies, random.choice([1,2,3,4]))) )
            strs = "INSERT INTO Data ( ID, Name, DOB, Location, Company, Hobbies) VALUES " + str(entry)
            #print(strs)
            curr.execute(strs)
            curr.close()
        con.commit()
    except:
        con.commit() 


# driver program
def main():
    '''
    Output: Creates the database with title - "dummydata_x" + where x represents number of datapoints.
    '''
    
    # Data is set limited to 1000 points to avoid generating similar data.
    while 1:
        n_size = int(input("Please select size of database between 100 and 1000: "))
        # Check limits
        if n_size >= 100 and n_size <= 1000 :
            break
    
    # Database making
    database = "./dummy data/dummydata_" + str(n_size) + ".db"
    print("Database is", database)
    
    # Check the database
    if not path.exists(database):
        # Connect to database    
        conn = connectdb(database)
        # Create Table
        createtable(conn)
        # Insert data into Table
        inserttable(database, n_size)
    else:
        print("Database already exists.")
    
# Call the main function
main()