from sqlite3 import Cursor
import pymysql

db = pymysql.Connect(host='localhost',
                     port=3306,
                     user='root',
                     password='M@rlagnwjd2468@',
                     db='brjm_db',
                     charset='utf8')

cursor = db.cursor()




