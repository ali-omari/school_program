from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from moduls import Tools
import sys


tool1=Tools.tool()
class main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons()
        self.labels()
        self.windowf()


    def windowf(self):
        self.setWindowTitle('ادارة المدرسه')
        self.setWindowIcon(QIcon('E:\مدارس pyqt5\image\main_img.jpg'))
        lblir=QLabel(self)
        lblir.setGeometry(600,100,400,400)
        pixir=QPixmap('E:\مدارس pyqt5\image\irr.jpg')
        lblir.setPixmap(pixir)
        self.setStyleSheet('ForeColor-color:black')
        self.setGeometry(130,150,1000,500)
        self.show()



    def open_frm_signup(self):
        import forms_app.frm_signup


    def log_out(self):
        self.close()
        import forms_app.frm_login

    def open_frm_programmer(self):
        import forms_app.frm_programmer

    def open_frm_addstudent(self):
        import forms_app.frm_add_student

    def open_frm_showstudent(self):
        import forms_app.frm_show_student

    def open_frm_studentmark(self):
        import forms_app.frm_students_marks

    def open_frm_note_student(self):
        import forms_app.frm_note_student

    def buttons(self):
        ######    This buttons for student    #######
        btn_add_student=tool1.make_btn('اضافة طالب جديد',self,50,120,150,50,12,'Purple',self.open_frm_addstudent)
        btn_management_student=tool1.make_btn('ادارة الطلاب',self,50,185,150,50,12,'Purple',self.open_frm_showstudent)
        btn_marks_student=tool1.make_btn('درجات الطلاب',self,50,250,150,50,12,'Purple',self.open_frm_studentmark)
        btn_notes_student=tool1.make_btn('ملاحظات حول الطلاب',self,50,315,150,50,12,'Purple',self.open_frm_note_student)
        btn_information_student=tool1.make_btn('المعلومات الكامله حول الطالب',self,50,375,150,50,12,'Purple')
        btn_identity_student=tool1.make_btn('هوية الطالب',self,50,440,150,50,12,'Purple')

        ######    This buttons for student    #######
        btn_directer=tool1.make_btn('المدير',self,240,120,150,50,14,'Purple')
        btn_directer = tool1.make_btn('اضافة مدرس جديد', self, 240, 185, 150, 50, 14, 'Purple')
        btn_directer = tool1.make_btn('ادارة المدرسين', self, 240, 250, 150, 50, 14, 'Purple')
        btn_directer = tool1.make_btn('معلومات المدرسين', self, 240, 315, 150, 50, 14, 'DimGray')
        btn_directer = tool1.make_btn('مرشدين الصفوف', self, 240, 375, 150, 50, 14, 'Purple')



        ######    this buttons for setting    #######

        #btn_signin=tool1.make_btn('تسجيل الدخول',self,420,120,150,50,14,'Purple')

        btn_add_password=tool1.make_btn('اضافة كلمة سر جديدة',self,420,185,150,50,14,'Purple',self.open_frm_signup)
        btn_log_out=tool1.make_btn('تسجيل خروج',self,420,250,150,50,14,'Purple',self.log_out)
        btn_about_programmer=tool1.make_btn('عن المبرمج',self,420,315,150,50,14,'Purple',self.open_frm_programmer)









    def labels(self):
        lbl_student=tool1.make_lbl('الطلاب',self,55,30,100,100,20,'red')

        lbl_teachers=tool1.make_lbl('المدرسين',self,240,30,130,100,20,'red')

        lbl_setting=tool1.make_lbl('الاعدادات',self,430,30,110,100,20,'red')







app=QApplication(sys.argv)
Window=main_window()
sys.exit(app.exec_())