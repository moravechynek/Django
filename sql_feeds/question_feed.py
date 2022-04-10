import sqlite3

con = sqlite3.connect('../website/db.sqlite3')
cur = con.cursor()
f = open('../scrapers/etesty.csv', 'r')
i = 0
f.readline()
while i < 928:
    line = f.readline().split(';')
    id = i + 1
    question = line[0]
    a = line[1]
    b = line[2]
    c = line[3]
    correct = line[4][0] # not '\n'
    cur.execute("INSERT INTO autoskola_otazka VALUES (" + str(id) + ",'" + question + "','','" + a + "','" + b + "','" + c + "','" + correct + "',NULL,NULL)")
    """
    print(id)
    print(question)
    print(a)
    print(b)
    print(c)
    print(correct)
    print()
    """
    i += 1

#cur.execute("DELETE FROM autoskola_otazka WHERE id != 0;")

con.commit()

con.close()