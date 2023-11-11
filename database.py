import sqlite3

connection = sqlite3.connect("itstep.sl3", 5)

cur = connection.cursor()

# cur.execute("UPDATE users SET email='ad@.a' where rowid=3")
cur.execute("DELETE FROM users where rowid=3")
connection.commit()

res = cur.fetchall()
# print(connection)
print(res)

connection.close()
