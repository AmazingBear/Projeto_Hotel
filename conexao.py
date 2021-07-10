import pymysql

def conectar():
    conn = pymysql.connect(
        host= 'localhost',
        user= 'root',
        password = '',
        database= 'db_hotel',
        cursorclass= pymysql.cursors.DictCursor,
    )
    return conn