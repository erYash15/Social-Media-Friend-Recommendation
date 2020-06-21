import random
import sqlite3
import pickle




linked_list_representation = []

conn = sqlite3.connect("./dummy data/dummydata.db")
curr = conn.cursor()
curr.execute('SELECT COUNT(*) FROM Data')
rows = curr.fetchone()
no_of_people = rows[0]
conn.commit()

all_people = [int(i) for i in range(no_of_people)] #just stores number 1 to 2000

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