#ZRNLBSWMSPRTBLD
#CREW2K22AL

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 404)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 10, 241, 121))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(179, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Calibri\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 10, 241, 121))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(179, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Calibri\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 140, 241, 121))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(179, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Calibri\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 140, 241, 121))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 147, 176);\n"
"background-color: rgb(31, 141, 0);\n"
"font: 75 14pt \"Calibri\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 270, 491, 51))
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 147, 176);\n"
"background-color: rgb(31, 141, 0);\n"
"font: 75 14pt \"Calibri\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 330, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 147, 176);\n"
"background-color: rgb(31, 141, 0);\n"
"font: 75 14pt \"Calibri\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 280, 131, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("zrn_logo_no_back.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 371, 381))
        self.label_4.setToolTipDuration(1)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 36pt \"Calibri\";")
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setPixmap(QtGui.QPixmap("WMS_LOGO.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_4.clicked.connect(self.launch_send_grp)
        self.pushButton_6.clicked.connect(self.load_scan_qr)
        self.pushButton_5.clicked.connect(self.load_logout)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#IN AN UPDATE, COPY CODE FROM HERE

    def launch_send_grp(self):
        print("signal received")
        os.system("python mlt_snd_grp.py&")
    def load_scan_qr(self):
        print("signal received")
        os.system("npx mudslide@latest login&")
    def load_logout(self):
        print("signal received")
        os.system("npx mudslide@latest logout&")
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ICTFROMABC WMS Version 3.1 [Bugfixed]"))
        self.pushButton.setText(_translate("MainWindow", "Send a Message to a number"))
        self.pushButton_2.setText(_translate("MainWindow", "Send a Message to\n"
" multiple Numbers"))
        self.pushButton_3.setText(_translate("MainWindow", "Send a Message to a Group"))
        self.pushButton_4.setText(_translate("MainWindow", "Send a Message to\n"
" Multiple Groups"))
        self.pushButton_5.setText(_translate("MainWindow", "Log Out"))
        self.pushButton_6.setText(_translate("MainWindow", "Scan QR and LogIn"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
