#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cycoe/python/pyqt_project/RSS_Reader/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_RSSManager import RSSManager

class Ui_MainWindow(object):
    def __init__(self):
        self.rssSubFile = 'rssSubList'
        self.rssDataFile = 'rssData.cache'
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(300, 80, 800, 600)
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())    #禁止拉伸窗口大小

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.RSSList = QtWidgets.QListWidget(self.centralWidget)
        self.RSSList.setGeometry(QtCore.QRect(0, 0, 280, 570))
        self.RSSList.setObjectName("RSSList")
        self.RSSContains = QtWidgets.QTextBrowser(self.centralWidget)
        self.RSSContains.setGeometry(QtCore.QRect(280, 40, 520, 530))
        self.RSSContains.setObjectName("RSSContains")
        self.restoreRSS()
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(300, 5, 380, 30))
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.refreshBT_2 = QtWidgets.QPushButton(self.centralWidget)
        self.refreshBT_2.setGeometry(QtCore.QRect(696, 0, 88, 34))
        self.refreshBT_2.setObjectName("refreshBT_2")
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
        self.refreshBT_2.clicked.connect(self.refreshRSS)
        self.quitBT.triggered.connect(MainWindow.close)
        self.manageRssBT.triggered.connect(self.manageRss)
        self.RSSList.itemDoubleClicked.connect(self.pushCon)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pure Rss Reader"))
        self.refreshBT_2.setText(_translate("MainWindow", "Refresh"))
        self.RSSBT.setTitle(_translate("MainWindow", "&RSS"))
        self.settingBT.setTitle(_translate("MainWindow", "设置"))
        self.refreshBT.setText(_translate("MainWindow", "刷新&RSS"))
        self.aboutBT.setText(_translate("MainWindow", "关于"))
        self.quitBT.setText(_translate("MainWindow", "退出"))
        self.manageRssBT.setText(_translate("MainWindow", "管理&RSS源"))

    def manageRss(self):
        self.rssManager = RSSManager(self.rssSubFile)
        self.rssManager.show()

    def refreshRSS(self):
        import os
        from rssFetcher import RssFetcher
        self.progressBar.setProperty("value", 0)
        if os.path.exists(self.rssSubFile):
            rssSubList = open(self.rssSubFile).readlines()
        rssFetcher = RssFetcher()
        self.titleList = []
        self.summaryList = []
        fetchProcess = 0
        for rssSub in rssSubList:
            try:
                rssFetcher.getCon(rssSub)
            except:
                QtWidgets.QMessageBox.warning(MainWindow, "error", "download %s failed" % rssSub, QtWidgets.QMessageBox.Yes)
                continue
            fetchProcess += 1
            self.progressBar.setProperty("value", int(fetchProcess/len(rssSubList)*100))
            rssTitle,  rssSummary = rssFetcher.outputer()
            self.titleList.extend(rssTitle)
            self.summaryList.extend(rssSummary)
        self.dumpRSS()

    def dumpRSS(self):
        with open(self.rssDataFile, 'w') as f:
            for i in range(len(self.titleList)):
                f.write(self.titleList[i] + '\n')
                f.write(self.summaryList[i] + '\n')

        self.RSSList.clear()
        QTitleList = []
        for title in self.titleList:
            QTitleList.append(QtWidgets.QListWidgetItem(title))
        for i in range(len(QTitleList)):
            self.RSSList.insertItem(i+1, QTitleList[i])
        self.RSSContains.setText(self.summaryList[0])


    def restoreRSS(self):
        import os
        if os.path.exists(self.rssDataFile):
            rssData = open(self.rssDataFile).readlines()
        numrssData = len(rssData)
        if numrssData > 0:
            self.titleList = [rssData[i] for i in range(numrssData) if i%2 == 0]
            self.summaryList = [rssData[i] for i in range(numrssData) if i%2 == 1]
            QTitleList = []
            for title in self.titleList:
                QTitleList.append(QtWidgets.QListWidgetItem(title))
            for i in range(len(QTitleList)):
                self.RSSList.insertItem(i+1, QTitleList[i])
            self.RSSContains.setText(self.summaryList[0])

    def pushCon(self):
        currentIndex = self.RSSList.currentRow()
        self.RSSContains.setText(self.summaryList[currentIndex])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
