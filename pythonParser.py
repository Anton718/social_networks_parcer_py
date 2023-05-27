import urllib.request
import sqlite3
import re

conn = sqlite3.connect('urls.db')
cur = conn.cursor()
cur.execute('delete from urls')
conn.commit()
conn.close()

try:
    print('start')

    web = 'https://captainbills.com/'

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
    
    conn = sqlite3.connect('urls.db')
    curs = conn.cursor()
    links = curs.execute('select url from urls').fetchall()
    my_tuple = ()
    for link in links:
        my_tuple += link
    for i in my_tuple:
        if len(i) < 80:
            if 'insta' in i:
                print(i)
            elif 'facebook' in i:
                print(i)
            elif 'youtube' in i:
                print(i)
            elif 'linkedin' in i:
                print(i)
            elif 'twitter' in i:
                print(i)
            elif 'vkontakte' in i:
                print(i)
            elif 'vk.ru' in i:
                print(i)
            elif 'vk.com' in i:
                print(i)
            elif 'ok.ru' in i:
                print(i)
            elif 'odnoklass' in i:
                print(i)
            elif 'telegram' in i:
                print(i)
            elif 'whatsapp' in i:
                print(i)
            elif 'tiktok' in i:
                print(i)

except:
    print('error')

finally:
    print('end')








    


