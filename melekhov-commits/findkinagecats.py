import sqlite3
a = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}}
def mid(a):
    return 0 if len(a) == 0 else sum(a) / len(a)

con = sqlite3.connect("maindb -- копия.db")
cur = con.cursor()
tables = list(list(zip(*cur.execute("Pragma table_info('Sheet0')").fetchall()))[1][7:24])
for i in range(len(tables)):
    tables[i] = tables[i].replace("оборот_", "")
for i in range(5):
    print("СЕЙЧАС ИЩЕМ В КАТЕГОРИИ " + str(i))
    all = cur.execute("SELECT * from Sheet0 where int_cat=" + str(i)).fetchall()
    for n in range(17):
        mids1 = []
        mids2 = []
        mids3 = []
        for j in range(0, len(all), 6):
            act = []
            not_act = []
            not_add = []
            for k in range(6):
                data_form = all[k + j][7 + n]
                data_form = 0 if data_form == None else data_form
                cashcheck = all[k + j][24 + n]
                if cashcheck == 1:
                    act.append(data_form)
                elif cashcheck == 0:
                    not_act.append(data_form)
                elif cashcheck == None:
                    not_add.append(data_form)
            mids1.append(mid(act))
            mids2.append(mid(not_act))
            mids3.append(mid(not_add))
        try:
            k = mid(mids1) / mid([mid(mids2), mid(mids3)])
        except ZeroDivisionError:
            k = 0
        a[i][tables[n]] = k
print(a)