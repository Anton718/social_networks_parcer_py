import urllib.request
import sqlite3
import re
import dbCleaner
import searchMedia

dbCleaner.dbCleaner()

try:
    print('start')

    web = 'https://www.avtosushi.ru'

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
    
    searchMedia.searchLinks()

except:
    print('some problem')

finally:
    print('end')








    


