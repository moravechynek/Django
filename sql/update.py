import sqlite3

con = sqlite3.connect('../website/db.sqlite3')
cur = con.cursor()
f = open('../scrapers/temp.csv', 'r')
i = 0
f.readline()
while i < 959: #959
    line = f.readline().split(';')
    id = str(line[0])
    a_id = str(line[1])
    b_id = str(line[2])
    c_id = str(line[3])

    cur.execute("UPDATE autoskola_otazka SET a_id = '" + a_id + "', b_id = '" + b_id + "', c_id = '" + c_id + "' WHERE id = " + id + ";")
    print(id)
    print(a_id)
    print(b_id)
    print(c_id)
    print()
    i += 1

con.commit()

con.close()