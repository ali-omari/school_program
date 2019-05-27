from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from moduls import Tools
from database import database_school
import sys

tool1=Tools.tool()


class programmer(QWidget):
    def __init__(self):
        super().__init__()
        self.label()
        self.windowf()






    def windowf(self):
        self.setWindowTitle('اضافة طالب جديد')
        self.setStyleSheet('Background-color:rpg(51, 51, 77)')
        self.setGeometry(200,200,550,300)
        self.show()



    def label(self):
        lbl_name=tool1.make_lbl('الاسم',self,470,15,70,30,25,'rgb(204, 255, 153)')
        lbl_name_val=tool1.make_lbl('علي عبد الخالق كاظم ابراهيم',self,170,13,300,35,25,'rgb(255, 102, 255)')

        lbl_phone = tool1.make_lbl('الهاتف', self, 442, 65, 100, 30, 25, 'rgb(204, 255, 153)')
        lbl_phone_val = tool1.make_lbl('07513964841', self, 250, 65, 200, 35, 25, 'rgb(255, 102, 255)')

        lbl_place = tool1.make_lbl('العنوان', self, 450, 112, 90, 30, 25, 'rgb(204, 255, 153)')
        lbl_place_val = tool1.make_lbl('العراق/الناصريه/الاصلاح', self, 200, 112, 250, 35, 25, 'rgb(255, 102, 255)')

        lbl_facebook = tool1.make_lbl('فيسبوك', self, 450, 155, 90, 30, 25, 'rgb(204, 255, 153)')
        lbl_facebook_val = tool1.make_lbl('علي العمري', self, 170, 155, 250, 35, 25, 'rgb(255, 102, 255)')

        lbl_info1=tool1.make_lbl('طالب في المرحله الاعداديه....',self,-50,200,550,40,25,'rgb(255, 0, 102)')
        lbl_info2=tool1.make_lbl('محب للبرمجه وعاشق لها',self,-20,240,300,40,25,'rgb(255, 0, 102)')

        btn_line=tool1.make_btn('',self,-1,195,1000,8,15,'rgb(102, 255, 255)')

        lbl_image=tool1.make_label_image(self,30,40,100,100,'E:\مدارس pyqt5\image\imgres.jpg')
app=QApplication(sys.argv)
mywindow=programmer()
sys.exit(app.exec_())