
import sqlite3
import names
import random
from random import sample

Company = ['Microsoft','CocaCola','Samsung','Toyota','Dominos','Facebook','Apple','Google','Disney','Amazon']

DOB = ['2015','2010','2005','2000','1995','1990','1985','1980','1975','1970']

Location = ['Delhi','Banglore','Mumbai','Kolkata','Madras','Hydrabad','Bhopal','Jaipur','Goa','Agra']

Hobbies = ['Sports','Music','Dance','Reading','Gaming', 'Craft', 'Travel','Fishing','Acting','Gardening']

try:
    conn = sqlite3.connect('dummydata.db')
    print("Open database successfully")
except:
    print("Open database unsuccessfully")


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

conn = sqlite3.connect('dummydata.db')
try:
    for i in range(2000):
        curr = conn.cursor()
        entry = ( i+1, names.get_full_name(), random.choice(DOB), random.choice(Location), random.choice(Company), \
            ' '.join(sample(Hobbies, random.choice([1,2,3,4]))) )
        strs = "INSERT INTO Data ( ID, Name, DOB, Location, Company, Hobbies) VALUES " + str(entry)
        #print(strs)
        curr.execute(strs)
        curr.close()
    conn.commit()
except:
    conn.commit()    
