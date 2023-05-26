import urllib.request
import sqlite3
import re

with open('dbCleaner.py', 'r') as file2:
    exec(file2.read())

try:
    print('start')

    web = 'https://www.foxnews.com/'

    def my_function(item):
        get_url = urllib.request.urlopen(item)
        data = get_url.read()
        data_string = data.decode('utf-8', errors = 'ignore')
        link = re.findall('https.*?"', data_string)
        conn = sqlite3.connect('urls.db')
        cur = conn.cursor()
        for i in link:
            i = i.replace('"', "")
            cur.execute('insert into urls (url) values(?)', [i])
            conn.commit()
        conn.close()

    my_function(web)
    
    with open('searchMedia.py', 'r') as file:
        exec(file.read())

except:
    print('some problem')

finally:
    print('end')








    


