import urllib.request
import sqlite3


conn = sqlite3.connect('urls.db')
curs = conn.cursor()
links = curs.execute('select url from urls').fetchall()
my_tuple = ()
for link in links:
    my_tuple += link


for i in my_tuple:
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
    elif '@.*?.' in i:
        print(i)

    