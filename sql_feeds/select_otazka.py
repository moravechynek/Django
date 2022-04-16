import sqlite3

con = sqlite3.connect('../website/db.sqlite3')
cur = con.cursor()

for row in cur.execute("SELECT obrazek FROM autoskola_otazka WHERE obrazek NOT LIKE '' ORDER BY id DESC;"):
    print(row)

con.commit()

con.close()