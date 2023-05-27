import sqlite3

def dbCleaner():
    conn = sqlite3.connect('urls.db')
    cur = conn.cursor()
    deletion = cur.execute('delete from urls')
    conn.commit()
    conn.close()
