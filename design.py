# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import detectimg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import detectimg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 934)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -10, 1201, 971))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("图片/背景3.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(640, 540, 81, 81))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("图片/按钮3.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setEnabled(False)
        self.textBrowser_3.setGeometry(QtCore.QRect(610, 620, 141, 41))
        self.textBrowser_3.setMouseTracking(False)
        self.textBrowser_3.setAutoFillBackground(True)
        self.textBrowser_3.setStyleSheet("QTextEdit { background-color: rgb(255,132,139,0);border-radius:3px; color:rgb(0,0,0);}")
        self.textBrowser_3.setTabChangesFocus(True)
        self.textBrowser_3.setUndoRedoEnabled(True)
        self.textBrowser_3.setPlaceholderText("")
        self.textBrowser_3.setOpenExternalLinks(True)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setEnabled(False)
        self.textBrowser_2.setGeometry(QtCore.QRect(260, 720, 621, 160))
        self.textBrowser_2.setMouseTracking(False)
        self.textBrowser_2.setAutoFillBackground(True)
        self.textBrowser_2.setStyleSheet("QTextEdit { background-color: rgb(255,132,139,0);border-radius:3px; color:rgb(0,0,0);}")
        self.textBrowser_2.setTabChangesFocus(True)
        self.textBrowser_2.setUndoRedoEnabled(True)
        self.textBrowser_2.setPlaceholderText("")
        self.textBrowser_2.setOpenExternalLinks(True)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setEnabled(False)
        self.textBrowser_5.setGeometry(QtCore.QRect(610, 380, 141, 41))
        self.textBrowser_5.setMouseTracking(False)
        self.textBrowser_5.setAutoFillBackground(True)
        self.textBrowser_5.setStyleSheet("QTextEdit { background-color: rgb(255,132,139,0);border-radius:3px; color:rgb(0,0,0);}")
        self.textBrowser_5.setTabChangesFocus(True)
        self.textBrowser_5.setUndoRedoEnabled(True)
        self.textBrowser_5.setPlaceholderText("")
        self.textBrowser_5.setOpenExternalLinks(True)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, -20, 921, 241))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("图片/title5.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1000, 690, 201, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("图片/AI1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 570, 21, 20))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setEnabled(False)
        self.textBrowser_4.setGeometry(QtCore.QRect(230, 180, 731, 71))
        self.textBrowser_4.setMouseTracking(False)
        self.textBrowser_4.setAutoFillBackground(True)
        self.textBrowser_4.setStyleSheet("QTextEdit { background-color: rgb(255,132,139,0);border-radius:3px; color:rgb(0,0,0);}")
        self.textBrowser_4.setTabChangesFocus(True)
        self.textBrowser_4.setUndoRedoEnabled(True)
        self.textBrowser_4.setPlaceholderText("")
        self.textBrowser_4.setOpenExternalLinks(True)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(640, 300, 81, 81))
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("图片/按钮3.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 330, 21, 20))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setEnabled(False)
        self.textBrowser_7.setGeometry(QtCore.QRect(120, 480, 141, 41))
        self.textBrowser_7.setMouseTracking(False)
        self.textBrowser_7.setAutoFillBackground(True)
        self.textBrowser_7.setStyleSheet("QTextEdit { background-color: rgb(255,132,139,0);border-radius:3px; color:rgb(0,0,0);}")
        self.textBrowser_7.setTabChangesFocus(True)
        self.textBrowser_7.setUndoRedoEnabled(True)
        self.textBrowser_7.setPlaceholderText("")
        self.textBrowser_7.setOpenExternalLinks(True)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 380, 81, 81))
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("图片/按钮3.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 260, 391, 431))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(750, 260, 391, 431))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_7.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 410, 21, 20))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_2.raise_()
        self.textBrowser_5.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.textBrowser_4.raise_()
        self.label_4.raise_()
        self.pushButton_2.raise_()
        self.textBrowser_7.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1209, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton_3.clicked.connect(self.openfile)
        self.pushButton_2.clicked.connect(self.detect)
        self.pushButton.clicked.connect(self.show)

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self.centralwidget, 'open file', '/')
        jpg = QtGui.QPixmap(openfile_name[0])
        self.label_7.setPixmap(jpg)
        self.path = openfile_name[0]

    def show(self):
        jpg = QtGui.QPixmap('D:\PyCharmProject\objDetect\keras-yolo3\\ui_result\\'+"result.jpg")
        self.label_8.setPixmap(jpg)



    def detect(self):
        r_image, out=d.detect(self.path)
        print(out)
        text = ""
        for key in out.keys():
            q=out[key]
            s = '类别:'+str(q[0])+" "'分数:'+str(q[1])+"位置：("+str(q[2][0])+","+str(q[2][1])+","+str(q[3][0])+","+str(q[3][1])+")\n"
            text =text+s
        self.textBrowser_2.setText(text)
        self.textBrowser_2.setStyleSheet("font-size:24px")
        self.textBrowser_2.setEnabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">查看结果</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#ffaa00;\">第三组 杨引弟 张力天 李宣仪 邢威</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">开始检测</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#ffaa00;\">第三组 杨引弟 张力天 李宣仪 邢威</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">上传图片</span></p></body></html>"))


if  __name__=="__main__":
    d = detectimg.detect()
    import  sys
    app=QtWidgets.QApplication(sys.argv)
    widget= QtWidgets.QMainWindow()
    ui= Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
