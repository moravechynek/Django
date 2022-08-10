import sqlite3

con = sqlite3.connect('../website/db.sqlite3')
cur = con.cursor()
f = open('../scrapers/topics.csv', 'r')
i = 0
f.readline()
while i < 976:
    line = f.readline().split(';')
    a_id = line[0]
    topic = line[1].replace('\n','')

    cur.execute("UPDATE autoskola_otazka SET orig_topic = '" + topic + "' WHERE a_id = " + a_id + ";")
    
    i += 1

con.commit()

con.close()