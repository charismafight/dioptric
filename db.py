import sqlite3


def db(func):
    def sql_exc():
        con = sqlite3.connect('dioptric.db')
        con.text_factory = str
        cur = con.cursor()
        func(cur)
        cur.close()
        con.close()

    return sql_exc


@db
def get(con):
    con.execute('select * from sqlite_master')
    rows = con.fetchall()
    print(rows)
