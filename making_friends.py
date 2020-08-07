import random
import sqlite3
import pickle


linked_list_representation = []

# Data is set limited to 1000 points to avoid generating similar data.
while 1:
    n_size = int(input("Please select size of database between 100 and 1000: "))
    # Check limits
    if n_size >= 100 and n_size <= 1000 :
        break

# Make the initial friends

path = './dummy data/'
dbfile = 'dummydata_'

database = path + dbfile + str(n_size) + ".db"


conn = sqlite3.connect(database)
curr = conn.cursor()
curr.execute('SELECT COUNT(*) FROM Data')
rows = curr.fetchone()
no_of_people = rows[0]
conn.commit()

all_people = [int(i) for i in range(no_of_people)] 

min_friends = 50
max_friends = 100
poss_friend = [int(i) for i in range(min_friends,max_friends)]

print(random.choice(poss_friend))

for i in all_people:
    #assuming each person has 50-99 friend

    temp_choice = (random.sample(all_people, random.choice(poss_friend)))
    temp_choice.sort()
    try:
        temp_choice.remove(i)
    except:
        pass
    linked_list_representation.append(temp_choice)

print(linked_list_representation)

save_filename = './friends network/' + 'linked_list_' + dbfile + str(n_size) +'.pkl'

with open(save_filename,'wb') as f:
    pickle.dump(linked_list_representation,f)