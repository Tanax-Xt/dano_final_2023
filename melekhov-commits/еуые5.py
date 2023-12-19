import matplotlib.pyplot as plt
import sqlite3
con = sqlite3.connect("maindb.db")
cur = con.cursor()
results = cur.execute("select оборот_фастфуд, активация_кэшбэка_фастфуд from Sheet0 ORDER BY оборот_фастфуд DESC").fetchall()
for i in range(len(results)):
    results[i] = (0 if results[i][0] == None else results[i][0], 0 if results[i][1] == None else 1)
dict2 = {}
for i in results:
    if i[1] == 1:
        if round(i[0] / 1000) * 1000 in dict2:
            dict2[round(i[0] / 1000) * 1000] += 1
        else:
            dict2[round(i[0] / 1000) * 1000] = 1
x = list(dict2.keys())
y = list(dict2.values())

plt.plot(x, y)
plt.show()