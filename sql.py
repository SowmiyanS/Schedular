import sqlite3
conn=sqlite3.connect("schedular.db")
cur = conn.cursor()
cur.execute("SELECT * FROM Tasks")
records=cur.fetchall()
conn.commit()
conn.close()
word = ''

count=0
for i in records:
	count=count+1
print(count)

for tuple in records:
	word=f'{tuple}' #tuple[i]
	print('')
	print(word)
	