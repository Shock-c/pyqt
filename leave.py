# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'leave.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import _thread
import fileinput
import sys
import time
from queue import Queue

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import QZoneUtil


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 721, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.leave_table = QtWidgets.QTableWidget(self.centralwidget)
        self.leave_table.setGeometry(QtCore.QRect(720, 0, 391, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leave_table.setFont(font)
        self.leave_table.setRowCount(1)
        self.leave_table.setColumnCount(3)
        self.leave_table.setObjectName("leave_table")
        item = QtWidgets.QTableWidgetItem()
        self.leave_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.leave_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.leave_table.setItem(0, 2, item)
        self.leave_table.horizontalHeader().setDefaultSectionSize(120)
        self.logBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.logBrowser.setGeometry(QtCore.QRect(0, 250, 721, 301))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.logBrowser.setFont(font)
        self.logBrowser.setObjectName("logBrowser")
        self.proxy_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.proxy_textEdit.setGeometry(QtCore.QRect(720, 250, 291, 41))
        self.proxy_textEdit.setObjectName("proxy_textEdit")
        self.proxy_Button = QtWidgets.QPushButton(self.centralwidget)
        self.proxy_Button.setGeometry(QtCore.QRect(1010, 250, 101, 41))
        self.proxy_Button.setObjectName("proxy_Button")
        self.leave_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.leave_textEdit.setGeometry(QtCore.QRect(720, 290, 291, 41))
        self.leave_textEdit.setObjectName("leave_textEdit")
        self.leave_Button = QtWidgets.QPushButton(self.centralwidget)
        self.leave_Button.setGeometry(QtCore.QRect(1010, 290, 101, 41))
        self.leave_Button.setObjectName("leave_Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(733, 501, 71, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.ck_Button = QtWidgets.QPushButton(self.centralwidget)
        self.ck_Button.setGeometry(QtCore.QRect(780, 410, 101, 41))
        self.ck_Button.setObjectName("ck_Button")
        self.start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.start_Button.setGeometry(QtCore.QRect(950, 410, 101, 41))
        self.start_Button.setObjectName("start_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ck_Button.clicked.connect(self.openfile)
        # self.leave_Button.clicked.connect(self)
        self.proxy_Button.clicked.connect(self.set_proxy)
        self.start_Button.clicked.connect(self.start)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "uin"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "cookies"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "结果"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "备注"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.leave_table.isSortingEnabled()
        self.leave_table.setSortingEnabled(False)
        item = self.leave_table.item(0, 0)
        item.setText(_translate("MainWindow", "uin"))
        item = self.leave_table.item(0, 1)
        item.setText(_translate("MainWindow", "qq"))
        item = self.leave_table.item(0, 2)
        item.setText(_translate("MainWindow", "状态"))
        self.leave_table.setSortingEnabled(__sortingEnabled)
        self.logBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:14pt;\"><br /></p></body></html>"))
        self.proxy_Button.setText(_translate("MainWindow", "设置代理"))
        self.leave_Button.setText(_translate("MainWindow", "设置留言"))
        self.ck_Button.setText(_translate("MainWindow", "导入CK"))
        self.start_Button.setText(_translate("MainWindow", "开始"))

    def openfile(self):
        openFile, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选择ck文件", "./",
                                                                   "All Files (*);;Text Files (*.txt)")
        # 当窗口非继承QtWidgets.QDialog时，self可替换成 None
        if openFile == '':
            self.log('未选择CK文件')
            return
        self.log('选中' + str(openFile))
        flag = self.set_proxy()
        self.get_cookie(openFile)

    def start(self):

        try:
            proxy = self.proxy
        except:
            self.log("未获取到代理")
            return

        if proxy.find('{') >= 0:
            self.log(proxy)
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
                self.q_leave(int(arg[0]), arg[1], arg[2], arg[3])
                i += 1
    def q_leave(self, qq, cookie, row, proxy_ip):
        forward_text = self.em()
        proxy_ip = proxy_ip.strip('\r')
        proxy_ip = proxy_ip.strip('\n')
        print("proxy_ip", proxy_ip)
        qzone = QZoneUtil.QZoneUtil(qq, forward_text, row, proxy=proxy_ip)

        flag = qzone.login_with_cookie(cookie)
        if flag != None:
            self.log(str(qq) + ' -- ' + flag)
            self.table_result(row, result='失败', other=flag)
            return
        friend_info, flag = qzone.friend_num()
        if flag != None:
            self.log(str(qq) + ' -- ' + flag)
            self.table_result(row, result='未获取', other=flag)
            return
        else:
            self.table_result(row, result=str(len(friend_info)))
            i = 0
            for f in friend_info:
                uin = f['uin']
                self.log(str(qq) + '-' + str(uin) + '-开始留言')
                for q in range(3):
                    code, msg = qzone.leave(uin)
                    if code == None:
                        self.log(str(qq) + '-' + str(uin) + '-' + msg)
                        self.leave_ta(str(qq), str(uin), msg)
                        return
                    elif code == -4012:
                        self.log(str(qq) + '-' + str(uin) + '-' + msg + '--等待10min')
                        time.sleep(60)
                    else:
                        self.leave_ta(str(qq), str(uin), msg)
                        self.log(str(qq) + '-' + str(uin) + '-' + msg + '--等待20s')
                        i += 1
                        time.sleep(20)
                        break

            self.table_result(row,other=str(i))
            self.log(str(qq) + ' -- ' + '留言发送结束')
            return

    def em(self):
        text = self.leave_textEdit.toPlainText()
        return text


    def leave_ta(self, uin, qq, result):
        rowCount = self.leave_table.rowCount()
        self.leave_table.insertRow(rowCount)
        self.leave_table.setItem(rowCount, 0, QTableWidgetItem(uin))
        self.leave_table.setItem(rowCount, 1, QTableWidgetItem(qq))
        self.leave_table.setItem(rowCount, 2, QTableWidgetItem(result))

    def table_result(self, row, result='', other=''):
        if result != '':
            self.tableWidget.setItem(row, 2, QTableWidgetItem(result))
        if other != '':
            self.tableWidget.setItem(row, 3, QTableWidgetItem(other))


    def get_cookie(self, filePath):
        for line in fileinput.input(filePath):
            line = line.strip('\n')
            line = line.strip('\r')
            sp1 = str(line).split('----')
            if sp1.__len__() < 3:
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
            data = [qq, cookies]
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
        self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(data[0]))
        self.tableWidget.setItem(rowCount, 1, QTableWidgetItem(data[1]))
        qq = data[0]
        cookies = data[1]
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
            print('qq', data[0])
            if not self.set_proxy():
                print(data[0])
                return
            else:
                proxy = self.proxy
                proxy_ip = proxy.split('\n')
        self.proxy_len = self.proxy_len - 1
        print(proxy_ip[self.proxy_len], self.proxy_len, data[0])
        data = [qq, cookie, rowCount, proxy_ip[self.proxy_len]]
        queue.put(data)

    def set_proxy(self):
        proxy_url = self.proxy_textEdit.toPlainText()
        proxy_url = proxy_url.strip('\n')
        self.log(proxy_url)
        try:
            proxy = requests.get(proxy_url)
            if proxy.status_code != 200:
                time.sleep(2)
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


    def log(self, log_str):
        time_str = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
        self.logBrowser.append(time_str + ' ---- ' + log_str)
        self.cursor = self.logBrowser.textCursor()
        self.logBrowser.moveCursor(self.cursor.End)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widgets)
    widgets.show()
    queue = Queue()
    sys.exit(app.exec_())