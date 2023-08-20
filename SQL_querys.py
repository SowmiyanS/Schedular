import sqlite3
conn=sqlite3.connect("schedular.db")
cur = conn.cursor()

#CREATE A TABLE TASKS

#cur.execute("CREATE TABLE if not exists Tasks(tid INTEGER PRIMARY KEY AUTOINCREMENT,score real,name text,descpt text,lastpausedtime text,cooltime text,totaltimetaken text,state boolean,reqmnts text,internet boolean,readable boolean,writeable boolean,otherreq boolean,instruction text) ")

gscore=int(10)
gname="First Task"
gdescpt="Some description about first task"
glastpausedtime="yyyy-mm-dd-hh-mnmn-ss"
gcooltime="hh-mm-ss"
gtotaltimetaken="hh-mm-ss"
gstate=1
greqmnts="We write this if we check otherreq checkbox"
ginternet=1
greadable=1
gwriteable=1
gotherreq=1
ginstruction="This is the best instruction in the world to do this task most efficiently rapidly and manyly!!!"

#INSERT VALUES INTO TASKS TABLE

#cur.execute("INSERT INTO Tasks (score,name,descpt,lastpausedtime,cooltime,totaltimetaken,state,reqmnts,internet,readable,writeable,otherreq,instruction) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(gscore,gname,gdescpt,glastpausedtime,gcooltime,gtotaltimetaken,gstate,greqmnts,ginternet,greadable,gwriteable,gotherreq,ginstruction))

#SELECT * FROM TASKS AND PRINT

#cur.execute("SELECT * FROM Tasks")
#records=cur.fetchall()
#count=0
#for i in records:
#	count=count+1
#print(count)
#for tuple in records:
#	word=f'{tuple}' #tuple[i]
#	print('')
#	print(word)

#CLOSE THE CONNECTION
	
conn.commit()
conn.close()
