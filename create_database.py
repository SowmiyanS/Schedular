import sqlite3
conn=sqlite3.connect("schedular.db")
cur=conn.cursor()
cur.execute("CREATE TABLE if not exists Tasks(id AUTOINCREMENT,score real,name text,descpt text,time text,reqmnts text,internet boolean,readable boolean,writeable boolean,otherreq boolean,instruction text)")
conn.commit()
conn.close()