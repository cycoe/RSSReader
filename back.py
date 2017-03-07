# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cycoe/python/pyqt_project/RSS_Reader/mainWindow1.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_fetchingWarn import Ui_Dialog
import rssCatcher

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        #禁止拉伸窗口大小
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.RSSList = QtWidgets.QListWidget(self.centralWidget)
        self.RSSList.setGeometry(QtCore.QRect(0, 0, 280, 570))        
        self.RSSList.setObjectName("RSSList")
        self.RSSContains = QtWidgets.QListWidget(self.centralWidget)
        self.RSSContains.setGeometry(QtCore.QRect(280, 0, 520, 570))
        self.RSSContains.setObjectName("RSSContains")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menuBar.setObjectName("menuBar")
        self.RSSBT = QtWidgets.QMenu(self.menuBar)
        self.RSSBT.setObjectName("RSSBT")
        self.settingBT = QtWidgets.QMenu(self.menuBar)
        self.settingBT.setObjectName("settingBT")
        MainWindow.setMenuBar(self.menuBar)
        self.refreshBT = QtWidgets.QAction(MainWindow)
        self.refreshBT.setObjectName("refreshBT")
        self.aboutBT = QtWidgets.QAction(MainWindow)
        self.aboutBT.setObjectName("aboutBT")
        self.quitBT = QtWidgets.QAction(MainWindow)
        self.quitBT.setObjectName("quitBT")
        self.manageRssBT = QtWidgets.QAction(MainWindow)
        self.manageRssBT.setObjectName("manageRssBT")
        self.RSSBT.addAction(self.refreshBT)
        self.RSSBT.addAction(self.aboutBT)
        self.RSSBT.addAction(self.quitBT)
        self.settingBT.addAction(self.manageRssBT)
        self.menuBar.addAction(self.RSSBT.menuAction())
        self.menuBar.addAction(self.settingBT.menuAction())

        self.retranslateUi(MainWindow)
        
        self.refreshBT.triggered.connect(self.refreshRSS)
        #self.aboutBT.triggered.connect(self.about)
        self.quitBT.triggered.connect(MainWindow.close)
        #self.manageRssBT.triggered.connect()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def refreshRSS(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        print('fetching rss contain...')
        Dialog.show()
        rssFresher = rssCatcher.RssCatcher('rssSubList')
        rssFresher.getCon()
        rssTitle,  rssSummary = rssFresher.outputer()
        
        titleList = []
        for title in rssTitle:
            titleList.append(QtWidgets.QListWidgetItem(title))
        for i in range(len(titleList)):
            self.RSSList.insertItem(i+1,  titleList[i])
            
        summaryList = []
        for summary in rssSummary:
            summaryList.append(QtWidgets.QListWidgetItem(summary))
        for i in range(len(summaryList)):
            self.RSSContains.insertItem(i+1,  summaryList[i])
            
        Dialog.hide()
            
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Awesome Rss Reader"))
        self.RSSBT.setTitle(_translate("MainWindow", "&RSS"))
        self.settingBT.setTitle(_translate("MainWindow", "设置"))
        self.refreshBT.setText(_translate("MainWindow", "刷新&RSS"))
        self.aboutBT.setText(_translate("MainWindow", "关于"))
        self.quitBT.setText(_translate("MainWindow", "退出"))
        self.manageRssBT.setText(_translate("MainWindow", "管理&RSS源"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.refreshRSS()
    MainWindow.show()
    sys.exit(app.exec_())


