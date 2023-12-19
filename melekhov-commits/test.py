import sqlite3
import pandas
a = {'аптеки': 2.0681341323941957, 'рестораны': 2.01997616558181, 'одежда_и_обувь': 2.2093409526539243, 'автоуслуги': 2.506924242464986, 'супермаркеты': 0.9597325278700365, 'такси': 1.2643240695971807, 'красота': 1.494908284552979, 'развлечения': 1.5462770834468618, 'жд_билеты': 2.471745514213426, 'образование': 2.1788572001149635, 'дом_и_ремонт': 0.801719915097952, 'спорттовары': 1.762281461383755, 'животные': 1.6472171710532537, 'цветы': 0.9381610110618431, 'фастфуд': 0.042375274883844675, 'каршеринг': 1.2857503499624807, 'аренда_авто': 0.4641838868218006}
con = sqlite3.connect("maindb--no_vybr.db")
cur = con.cursor()
tables = list(list(zip(*cur.execute("Pragma table_info('Sheet0')").fetchall()))[1][7:24])
for i in range(len(tables)):
    tables[i] = tables[i].replace("оборот_", "")
oborot = cur.execute("SELECT * from Sheet0").fetchall()
print(tables)
oborot = list(zip(*oborot))[7:24]
for i in range(len(oborot)):
    j = [0 if v is None else v for v in oborot[i]]
    print(tables[i], (sum(j) / len(j)) / a[tables[i]])