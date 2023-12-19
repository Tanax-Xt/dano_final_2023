import sqlite3
con = sqlite3.connect("maindb.db")
cur = con.cursor()
mas = open("save.txt").readlines()
res = []
for i in mas:
    res.append(int(i[:-2]))
for i in cur.execute("SELECT ключ_клиента from Sheet0 where пол IS Null").fetchall():
    res.append(i[0])

all = cur.execute("SELECt * from Sheet0").fetchall()  # достать данные из бд
cb = []

for i in range(len(all)):
    a = all[i][41:-3]
    a = [0 if v is None else v for v in a]
    cb.append(a)
    b = all[i][7:24]
    b = [0 if v is None else v for v in b]
    all[i] = [all[i][1]] + b

print(cb[0])
for i in range(len(all)):
    for j in range(17):
        perc = 0 if all[i][j + 1] == 0 else cb[i][j] / all[i][j + 1] * 100
        if perc >= 100:
            res.append(all[i][0])
print(len(list(set(res))))