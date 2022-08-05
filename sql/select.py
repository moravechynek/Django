import sqlite3

con = sqlite3.connect('../website/db.sqlite3')
cur = con.cursor()

for row in cur.execute("SELECT * FROM autoskola_otazka;"):
    print(row)

con.commit()

con.close()