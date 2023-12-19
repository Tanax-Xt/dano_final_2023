import numpy as np


def remove_outliers_iqr(data):
    # Вычисление первого (Q1) и третьего (Q3) квартилей
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)

    # Вычисление интерквартильного расстояния (IQR)
    IQR = Q3 - Q1

    # Определение границ для определения выбросов
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Фильтрация данных, оставляя только те значения, которые находятся в пределах границ
    filtered_data = []
    for value in range(len(data)):
        if not(lower_bound <= data[value] <= upper_bound):
            filtered_data.append(value)

    return filtered_data


import sqlite3
con = sqlite3.connect("maindb.db")
cur = con.cursor()
all = list(zip(*cur.execute("SELECT * from Sheet0").fetchall()))
all = all[7:24] + all[41:41+17]
to_vybr = []
for i in all:
    i = [v if v else 0 for v in i]
    to_vybr += remove_outliers_iqr(i)
all = cur.execute("SELECT id, ключ_клиента From Sheet0").fetchall()
to_vybr = list(set(to_vybr))
keys = []
for i in all:
    if i[0] in to_vybr:
        keys.append(i[1])
print(len(list(set(keys))))