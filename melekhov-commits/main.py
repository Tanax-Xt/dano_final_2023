import pandas as pd
import sqlite3

db = sqlite3.connect('maindb.db') #импорт базы данных
cur = db.cursor()
cur.execute(f"""UPDATE Sheet0
    SET is_vybr=0
    WHERE is_vybr=1""") #убрать все пометки выбросов для повторного выбора
db.commit()
all = cur.execute("SELECt * from Sheet0").fetchall() #достать данные из бд
for i in range(len(all)):
    all[i] = all[i][7:24] + all[i][41:-3] #выбрать только столбцы с деньгами(оборот/кешбек), если нет колонки to_vybr, уб
    all[i] = [0 if j == None else j for j in all[i]] #заменяем None на 0
to_vibr = []
for i in zip(*all): # перебор по каждой из категорий
    dicti = {a:i[a] for a in range(len(i))} #представляем в виде словаря для сохранения изначальных id после сортировки
    dict_sorted = sorted(dicti.items(), key=lambda item: item[1], reverse=True) #сортируем
    if len(dict_sorted) % 2 == 1:
        med = dict_sorted[len(dict_sorted) // 2][1]
    else:
        med = (dict_sorted[len(dict_sorted) // 2][1] + dict_sorted[len(dict_sorted) // 2 - 1][1]) / 2 #находим медиану
    print(med)
    for i in range(len(dict_sorted) - 1):
        difftonext = dict_sorted[i][1] - dict_sorted[i + 1][1]  # расстояние до следующего элемента
        diffnexttomed = abs(dict_sorted[i + 1][1] - med) #расстояние от следующего элемента до медианы
        if 0.2 * diffnexttomed < difftonext and difftonext > 1000: # первое условие - находим выброс, если отрыв от следующего элемента больше половины от расстояния следущего элемента до медианы. это значит наш элемент слишком далеко, следовательно выброс. второе условие, чтобы не было ошибочных активаций при значениях, близких к медиане
            to_vibr.append(cur.execute(f"SELECT ключ_клиента from Sheet0 where id={str(dict_sorted[i][0])}").fetchone()[0]) # добавляем id человека(не записи) в список выбросов
    print(to_vibr)
for i in cur.execute("SELECT ключ_клиента from Sheet0 where пол IS Null").fetchall():
    to_vibr.append(i[0])


import sqlite3
con = sqlite3.connect("maindb.db")
cur = con.cursor()
all = cur.execute("SELECt * from Sheet0").fetchall()  # достать данные из бд
cb = []

for i in range(len(all)):
    a = all[i][41:-3]
    a = [0 if v is None else v for v in a]
    cb.append(a)
    b = all[i][7:24]
    b = [0 if v is None else v for v in b]
    all[i] = [all[i][1]] + b

for i in range(len(all)):
    for j in range(17):
        perc = 0 if all[i][j + 1] == 0 else cb[i][j] / all[i][j + 1] * 100
        if perc >= 100:
            to_vibr.append(all[i][0])
print(to_vibr)

for i in to_vibr:
    cur.execute("UPDATE Sheet0 set is_vybr=1 where ключ_клиента=" + str(i))
con.commit()