import sqlite3

con = sqlite3.connect('../website/db.sqlite3')
cur = con.cursor()

cur.execute("DELETE FROM autoskola_otazka;")

con.commit()

con.close()