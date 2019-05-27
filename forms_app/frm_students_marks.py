from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from moduls import Tools
import sys


tool1=Tools.tool()
class main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.windowf()



    def windowf(self):
        self.setWindowTitle('ادارة المدرسه')
        self.setWindowIcon(QIcon('E:\مدارس pyqt5\image\main_img.jpg'))
        self.setStyleSheet('Background-color:rgb(119, 119, 60)')
        self.setGeometry(130,150,1000,500)
        self.show()




#app=QApplication(sys.argv)
mywindow=main_window()
#sys.exit(app.exec_())