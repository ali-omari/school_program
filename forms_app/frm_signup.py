from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from moduls import Tools
from database import database_school
import sys


tool1=Tools.tool()
####
tool2=Tools
#######
my_database=database_school.database_for_school()
class login_p(QWidget):
    def __init__(self):
        super().__init__()
        self.button()
        self.label()
        self.edit_line()
        self.windowf()






    def windowf(self):
        self.setWindowTitle('اضافة مستخدم جديد')
        self.setStyleSheet('Background-color:black')
        self.setGeometry(200,200,480,220)
        self.show()


    def label(self):
        self.lbl_title=tool1.make_lbl('اضافة مستخدم جديد',self,120,10,250,50,30,'rgb(0, 255, 0)')
        self.lbl_user=tool1.make_lbl('اسم المستخدم',self,340,70,120,30,20,'rgb(255, 0, 255)')
        self.lbl_password = tool1.make_lbl('كلمة السر', self, 340, 120, 120, 30, 20, 'rgb(255, 0, 255)')

    def edit_line(self):
        self.editline_user=tool2.make_EDITLINE(self,30,70,300,35,15)

        self.editline_password = tool2.make_EDITLINE(self, 30, 120, 300, 35, 15)


    def Close(self):
        self.close()

    def add_new_user(self):
        user1=self.editline_user.get_txt_editline()
        password1=self.editline_password.get_txt_editline()
        if len(user1) > 0:
            if len(password1) > 0:
                 resuelt=my_database.add_user(user1,password1)
                 if resuelt ==1:
                     tool1.make_messagebox(self,'اضافة مستخدم جديد','تم اضافة مستخدم جديد')
            else:
                tool1.make_messagebox(self, 'اضافة مستخدم جديد', 'يرجى ادخال كلمة السر')

        else:
            tool1.make_messagebox(self, 'اضافة مستخدم جديد', 'يرجى ادخال المعاومات')

    def button(self):
        self.btn_line=tool1.make_btn('',self,1,45,1000,5,15)

        self.btn_login=tool1.make_btn('حفظ',self,30,170,100,40,15,'rgb(0, 153, 255)',self.add_new_user)

        self.btn_close=tool1.make_btn('خروج',self,145,170,100,40,15,'rgb(255, 0, 255)',self.Close)




#app=QApplication(sys.argv)
mywindow=login_p()
#sys.exit(app.exec_())