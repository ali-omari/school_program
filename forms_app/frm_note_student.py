from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from moduls import Tools
from database import database_school
import sys

########
mydatabase=database_school.database_for_school()
######
my_editline=Tools
######
tool1=Tools.tool()
########
my_txtedit=Tools
########
class note_student(QWidget):
    def __init__(self):
        super().__init__()


        self.label()
        self.txtedit()
        self.comboBOx()
        self.editline()
        self.button()
        self.windowf()






    def windowf(self):
        self.setWindowTitle('اضافة ملاحظة لطالب')
        self.setStyleSheet('Background-color:rgb(102, 102, 51)')
        self.setGeometry(200,100,700,550)
        self.show()



    def txtedit(self):
        self.txedit=my_txtedit.make_textedit(self,10,150,680,250)

    def label(self):
        self.lbl_Absences=tool1.make_lbl('عدد الغيابات',self,585,420,100,50,17)

        self.lbl_kick = tool1.make_lbl('عدد مرات الفصل', self, 150, 420, 150, 50, 17)

        self.lbl_name=tool1.make_lbl('الاسم',self,645,15,40,30,20)
        self.lbl_class = tool1.make_lbl('الصف', self, 330, 15, 50, 30, 20)

        self.lbl_note=tool1.make_lbl('كتابة الملاحظات ',self,280,100,130,30,20)




    def editline(self):
        self.linedit_Absences=my_editline.make_EDITLINE(self,420,430,150,35,15)

        self.linedit_kick = my_editline.make_EDITLINE(self, 20, 430, 150, 35, 15)

        self.editline_name=my_editline.make_EDITLINE(self,420,17,200,35,15)

        #self.editline_class=my_editline.make_EDITLINE(self,100,17,200,35,15)

    def save_note(self):
        name_student=self.editline_name.get_txt_editline()
        class_studnet=self.combo_class.get_txtcombo()
        absences_student=self.linedit_Absences.get_txt_editline()
        kick_student=self.linedit_kick.get_txt_editline()
        not_student=self.txedit.get_text_txtedit()
        if len(self.txedit.get_text_txtedit()) >1:
            if len(self.editline_name.get_txt_editline()) >1:
                mydatabase.insert_note_student(name_student,class_studnet,not_student,absences_student,kick_student)
                print('تم حفظ الملاحظة')

            else:
                print('حدث خطا')


    def button(self):
        self.btn_save=tool1.make_btn('حفظ',self,190,490,130,45,17,'rgb(0, 153, 0)',self.save_note)
        self.btn_line1=tool1.make_btn('',self,-1,411,1000,10,15,'rgb(0, 51, 102)')
        self.btn_line2= tool1.make_btn('', self, -1, 470, 1000, 10, 15, 'rgb(0, 51, 102)')
        self.btn_line3=tool1.make_btn('', self, -1, 80, 1000, 10, 15, 'rgb(0, 51, 102)')
        self.btn_close = tool1.make_btn('خروج', self, 350, 490, 130, 45, 17,'rgb(255, 0, 102)')


    def comboBOx(self):
        self.combo_class=my_editline.make_COMBOBOX(self,100,17,200,35)



#app=QApplication(sys.argv)
mywindow=note_student()
#sys.exit(app.exec_())
