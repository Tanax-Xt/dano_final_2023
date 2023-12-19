import pandas
import sqlite3
con = sqlite3.connect('maindb.db')
df = pandas.read_sql("SELECT * from Sheet0", con)
df.to_excel("outputwithoutvybr.xlsx")