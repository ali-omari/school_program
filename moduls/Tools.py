from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


########

class tool():
    def __init__(self):
        return

    def Defualt(self):
        print('ali omari')

    def make_btn(self,name,window,x,y,h,w,fontsize,color='rgb(255, 255, 255)',Command=Defualt):
        btn=QPushButton(name,window)
        btn.setGeometry(x,y,h,w)
        btn.setStyleSheet('Background-color:{}'.format(color))
        btn.setFont(QFont('Andalus',fontsize))
        btn.clicked.connect(Command)


    def make_lbl(self,name,window,x,y,h,w,fontsize,color='800080'):
        lbl=QLabel(name,window)
        lbl.setGeometry(x,y,h,w)
        lbl.setStyleSheet('color:{}'.format(color))
        lbl.setFont(QFont('Andalus',fontsize))







    def make_combobox(self,window,x,y,h,w,type='classes'):
        combo=QComboBox(window)
        combo.setGeometry(x,y,h,w)
        combo.setFont(QFont('Andalus',15))
        if type=='classes':
            combo.addItem('الاول المتوسط')
            combo.addItem('الثاني المتوسط')
            combo.addItem('الثالث المتوسط')
            combo.addItem('الرابع العلمي')
            combo.addItem('الرابع الادبي')
            combo.addItem('الخامس العلمي')
            combo.addItem('الخامس الادبي')
            combo.addItem('السادس العلمي')
            combo.addItem('السادس الادبي')
        else:
            combo.addItem('رجاء ادخل الاصناف')


    def make_label_image(self,window,x,y,h,w,path_window='E:\مدارس pyqt5\image\\add_student.jpg'):
        lbl=QLabel(window)
        lbl.setGeometry(x,y,h,w)
        pixmap=QPixmap(path_window)
        lbl.setPixmap(pixmap)


    def make_messagebox(self,window,title,text,btn_message=QMessageBox.Yes,background='white'):
        msg = QMessageBox(window)
        msg.setWindowTitle('{}'.format(title))
        msg.setText('{}'.format(text))
        msg.setStandardButtons(btn_message)
        msg.setStyleSheet('background-color:{}'.format(background))
        #msg.setStyleSheet('color:{}'.format(font_color))
        msg.exec_()


    def make_horizontal_line(self):
        horz_line=QLine()
        #horz_line.

class make_EDITLINE():
    def __init__(self,window,x,y,h,w,fontsize,Enabled=True,settext='null'):
        self.line = QLineEdit(window)
        self.line.setGeometry(x, y, h, w)
        self.line.setFont(QFont('Andalus', fontsize))
        self.line.setStyleSheet('background-color: rgb(33, 33, 33);'
                                               'border-color: rgb(192, 0, 0);'
                                               'color: rgb(192, 0, 0);'
                                               'font: bold italic 20pt "Times New Roman";'
                                               )
        self.line.setEnabled(Enabled)
        self.line.setText(settext)
    def get_txt_editline(self):
        txtline=self.line.text()
        return txtline


class make_COMBOBOX():
    def __init__(self,window,x,y,h,w,type='classes'):
        self.combo = QComboBox(window)
        self.combo.setGeometry(x, y, h, w)
        self.combo.setFont(QFont('Andalus', 15))
        if type == 'classes':
            self.combo.addItem('الاول المتوسط')
            self.combo.addItem('الثاني المتوسط')
            self.combo.addItem('الثالث المتوسط')
            self.combo.addItem('الرابع العلمي')
            self.combo.addItem('الرابع الادبي')
            self.combo.addItem('الخامس العلمي')
            self.combo.addItem('الخامس الادبي')
            self.combo.addItem('السادس العلمي')
            self.combo.addItem('السادس الادبي')
        else:
            self.combo.addItem('رجاء ادخل الاصناف')



    def get_txtcombo(self):
        txtcombo=self.combo.currentText()
        return txtcombo



class make_tableWidget():
    def __init__(self,window,x,y,h,w):
        super().__init__()
        self.table=QTableWidget(window)
        self.table.setGeometry(x,y,h,w)
        self.table.setVerticalHeaderLabels(str("name:id:class:phone:born").split(':'))
        self.table.setFont(QFont('Andalus', 15))


       # self.table.setStyleSheet('background-color:white;'
        #                                       'border-color: rgb(102, 252, 24);'
        #                                      'color: white;')
        #self.table.verticalHeader().setStyleSheet('background-color:white')
        #self.table.horizontalHeader().setStyleSheet('background-color:rgb(102, 255, 153)')

        self.table.horizontalHeader().setDefaultSectionSize(172)
        self.table.verticalHeader().setDefaultSectionSize(50)

    def add_atems(self,data,row_number=0,column_number=5):
        self.table.setColumnCount(column_number)
        alldata=data
        for row_number,row_data in enumerate(alldata):
            self.table.insertRow(row_number)
            for coloumn_num,datat in enumerate(row_data):
                self.table.setItem(row_number,coloumn_num,QTableWidgetItem(str(datat)))





    def get_current_row(self):
        try:
            itemTableText = self.table.item(self.table.currentRow(), 0).text()
            #print(itemTableText)
            return itemTableText
        except Exception as ex:
            return


    def destroy_table(self):
        self.table.clear()


class make_textedit():
    def __init__(self,window,x,y,h,w,fontsize=15,settext='null'):
        super().__init__()

        self.txtedit=QTextEdit(window)
        self.txtedit.setGeometry(x,y,h,w)
        self.txtedit.setStyleSheet('background-color:balck;''color:rgb(0, 153, 255)')
        self.txtedit.setFont(QFont('Andalus', fontsize))
        self.txtedit.setText(settext)


    def get_text_txtedit(self):
        val=self.txtedit.toPlainText()
        return val









