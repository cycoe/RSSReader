# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cycoe/python/pyqt_project/RSS_Reader/RSSManager.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class RSSManager(QtWidgets.QDialog):
    def __init__(self,  rssSubFile):
        QtWidgets.QDialog.__init__(self)
        self.rssSubFile = rssSubFile
        self.setObjectName("RSSManager")
        self.setFixedSize(600, 400)
        self.setSizeGripEnabled(True)
        self.subList = QtWidgets.QListWidget(self)
        self.subList.setGeometry(QtCore.QRect(10, 10, 460, 380))
        self.subList.setObjectName("subList")
        self.restoreRssSubList()
        self.addNewBT = QtWidgets.QPushButton(self)
        self.addNewBT.setGeometry(QtCore.QRect(490, 48, 90, 40))
        self.addNewBT.setObjectName("addNewBT")
        self.addNewBT.setText("新增")
        self.removeBT = QtWidgets.QPushButton(self)
        self.removeBT.setGeometry(QtCore.QRect(490, 136, 90, 40))
        self.removeBT.setObjectName("removeBT")
        self.removeBT.setText("删除")
        self.applyBT = QtWidgets.QPushButton(self)
        self.applyBT.setGeometry(QtCore.QRect(490, 224, 90, 40))
        self.applyBT.setObjectName("applyBT")
        self.applyBT.setText("应用")
        self.qiutBT = QtWidgets.QPushButton(self)
        self.qiutBT.setGeometry(QtCore.QRect(490, 312, 90, 40))
        self.qiutBT.setObjectName("qiutBT")
        self.qiutBT.setText("丢弃")
        
        self.addNewBT.clicked.connect(self.addNewSub)
        self.removeBT.clicked.connect(self.delSub)
        self.applyBT.clicked.connect(self.applyChange)
        self.qiutBT.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    
    def restoreRssSubList(self):
        with open(self.rssSubFile) as f:
            self.rssSubList = f.readlines()
        QRssSubList = []
        for rssSub in self.rssSubList:
            QRssSubList.append(QtWidgets.QListWidgetItem(rssSub))
        for i in range(len(QRssSubList)):
            self.subList.insertItem(i+1,  QRssSubList[i])
    
    def addNewSub(self):
        self.newSub, isCommit = QtWidgets.QInputDialog.getText(self, '新增RSS源', '输入RSS源')
        if isCommit:
            self.rssSubList.append(self.newSub)
            self.subList.insertItem(len(self.rssSubList), QtWidgets.QListWidgetItem(self.newSub))
            
    def delSub(self):
        currentIndex = self.subList.currentRow()
        del(self.rssSubList[currentIndex])
        self.subList.clear()
        QRssSubList = []
        for rssSub in self.rssSubList:
            QRssSubList.append(QtWidgets.QListWidgetItem(rssSub))
        for i in range(len(QRssSubList)):
            self.subList.insertItem(i+1,  QRssSubList[i])
    
    def applyChange(self):
        with open(self.rssSubFile, 'w') as fr:
            for rssSub in self.rssSubList:
                fr.write(rssSub)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rssManager = RSSManager('rssSubList')
    rssManager.show()
    sys.exit(app.exec_())

