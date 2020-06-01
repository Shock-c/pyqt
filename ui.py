# -*- codingg: utf-8 -*-

# Form implementation generated from reading ui file 'qzone.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import _thread
import ctypes
import datetime
import fileinput
import random
import sys
import time
from os import path
from queue import Queue

import cv2
import requests
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import PyQt5.sip

import QZoneUtil

import ctypes

try:
    temp=ctypes.windll.LoadLibrary('opencv_videoio_ffmpeg420_64.dll')

except:
    pass


class Ui_MainWindow(object):

    success_num = 0
    error_num = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 600)
        MainWindow.setWhatsThis("")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 931, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 231))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 231))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(960, 330, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.picButton = QtWidgets.QPushButton(self.centralwidget)
        self.picButton.setGeometry(QtCore.QRect(960, 40, 100, 40))
        self.picButton.setObjectName("picButton")
        self.picEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.picEdit.setGeometry(QtCore.QRect(960, 20, 50, 20))
        self.picEdit.setValidator(QIntValidator())  # 空的整数校验
        self.picEdit.setMaxLength(10)  # 最多输入4位，即不超过9999
        self.picEdit.setAlignment(Qt.AlignRight)
        self.picEdit.setPlaceholderText('40000')
        self.picEdit.setObjectName("picEdit")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(1020, 20, 50, 20))
        self.radioButton.setObjectName("radioButton")
        self.ckButton = QtWidgets.QPushButton(self.centralwidget)
        self.ckButton.setGeometry(QtCore.QRect(960, 130, 100, 40))
        self.ckButton.setObjectName("ckButton")
        self.ipEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.ipEdit.setGeometry(QtCore.QRect(719, 251, 211, 40))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(8)
        self.ipEdit.setFont(font)
        self.ipEdit.setWhatsThis("")
        self.ipEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.ipEdit.setPlaceholderText("")
        self.ipEdit.setObjectName("ipEdit")
        self.ipButton = QtWidgets.QPushButton(self.centralwidget)
        self.ipButton.setGeometry(QtCore.QRect(960, 251, 100, 40))
        self.ipButton.setObjectName("ipButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 230, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.logBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.logBrowser.setGeometry(QtCore.QRect(0, 251, 721, 311))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        self.logBrowser.setFont(font)
        self.logBrowser.setObjectName("logBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(870, 440, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.successLable = QtWidgets.QLabel(self.centralwidget)
        self.successLable.setGeometry(QtCore.QRect(970, 440, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.successLable.setFont(font)
        self.successLable.setAlignment(QtCore.Qt.AlignCenter)
        self.successLable.setObjectName("successLable")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(870, 500, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.failLabel = QtWidgets.QLabel(self.centralwidget)
        self.failLabel.setGeometry(QtCore.QRect(970, 500, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.failLabel.setFont(font)
        self.failLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.failLabel.setObjectName("failLabel")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(720, 330, 211, 40))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1082, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ckButton.clicked.connect(self.openfile)
        self.picButton.clicked.connect(self.openImg)
        self.ipButton.clicked.connect(self.set_proxy)
        self.startButton.clicked.connect(self.start)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        # item = self.tableWidget.item(0, 0)
        # item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "uin"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "pwd"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "cookie"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "空间权限"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "上传结果"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "好友数量"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "备注"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.startButton.setText(_translate("MainWindow", "开始上传"))
        self.picButton.setText(_translate("MainWindow", "选择图片"))
        self.ckButton.setText(_translate("MainWindow", "导入CK"))
        self.ipEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'仿宋\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:15pt;\">输入代理</span></p></body></html>"))
        self.ipButton.setText(_translate("MainWindow", "设置代理"))
        self.label.setText(_translate("MainWindow", "运行日志"))
        self.logBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:14pt;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "成功"))
        self.successLable.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "失败"))
        self.failLabel.setText(_translate("MainWindow", "0"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'仿宋\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">输入文本</p></body></html>"))
        self.radioButton.setText(_translate("MainWindow", "灰色"))
    def openfile(self):
        openFile, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选择ck文件", "./","All Files (*);;Text Files (*.txt)")
        # 当窗口非继承QtWidgets.QDialog时，self可替换成 None
        if openFile == '':
            self.log('未选择CK文件')
            return
        self.log('选中'+str(openFile))
        self.get_cookie(openFile)

    def openImg(self):
        openFile, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选择img文件", "./","All Files (*);;Text Files (*.txt)")
        # 当窗口非继承QtWidgets.QDialog时，self可替换成 None
        print(type(openFile))
        if openFile == '':
            self.log('未选择图片')
            return
        self.log('选中'+str(openFile))
        if self.radioButton.isChecked():
            img = cv2.imread(openFile, cv2.IMREAD_GRAYSCALE)
        else:
            img = cv2.imread(openFile)

        sp = img.shape
        self.log('处理图片中，请等待...')
        rand = self.picEdit.text()
        if rand is None or rand =='':
            rand = 40500
        for i in range(int(rand)):  # 生成1000个噪点
            a = random.randint(0, int(sp[0])-1)
            b = random.randint(0, int(sp[1])-1)
            img[a, b] = 0

        cv2.imwrite('vc1.png', img)
        self.log('图片处理完成')

    def start(self):

        try:
            proxy = self.proxy
        except:
            self.log("未获取到代理")
            return

        if proxy.find('{') >= 0:
            self.log(proxy)
            return
        elif not path.exists('vc1.png'):
            self.log('未选择图片')
            return
        
        proxy_ip = proxy.split('\n')
        proxy_len = len(proxy_ip)
        for i in range(0, proxy_len):
            _thread.start_new_thread(self.get_list, (proxy_ip[i],))

    def get_list(self, proxy_ip):
        global queue
        i = 0
        while True:
            arg = queue.get()
            if arg != None:
                self.q_zone(int(arg[0]), arg[1], arg[2], arg[3])
                i += 1

    def em(self):
        forward_text = self.textEdit.toPlainText()
        text_list = list(forward_text)
        forward_text = ''
        for i in text_list:
            em = '[em]e' + str(random.randint(100, 204)) + '[/em]'
            forward_text += em + i

        return forward_text

    def q_zone(self, qq, cookie, row, proxy_ip):
        forward_text = self.em()
        proxy_ip = proxy_ip.strip('\r')
        proxy_ip = proxy_ip.strip('\n')
        print("proxy_ip", proxy_ip)
        qzone = QZoneUtil.QZoneUtil(qq, forward_text, row, proxy=proxy_ip)

        flag = qzone.login_with_cookie(cookie)
        if flag != None:
            self.log(str(qq) + ' -- ' + flag)
            self.table_result(row, flag=flag)
            return
        flag = qzone.open_auth()
        if flag != None:
            self.log(str(qq) + ' -- ' + flag)
            self.table_result(row, auth='未修改')
        else:
            self.table_result(row, auth='所有人')
        num, flag = qzone.friend_num()
        if flag != None:
            self.log(str(qq) + ' -- ' + flag)
            self.table_result(row, friend_num='未获取')
        else:
            self.table_result(row, friend_num=str(num))

        flag = qzone.creat_img()
        if flag != None:
            self.log(str(qq) + ' -- ' + flag)
            self.table_result(row, flag=flag)
            self.log(str(qq) + ' -- ' + "相册创建失败")
            return
        flag = qzone.upload_img()
        if flag != None:
            self.log(str(qq) + ' -- ' + flag)
            self.table_result(row, flag=flag)
            self.log(str(qq) + ' -- ' + "上传图片失败")
            return
        self.tableWidget.setItem(row, 4, QTableWidgetItem('成功'))
        self.log(str(qq) + ' -- ' + "上传成功")
        self.success_num += 1
        self.successLable.setText(str(self.success_num))


    def set_proxy(self):
        proxy_url = self.ipEdit.toPlainText()
        proxy_url = proxy_url.strip('\n')
        self.log(proxy_url)
        try:
            proxy = requests.get(proxy_url)
            self.log(proxy.text)
        except:
            self.log('输入的代理有误')
            return False
        else:
            self.proxy = proxy.text
            proxy_ip = self.proxy.split('\n')
            self.proxy_len = len(proxy_ip)
            return True

    def get_cookie(self, filePath):
        for line in fileinput.input(filePath):
            line = line.strip('\n')
            line = line.strip('\r')
            sp1 = str(line).split('----')
            if sp1.__len__() < 3 :
                print("ck格式错误")
                self.log("ck格式错误 " + line)
                continue
            qq = sp1[0]
            pwd = sp1[1]
            cookies = sp1[2].strip(' ')
            # cookie_array = cookies.split(';')
            # cookie = {}
            # for cookie_element in cookie_array:
            #     cookie_element = cookie_element.strip(' ')
            #     ck = cookie_element.split('=')
            #     if len(ck) == 2:
            #         cookie[ck[0]] = ck[1]
            #     else:
            #         pass
            # print("cookie",cookie)
            # print("line", line)
            data = [qq, pwd, cookies]
            # data = [cookie, qq, line]

            self.tableCK(data)
            # queue.put(data)

    def tableCK(self, data):

        try:
            proxy = self.proxy
        except:
            self.log("先设置代理")
            return
        if proxy.find('{') >= 0:
            self.log(proxy)
            return

        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        self.tableWidget.setItem(rowCount,0,QTableWidgetItem(data[0]))
        self.tableWidget.setItem(rowCount,1,QTableWidgetItem(data[1]))
        self.tableWidget.setItem(rowCount,2,QTableWidgetItem(data[2]))
        qq = data[0]
        cookies = data[2]
        cookie_array = cookies.split(';')
        cookie = {}
        for cookie_element in cookie_array:
            cookie_element = cookie_element.strip(' ')
            ck = cookie_element.split('=')
            if len(ck) == 2:
                cookie[ck[0]] = ck[1]
            else:
                pass

        proxy_ip = proxy.split('\n')
        if self.proxy_len <= 0:
            print('qq',data[0])
            if not self.set_proxy():
                print(data[0])
                return
            else:
                proxy = self.proxy
                proxy_ip = proxy.split('\n')
        self.proxy_len = self.proxy_len-1
        print(proxy_ip[self.proxy_len], self.proxy_len, data[0])
        data = [qq, cookie, rowCount, proxy_ip[self.proxy_len]]
        queue.put(data)


    def log(self, log_str):
        time_str = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
        self.logBrowser.append(time_str + ' ---- ' + log_str)
        self.cursor = self.logBrowser.textCursor()
        self.logBrowser.moveCursor(self.cursor.End)

    def table_result(self, row, flag='', auth='', friend_num=''):
        print('auth', auth)
        if auth != '':
            self.tableWidget.setItem(row, 3, QTableWidgetItem(auth))
        if friend_num != '':
            self.tableWidget.setItem(row, 5, QTableWidgetItem(friend_num))
        if flag != '':
            self.tableWidget.setItem(row, 4, QTableWidgetItem('失败'))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(flag))
            self.error_num += 1
            self.failLabel.setText(str(self.error_num))





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widgets)
    widgets.show()
    queue = Queue()
    sys.exit(app.exec_())
