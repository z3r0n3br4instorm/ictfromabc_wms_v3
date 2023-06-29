#ZERONE TECHNOLOGIES AND LABORATORIES
#CREW2K22AL
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os
from PyQt5.QtCore import QDir
global filename, teacup, watercup, watercup_data, beercup, filename2
global grp_array 
grp_array = []
teacup = 0 #Switch for image send
watercup = 0 #Switch to skip groups
beercup = 0     #Audio Select Switch
watercup_data = 1 #Variable which determine the starting value of the sending array
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 620)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -140, 381, 371))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo_new.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 560, 241, 31))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Ubuntu Light\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 570, 231, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(740, 480, 101, 211))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("home android.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 110, 681, 61))
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(120, 120, 120);\n"
"font: 75 12pt \"Ubuntu Mono\";")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 190, 541, 61))
        self.textEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(120, 120, 120);\n"
"font: 75 12pt \"Ubuntu Mono\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 110, 131, 61))
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Ubuntu Light\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 300, 861, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-10, 530, 861, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 330, 751, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(560, 190, 131, 61))
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Ubuntu Light\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(700, 190, 131, 61))
        self.pushButton_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Ubuntu Light\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 791, 18))
        self.label_4.setStyleSheet("color: rgb(153, 153, 153);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 280, 791, 18))
        self.label_5.setStyleSheet("color: rgb(153, 153, 153);")
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(750, 260, 61, 41))
        self.textEdit_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(120, 120, 120);\n"
