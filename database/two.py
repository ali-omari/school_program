import sqlite3


###########
class school_data():
    def __init__(self):
        self.conn=sqlite3.connect('school_database.db')
        self.conn.execute('create table if not exists student(ID INTEGER NOT NULL PRIMARY KEY ASC,'
                          'name varchar(50),class varchar(50),born varchar(20),phone varchar(11))')

        self.conn.commit()

