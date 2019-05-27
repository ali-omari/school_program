from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from moduls import Tools
from database import database_school
import sys


mydatabase=database_school.database_for_school()
##
my_table=Tools
##
my_editline=Tools
tool1=Tools.tool()
##
global ali_omari


class show_student(QWidget):
    def __init__(self):
        super().__init__()
        self.button()
        self.line_edit_search()
        self.label()
        self.table()
        self.windowm()


    def windowm(self):
        self.setWindowTitle('ادارة الطلاب')
        self.setGeometry(200, 115, 900, 550)
        self.setStyleSheet('background-color:rgb(64, 64, 64)')
        self.show()


    def table(self):
        self.all_data_student=mydatabase.get_student()
        self.table_student=my_table.make_tableWidget(self,10,50,880,380)
        self.table_student.add_atems(self.all_data_student)


    #######     command    #########

    def btn_add_show(self):
        import forms_app.frm_add_student


    def line_edit_search(self):
        self.val_search=my_editline.make_EDITLINE(self,120,9,600,35,15)


   ############################################33
   ############     commands      ###############
   ##############################################
    def Close(self):
        self.close()


    def get_row(self):
        import forms_app.frm_update_student
        global idval
        idval=self.table_student.get_current_row()
        print(idval)


    def delete_student(self):
        idcur=self.table_student.get_current_row()
        print(idcur)
        mydatabase.delete_stud(idcur)



    def export_pdf(self):
        fn,a=QFileDialog.getSaveFileName(self,'pdf','export pdf','PDF files(.pdf)')
        if fn != '':
            if QFileInfo(fn).suffix() =='':fn +='.pdf'
            printr=QPrinter(QPrinter.HighResolution)
            printr.setOutputFormat(QPrinter.PdfFormat)
            printr.setOutputFileName(fn)
            data=mydatabase.get_student()



    def get_search(self):
        try:
            search_data=mydatabase.get_student_where(self.val_search.get_txt_editline())
            if len(search_data)>0:
                 self.table_student.destroy_table()
                 self.table_student.add_atems(search_data)
            else:
                return


        except :
            QMessageBox.question(self, 'عذرا', 'لا يوجد هكذا عنوان لطالب', QMessageBox.Yes)











    def button(self):
        btn_add_student=tool1.make_btn('اضافة طالب',self,670,450,180,40,20,'green',self.btn_add_show)
        btn_add_student = tool1.make_btn('حذف الطالب', self, 670, 500, 180, 40, 20, 'green',self.delete_student)
        btn_add_student = tool1.make_btn('تعديل الطالب', self, 465, 450, 180, 40, 20, 'green',self.get_row)
        btn_add_student = tool1.make_btn('طباعة الطالب المحدد', self, 465, 500, 180, 40, 20, 'green')
        btn_add_student = tool1.make_btn('طباعة كل الطلاب', self, 260, 450, 180, 40, 20, 'green')
        btn_add_student = tool1.make_btn('حفظ في اكسل', self, 260, 500, 180, 40, 20, 'green')
        btn_add_student = tool1.make_btn('حفظ في pdf', self, 60, 450, 180, 40, 20, 'green',self.export_pdf)
        btn_add_student = tool1.make_btn('خروج', self, 60, 500, 180, 40, 20, 'red',self.Close)


        btn_search=tool1.make_btn('بحث',self,10,10,100,35,20,'rgb(204, 204, 0)',self.get_search)



    def label(self):
        tool1.make_lbl('ابحث عن اسم الطالب',self,725,10,160,30,18,'rgb(102, 255, 255)')







app=QApplication(sys.argv)
mywindow=show_student()
sys.exit(app.exec_())