"font: 75 12pt \"Ubuntu Mono\";")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QPushButton(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(667, 260, 71, 31))
        self.label_6.setObjectName("label_6")
        self.label_3.raise_()
        self.label.raise_()
        self.pushButton_4.raise_()
        self.label_2.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        self.pushButton_5.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.textBrowser.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.textEdit_3.raise_()
        self.label_6.raise_()
        self.pushButton_5.clicked.connect(self.search_group)
        self.pushButton_6.clicked.connect(self.aud_vid_select_slot)
        self.pushButton_4.clicked.connect(self.search_group_send)
        self.pushButton_7.clicked.connect(self.aud_vid_select_slot_2)
        self.label_6.clicked.connect(self.watercup)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.textBrowser.setStyleSheet('background-color: white')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #Function that manages Images
    def aud_vid_select_slot(self):
        global filename, beercup, teacup
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.bmp)", options=options)
        filename = QDir.toNativeSeparators(filename)
        if filename:
                print(filename)
                self.label_4.setText(filename)
        teacup = 1
        #DEV
    def aud_vid_select_slot_2(self):#Slot that manages audios
        global filename2, teacup, beercup
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename2, _ = QFileDialog.getOpenFileName(None, "Select File", "", "Files (*.mp3 *.ogg *.pdf)", options=options)
        if filename2:
                print(filename2)
                self.label_5.setText(filename2)
        beercup = 1
        #DEV
    def aud_vid_select_slot_3(self):#Slot that manages videos
        global filename, teacup
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(None, "Select Video", "", "Video Files (*.mp4)", options=options)
        if filename:
                print(filename)
                self.label_4.setText(filename)
        teacup = 1
        #DEV
    #Function that manages the groupSkip switch and its thing
    def watercup(self):
        print("Watercup Active")
        global watercup, watercup_data
        watercup = 1
        watercup_data = message = self.textEdit_3.toPlainText()
    #Searching Groups
    def search_group(self):
        global grp_array
        grp_array = []
        text_data = self.textEdit.toPlainText()
        self.textBrowser.setText("Searching For Groups... Please wait !")
        QApplication.instance().processEvents()
        os.system("npx mudslide@latest groups > groups.txt")
        line_count = 0
        with open("groups.txt", mode='r', encoding='utf-8') as file:
                for line in file:
                        print("")
        self.textBrowser.setText("Selecting groups, please wait...")
        os.system("npx mudslide@latest groups > groups.txt")
        with open("groups.txt", mode='r', encoding='utf-8') as file:
            data = file.readlines()[:-1]
            results = ""
            line_2 = 0
            if(True):
                for line in data:
                    # Remove the newline character from each line
                    line = line.strip()
                    json_data = json.loads(line)
                    if text_data in json_data["subject"]:
                        results += json_data["subject"] + "\n"
                        line_2 = line_2+1
                        data_rec = results+"["+str(line_2)+"]"
                        self.textBrowser.append(data_rec)
                        QApplication.instance().processEvents()
                        print(line_count)
                        grp_array.append(line_count)
                        print(grp_array)
                    line_count+=1
            else:
                self.textBrowser.setText(results)
        #DEV
    #Sending the message
    def search_group_send(self):
        print("Signal Received")
        global filename, teacup, watercup, watercup_data, grp_array, filename2, beercup
        print("teacup_switch = ", teacup)
        print("watercup_switch = ", watercup)
        print("beercup_switch = ", beercup)
        print("Array Start Value =", str(watercup_data))
        message = self.textEdit_2.toPlainText()
        self.textBrowser.append("Selecting groups, please wait...")
        QApplication.instance().processEvents()
        try:
                print("Failed to create log file, Creating new file...")
                file_name = open("log.txt","x")
        except:
                print("Log file detected")
                file_name = open('log.txt',"w")
        def smn(number,message):
                global teacup, filename
                if True:
                        print("Sending Message to returned number...")
                        if len(message) > 0:
                                message = message.replace("\n","\\n")
                                #print(message)
                                return_os_text = "npx mudslide@latest send "+str(number)+" \""+str(message)+"\""
                        else:
                                return_os_text = "echo"
                        if teacup == 1:
                                return_os_text_2 = "npx mudslide@latest send-image "+str(number)+" \""+str(filename)+"\""
                                os.system(return_os_text_2)
                        if beercup == 1:
                                return_os_text_3 = "npx mudslide@latest send-file "+str(number)+" \""+str(filename2)+"\""
                                os.system(return_os_text_3)
                        print(return_os_text)
                        os.system(return_os_text)
        text_data = self.textEdit.toPlainText()
        line_count = 0
        os.system("npx mudslide@latest groups > groups.txt")
        with open("groups.txt", mode='r', encoding='utf-8') as file:
                for line in file:
                        line_count += 1
        count = 0
        with open("groups.txt", mode='r', encoding='utf-8') as file:
            data = file.readlines()[:-1]
            results = ""
            line_count_2 = 0#im lazy to implement the more efficient way now so imma do it this way
            if(True):
                for line in data:
                    # Remove the newline character from each line
                    if True:
                        line = line.strip()
                        json_data = json.loads(line)
                        if int(line_count_2) >= grp_array[int(watercup_data)-1]:
                                if text_data in json_data["subject"]:
                                        count +=1
                                        results += json_data["subject"] + "\n"
                                        smn(json_data["id"],message)
                                        datasend = "Sending Message "+"["+str(count)+"]"
                                        print(datasend)
                                        file_name.write(datasend+" "+json_data["subject"]+"\n")
                                        self.textBrowser.append(datasend)

                                        QApplication.instance().processEvents()
                        else:
                                print("watercupSkip")
                        line_count_2 += 1
                #teacup = 0
            else:
                self.label_4.setText(results)
        #DEV

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZERONE TECHNOLOGIES - WMS MULTIPLE GROUP SELECTION INTERFACE Version 3.2"))
        self.pushButton_4.setText(_translate("MainWindow", "SEND"))
        self.label_2.setText(_translate("MainWindow", "ictfromabc-CREW#2022AL"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "ENTER GROUP NAME"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "ENTER THE MESSAGE"))
        self.pushButton_5.setText(_translate("MainWindow", "Search Group"))
        self.textBrowser.setPlaceholderText(_translate("MainWindow", "Waiting For Data..."))
        self.pushButton_6.setText(_translate("MainWindow", "Select Image"))
        self.pushButton_7.setText(_translate("MainWindow", "Select File"))
        self.label_4.setText(_translate("MainWindow", "File Select"))
        self.label_5.setText(_translate("MainWindow", "File Select"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "GroupSkip"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
