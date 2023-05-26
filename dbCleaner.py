import sqlite3

conn = sqlite3.connect('urls.db')
cur = conn.cursor()
deletion = cur.execute('delete from urls')
conn.commit()
conn.close()
