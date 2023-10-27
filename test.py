from PyQt6 import QtCore , uic , QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtWidgets import QTextEdit , QPushButton , QListWidget , QMessageBox , QLineEdit , QInputDialog

import sys

class UI2(QMainWindow) :
    def __init__(self) :
        super(UI2 , self).__init__()
        uic.load_ui.loadUi("./w6506021420068.ui" , self)
        
        #Find Widget
        self.textedit = self.findChild(QTextEdit , "textEdit")
        self.btn_1 = self.findChild(QPushButton , "btn_1")
        self.btn_2 = self.findChild(QPushButton , "btn_2")
        
        #Connect to take action
        self.btn_1.clicked.connect(self.clickBtn_1)
        self.btn_2.clicked.connect(self.clickBtn_2)
        
        #Show ui
        self.show()
    
    def clickBtn_1(self) :
        self.myList = List_UI()

    def clickBtn_2(self) :
        self.student = Student_UI()

class List_UI(QMainWindow) :
    def __init__(self) :
        super(List_UI , self).__init__()
        uic.load_ui.loadUi("./w6506021420068.ui" , self)
        
        #Find Widget
        self.list = self.findChild(QListWidget , "listWidget")
        self.addBtn = self.findChild(QPushButton , "addBtn")
        self.delBtn = self.findChild(QPushButton , "delBtn")
        self.showBtn = self.findChild(QPushButton , "showBtn")

        #Connect to take action
        self.list.clicked.connect(self.listview_click)
        self.addBtn.clicked.connect(self.act_add)
        self.delBtn.clicked.connect(self.act_del)
        self.showBtn.clicked.connect(self.showmessage)
        #self.list.doubleClicked.connect(self.act_del)

        #Show ui
        self.show()
        
    def listview_click(self) :
        item = self.list.currentRow()
        text = self.list.currentItem().text()
        print(item , text)
        #self.showmessage()
        
    def act_add(self) :
        #self.t1.setPlainText("Hello")
        self.list.insertItem(0 , "Red")
    
    def act_del(self) :
        item = self.list.currentRow()
        self.list.takeItem(item)
        
    def showmessage(self) :
        m = QMessageBox(self , text = "Hello Red")
        m.setIcon(QMessageBox.Icon.Information)
        m.show()

class Student_UI(QMainWindow):
    def __init__(self):
        super(Student_UI, self).__init__()
        uic.load_ui.loadUi("./ui/w6506021420068.ui", self)

        # Find Widget
        self.listWidget = self.findChild(QListWidget, "listWidget")
        self.addBtn3 = self.findChild(QPushButton, "addBtn3")
        self.updateBtn3 = self.findChild(QPushButton, "updateBtn3")
        self.deleteBtn3 = self.findChild(QPushButton, "deleteBtn3")
        self.studentLine = self.findChild(QLineEdit , "studentLine")
        self.telLine = self.findChild(QLineEdit , "telLine")
        self.emailLine = self.findChild(QLineEdit , "emailLine")

        # Connect to take action
        self.listWidget.clicked.connect(self.listview_click)
        self.addBtn3.clicked.connect(self.act_add2)
        self.updateBtn3.clicked.connect(self.act_update2)
        self.deleteBtn3.clicked.connect(self.act_del2)

        # Show ui
        self.show()

    def listview_click(self):
        item = self.listWidget.currentRow()
        text = self.listWidget.currentItem().text()
        print(item , text)

    def act_add2(self):
        studentName = self.studentLine.text()
        tel = self.telLine.text()
        email = self.emailLine.text()

        # Insert each text into the list widget as separate items
        self.listWidget.addItem("Student Name : " + studentName)
        self.listWidget.addItem("Telephone : " + tel)
        self.listWidget.addItem("Email : " + email)
        
    def act_update2(self):
        current_item = self.listWidget.currentItem()
        if current_item:
            new_text, ok = QInputDialog.getText(self, "Update Item", "Enter new text:")
            if ok:
                current_item.setText(new_text)


    def act_del2(self):
        item = self.listWidget.currentRow()
        self.listWidget.takeItem(item)
        
app = QtCore.QCoreApplication.instance()
if app is None : app = QtWidgets.QApplication([])
window = UI2()
app.exec()