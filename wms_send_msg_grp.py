#ZTWMSICTFRMABC
#CREW2K22AL
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 448)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -140, 381, 371))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/zrn/Desktop/WMS-PROT-NEW/logo_new.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 380, 241, 31))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Ubuntu Light\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 390, 231, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(740, 300, 101, 211))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("/home/zrn/Desktop/WMS-PROT-NEW/home android.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 801, 151))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 22pt \"Ubuntu Mono\";")
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(330, 30, 361, 61))
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Ubuntu Mono\";")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 110, 361, 61))
        self.textEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Ubuntu Mono\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 30, 131, 61))
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Ubuntu Light\";")
        self.pushButton_4.clicked.connect(self.search_group_send)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.search_group)
        self.label_3.raise_()
        self.label.raise_()
        self.pushButton_4.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        self.pushButton_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def search_group(self):
        text_data = self.textEdit.toPlainText()
        os.system("npx mudslide groups > /home/zrn/Desktop/WMS-PROT-NEW/groups.txt")
        line_count = 0
        with open("/home/zrn/Desktop/WMS-PROT-NEW/groups.txt", "r") as file:
                for line in file:
                        print("")
        self.label_4.setText("Selecting groups, please wait...")
        os.system("npx mudslide groups > /home/zrn/Desktop/WMS-PROT-NEW/groups.txt")
        with open("/home/zrn/Desktop/WMS-PROT-NEW/groups.txt") as file:
            data = file.readlines()[:-1]
            results = ""
            if(True):
                for line in data:
                    # Remove the newline character from each line
                    line = line.strip()
                    json_data = json.loads(line)
                    if text_data in json_data["subject"]:
                        results += json_data["subject"] + "\n"
                        line_count+=1
                        data_rec = results+"["+str(line_count)+"]"
                        self.label_4.append(data_rec)
                        QApplication.instance().processEvents()
            else:
                self.label_4.setText(results)
        #DEV
    def search_group_send(self):
        message = self.textEdit_2.toPlainText()
        self.label_4.append("Selecting groups, please wait...")
        def smn(number,message):
                if True:
                        print("Sending Message to returned number...")
                        return_os_text = "npx mudslide send "+str(number)+" \""+str(message)+"\""
                        print(return_os_text)
                        os.system(return_os_text)
        text_data = self.textEdit.toPlainText()
        line_count = 0
        os.system("npx mudslide groups > /home/zrn/Desktop/WMS-PROT-NEW/groups.txt")
        with open("groups.txt", mode='r', encoding='utf-8') as file:
                for line in file:
                        line_count += 1
        count = 0
        with open("groups.txt") as file:
            data = file.readlines()[:-1]
            results = ""
            if(True):
                for line in data:
                    # Remove the newline character from each line
                    line = line.strip()
                    json_data = json.loads(line)
                    if text_data in json_data["subject"]:
                        count +=1
                        results += json_data["subject"] + "\n"
                        smn(json_data["id"],message)
                        datasend = "Sending Message "+"["+str(count)+"]"#
                        print(datasend)
                        self.label_4.append(datasend)
                        QApplication.instance().processEvents()
            else:
                self.label_4.setText(results)
        #DEV
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "SEND"))
        self.label_2.setText(_translate("MainWindow", "ictfromabc-CREW#2022AL"))
        self.label_4.setText(_translate("MainWindow", "wms-grp-disp"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "ENTER GROUP NAME"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "ENTER THE MESSAGE"))
        self.pushButton_5.setText(_translate("MainWindow", "Search Group"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
