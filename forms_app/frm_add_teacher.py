from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from moduls import Tools
from database import database_school
import sys


mydatabase=database_school.database_for_school()

my_editline=Tools
tool1=Tools.tool()
class add_student(QWidget):
    def __init__(self):
        super().__init__()
        self.labels()
        self.button()
        self.picture()
        self.line_edit()
        self.windowf()






    def windowf(self):
        self.setWindowTitle('اضافة طالب جديد')
        #self.setStyleSheet('Background-color:gray')
        self.setGeometry(200,200,600,280)
        self.show()


    def labels(self):
        lbl_id_teacher=tool1.make_lbl('معرف المدرس',self,490,-10,100,100,15)
        lbl_name_teacher = tool1.make_lbl('اسم المدرس', self, 490, 30, 100, 100, 15)
        lbl_type_teacher = tool1.make_lbl('الماده', self, 490, 65, 100, 100, 15)
        lbl_born_teacher = tool1.make_lbl('المواليد', self, 490, 95, 105, 100, 15)
        lbl_phone_teacher = tool1.make_lbl('رقم الهاتف', self, 490, 135, 100, 100, 15)


    def line_edit(self):
        self.line_id = Tools.make_EDITLINE(self, 225, 30, 250, 30, 14)
        self.line_name=Tools.make_EDITLINE(self,225,68,250,30,14)
        self.line_type = Tools.make_EDITLINE(self,225,110,250,30,14)
        self.line_born = Tools.make_EDITLINE(self,225,150,250,30,14)
        self.line_phone = Tools.make_EDITLINE(self,225,190,250,30,14)






    def picture(self):
        pix_picture=tool1.make_label_image(self,15,22,200,200)

    def save_newstudent(self):
        try:

            idd=self.line_id.get_txt_editline()
            namee=self.line_name.get_txt_editline()
            typee=self.line_type.get_txt_editline()
            bornn=self.line_born.get_txt_editline()
            phonee=self.line_phone.get_txt_editline()

            mydatabase.insert_teacher(idd,namee,typee,bornn,phonee)

            QMessageBox.question(self, 'تم الحفظ بنجاح',
                                 'تم الحفظ', QMessageBox.Yes)

        except Exception as ex:
            print(ex)


    def Close(self):
        self.close()

    def button(self):
        btn_save_teacher=tool1.make_btn('حفظ',self,20,235,100,35,15,'green',self.save_newstudent)
        btn_cancel_teacher=tool1.make_btn('خروج',self,130,235,100,35,15,'red',self.Close)












app=QApplication(sys.argv)
mywindow=add_student()
sys.exit(app.exec_())