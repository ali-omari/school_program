import sqlite3


class database_for_school():
    def __init__(self):
        self.conn=sqlite3.connect('mySCHOOL.db')
        self.conn.execute('create table if not exists students(id INTEGER NOT NULL PRIMARY KEY ASC,name varchar(50),classes varchar(50),born varchar(20),phone varchar(11))')
        self.conn.execute('create table if not exists note_student(name varchar(50),classes varchar(50),note Text,Absences varchar(50),kick varchar(50))')
        self.conn.execute('create table if not exists users_teachers(name VARCHAR(50),password VARCHAR(50))')
        self.conn.execute('create table if not exists teachers(id INTEGER NOT NULL PRIMARY KEY ASC,name VARCHAR(50),type varchar(50),born varchar(50),phone varchar(50))')

        self.conn.commit()

    def insert_student(self,ID,Name,Classes,Born,Phone):
        self.conn.execute('insert into students(id,name,classes,born,phone) values(?,?,?,?,?)',(ID,Name,Classes,Born,Phone))
        self.conn.commit()


    def get_student(self):
        try:
           cur=self.conn.execute('select * from students')
           data=cur.fetchall()
           print('ali omari yes')
           return data
        except Exception as ex:
            print(ex)


    def update_student(self,NAME,CLASSES,BORN,PHONE,ID=1):
        try:
            self.conn.execute('update students set name={},classes={},born={},phone={} where id ={}'.format(NAME,CLASSES,BORN,PHONE,ID))
            print('تم التعديل بنجاح')

        except Exception as ex:
            print(ex)


    def delete_stud(self,ID):
        try:
            self.conn.execute('delete from students where id={}'.format(ID))
            self.conn.commit()
            print('تم الحذف')
        except Exception as ex:
            print(ex)

    def get_student_where(self,name):
        try:
            cur=self.conn.execute('select * from students where name={}'.format("'"+name+"'"))
            data=cur.fetchall()
            self.conn.commit()
            return data
        except Exception as ex:
            print(ex)


    def insert_note_student(self,NAME,CLASS,NOTE,Absences,KICK):
        try:
            self.conn.execute('insert into note_student(name,classes,note,Absences,kick) values(?,?,?,?,?)',(NAME,CLASS,NOTE,Absences,KICK))
            self.conn.commit()
        except Exception as ex:
            print(ex)



    def get_users_login(self):
        try:
            cur=self.conn.execute('select * from users_teachers')
            all_data=cur.fetchall()
            return all_data
        except Exception as ex:
            print(ex)

    def check_user(self,User,passWord):
        try:
            data=self.get_users_login()
            username=[]
            password=[]
            for i in data:
                username.append(i[0])
                password.append(i[1])
            j=0
            while j<len(username):
                if username[j]==User:
                    if password[j]==passWord:
                        return 1

                    else:
                        return 2
                else:
                    j+=1
                    continue
                    return 3

        except Exception as ex:
            print(ex)
            return


    def add_user(self,name,password):
        try:
            self.conn.execute('insert into users_teachers(name,password) values(?,?)',(name,password))
            self.conn.commit()
            return 1

        except Exception as ex:
            print(ex)


    def insert_teacher(self,ID,NAME,TYPE,BORN,PHONE):
        try:
            self.conn.execute('insert into teachers(id,name,type,born,phone) values (?,?,?,?,?)',(ID,NAME,TYPE,BORN,PHONE))
            self.conn.commit()
            return 1

        except Exception as ex:
            print(ex)


    def get_teacher(self):
        try:
            cur=self.conn.execute('select * from teachers')
            data=cur.fetchall()
            return data
        except Exception as ex:
            print(ex)


    def get_teacher_where(self,name):
        try:
            cur=self.conn.execute('select * from teachers where name={}'.format("'"+name+"'"))
            data=cur.fetchall()
            self.conn.commit()
            return data
        except Exception as ex:
            print(ex)



    def delete_teacher(self,ID):
        try:
            self.conn.execute('delete from teachers where id={}'.format(ID))
            self.conn.commit()
            print('تم الحذف')
        except Exception as ex:
            print(ex)


    def update_teacher(self,NAME,TYPE,BORN,PHONE,ID=1):
        try:
            self.conn.execute('update teachers set name={},type={},born={},phone={} where id ={}'.format(NAME,TYPE,BORN,PHONE,ID))
            print('تم التعديل بنجاح')

        except Exception as ex:
            print(ex)





Data_school=database_for_school()

