
import sqlite3
from prettytable import PrettyTable
import random
import pickle


dbpath = './dummy data/'
frpath = './friends network/'
dbfile = 'dummydata_'
repr_type = 'linked_list'


n_size = int(input("Enter the size of database "))




friend_filename  =  frpath + repr_type + '_' + dbfile + str(n_size) + '.pkl'
db_filename = dbpath + dbfile + str(n_size) +'.db'

def disp_(rows):
    table = PrettyTable(['ID','Name','DOB','Location','Company','Hobbies'])
    for r in rows:
        table.add_row(r)
    print(table)    


new_friend = []
reco_friend = []

with open(friend_filename,'rb') as f:
    friend_repr = pickle.load(f)

print(friend_repr)

print("Press Enter for default.") 
Name = input("Input Name")
DOB = input('Input Year of Birth (1975 - 2020)')
Location = input('Input your Location. Major Cities from India.')
Company	= input('Input your Company. Top 10 Companies from World.')
Hobbies = input('Input your Hobbies. Space seprated.')

if Name == '':
    Name = 'Yash Gupta'
if DOB == '':
    DOB = '1998'
if Location == '':
    Location = 'Delhi'
if Company == '':
    Company = 'Google'
if Hobbies == '':
    Hobbies = 'Gaming'

print(Name, DOB, Location, Company, Hobbies)


try:
    conn = sqlite3.connect(db_filename)
    print("Open database successfully")
except:
    print("Open database unsuccessfully")

curr = conn.cursor()
curr.execute("SELECT * FROM Data WHERE Location=? AND Company=? ", (Location, Company))
rows = curr.fetchall()

curr.close()



disp_(rows)

friend_list = [300,250]

while 1:
    print("Enter ID of the person to become friend")
    print("Enter 0 to view current list of friends")
    new_friend = int(input())
    if new_friend == 0:
        print(friend_list)
        curr = conn.cursor()
        result_set = curr.execute('SELECT * FROM Data WHERE ID IN (%s)' % ("?," * len(all_recommendations))[:-1], all_recommendations)
        curr.execute("SELECT * FROM Data WHERE ID IN (?)", (list(set(friend_list))))
        rows = curr.fetchall()
        curr.close()
        disp_(rows)
    else:
        friend_list.append(str(new_friend))
        all_recommendations = []
        for i in friend_list:
            for j in friend_repr[int(i)-1]:
                curr = conn.cursor()
                curr.execute("SELECT ID FROM Data WHERE ID = ? AND  Hobbies LIKE ? ", (str(j), '%' + Hobbies + '%'))
                rows = curr.fetchall()
                rows_list = [str(r[0]) for r in rows]
                curr.close()
                all_recommendations.extend(rows_list)

        print(all_recommendations)
        curr = conn.cursor()
        result_set = curr.execute('SELECT * FROM Data WHERE ID IN (%s)' % ("?," * len(all_recommendations))[:-1], all_recommendations)
        #curr.execute("SELECT * FROM Data WHERE ID IN (?)", (list(set(all_recommendations))))
        print(result_set)
        rows = curr.fetchall()
        curr.close()
        disp_(rows)

