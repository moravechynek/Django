import sqlite3

con = sqlite3.connect('../website/db.sqlite3')
cur = con.cursor()
f = open('../scrapers/etesty.csv', 'r')
i = 0
f.readline()
while i < 928: #928
    line = f.readline().split(';')
    id = i + 1
    question = line[0]
    if line[1]:
        image = 'otazky/' + line[1]
    else: image = line[1]
    a = line[2]
    b = line[3]
    c = line[4]
    correct = line[5][0] # not '\n'

    cur.execute("INSERT INTO autoskola_otazka VALUES (" + str(id) + ",'" + question + "','" + image + "','" + a + "','" + b + "','" + c + "','" + correct + "',NULL,NULL)")
    print(id)
    print(question)
    print(image)
    print(a)
    print(b)
    print(c)
    print(correct)
    print()
    i += 1

#cur.execute("DELETE FROM autoskola_otazka WHERE id != 0;")

con.commit()

con.close()