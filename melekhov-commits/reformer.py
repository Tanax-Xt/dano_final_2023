import sqlite3, pandas, os
h = int(input("""1-sql -> sql_filtred
2-sql->xlsx
3-sql->xlsx_filtred
4-sql_filtred->xlsx_filtred"""))
if h == 1:
    try:
        os.remove("maindb_filtred.db")
    except BaseException:
        pass
    os.system("copy maindb.db maindb_filtred.db")
    con = sqlite3.connect("maindb_filtred.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Sheet0 where is_vybr=1")
    con.commit()
if h == 2:
    con = sqlite3.connect("maindb.db")
    pandas.read_sql("SELECT * FROM Sheet0", con).to_excel("maindb.xlsx")
if h == 3:
    try:
        os.remove("maindb_filtred.db")
    except BaseException:
        pass
    os.system("copy maindb.db maindb_filtred.db")
    con = sqlite3.connect("maindb_filtred.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Sheet0 where is_vybr=1")
    con.commit()
    print("переписываем")
    a = pandas.read_sql("SELECT * FROM Sheet0", con)
    print("прочитали")
    a.to_excel("maindb_filtred.xlsx")