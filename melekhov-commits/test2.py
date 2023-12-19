import sqlite3
import matplotlib.pyplot as plt
import numpy as np
con = sqlite3.connect("maindb.db")
cur = con.cursor()
data = cur.execute("SELECT * FROM Sheet0").fetchall()
tables = list(zip(*cur.execute("Pragma table_info('Sheet0')").fetchall()))[1]
koefs = []
for n in range(17):
    mids1 = []
    mids2 = []
    mids3 = []
    for i in range(0, len(data), 6):
        was_act = []
        was_not_act = []
        was_not_add = []
        for j in range(6):
            if i + j < len(data):
                data_form = data[i+j][7+n]
                data_form = 0 if data_form==None else data_form
                if data[i+j][24+n] == 1:
                    was_act.append(data_form)
                elif data[i+j][24+n] == 0:
                    was_not_act.append(data_form)
                else:
                    was_not_add.append(data_form)
        mid1 = 0 if was_act == [] else sum(was_act) / len(was_act)
        mid2 = 0 if was_not_act == [] else sum(was_not_act) / len(was_not_act)
        mid3 = 0 if was_not_add == [] else sum(was_not_add) / len(was_not_add)
        mids1.append(mid1)
        mids2.append(mid2)
        mids3.append(mid3)
        # print(was_act, was_not_act, was_not_add, mid1, mid2, mid3)
    midls = [sum(mids1) / len(mids1), sum(mids2) / len(mids2), sum(mids3) / len(mids3)]
    koef = 0 if midls[1] + midls[2] == 0 else midls[0] / ((midls[1] + midls[2]) / 2)
    koefs.append(koef)
    print(tables[7 + n], midls)
print(koefs)
all = list(zip(*cur.execute("SELECT * FROM Sheet0").fetchall()))
takver = []
for i in range(17):
    co0 = 0
    co1 = 0
    for j in all[24 + i]:
        if j == 0:
            co0 += 1
        if j == 1:
            co1 += 1
    takver.append(co1/(co0+co1)*100)
    print(tables[24+i], co0, co1, co1/(co0+co1)*100)
tables = list(tables[24:41])
for i in range(len(tables)):
    tables[i] = tables[i].replace('активация_кэшбэка_', "")
print(tables)
print(dict(zip(tables, koefs)))