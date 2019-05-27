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
        self.setWindowTitle('اضافة طالب جديد')
        self.setStyleSheet('Background-color:black')
        self.setGeometry(200,200,480,220)
        self.show()


    def label(self):
        self.lbl_title=tool1.make_lbl('تسجيل الدخول',self,150,10,164,50,30,'rgb(0, 255, 0)')
        self.lbl_user=tool1.make_lbl('اسم المستخدم',self,340,70,120,30,20,'rgb(255, 0, 255)')
        self.lbl_password = tool1.make_lbl('كلمة السر', self, 340, 120, 120, 30, 20, 'rgb(255, 0, 255)')

    def edit_line(self):
        self.editline_user=tool2.make_EDITLINE(self,30,70,300,35,15)

        self.editline_password = tool2.make_EDITLINE(self, 30, 120, 300, 35, 15)


    #######      command       ##########
    def Close(self):
        self.close()


    def login_user(self):
        user1=self.editline_user.get_txt_editline()
        password1=self.editline_password.get_txt_editline()
        try:
            if len(user1)>0:
                if len(password1)>0:
                    check=my_database.check_user(user1,password1)
                    if check==1:
                        import forms_app.frm_main
                        self.Close()

                    elif check==2:

                       tool1.make_messagebox(self,'كلمة السر غير صحيحه','عذرا كلمة السر غير صحيحه يرجى اعادة المحاولة')
                    else:
                        tool1.make_messagebox(self,'اسم المستخدم وكلمة السر غير صحيحين','عذرا اسم المستخدم وكلمة السر غير صحيحين يرجى اعادة المحاولة')

        except Exception as ex :
            print(ex)

  #  def login_user(self):
   #     try:
    #        user1 = self.editline_user.get_txt_editline()
     #       password1=self.editline_password.get_txt_editline()
      #      ifd=my_database.check_user(user1,password1)
       #     if ifd==1:
        #    elif ifd==2:
         #      QMessageBox.question(self, 'كلمة السر غير صحيحة',
          #                                   'عذرا كلمة السر غير صحيحة يرجى اعادة المحاولة', QMessageBox.Yes)
#
 #           else:
  #             QMessageBox.question(self, 'اسم المستخدم وكلمة السر غير صحيحين',
   #                                          'عذرا اسم المستخدم وكلمة السر غير صحيحين يرجى اعادة المحاولة', QMessageBox.Yes)
    #    except Exception as ex:
     #       print(ex)


    def button(self):
        self.btn_line=tool1.make_btn('',self,1,45,1000,5,15)

        self.btn_login=tool1.make_btn('دخول',self,30,170,100,40,15,'rgb(0, 153, 255)',self.login_user)

        self.btn_close=tool1.make_btn('خروج',self,145,170,100,40,15,'rgb(255, 0, 255)',self.Close)




app=QApplication(sys.argv)
mywindow=login_p()
sys.exit(app.exec_())