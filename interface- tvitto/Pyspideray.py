# -*- coding: utf-8 -*-
"""
Created on Thu May  7 01:51:55 2020

@author: ah_su
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(50, 80, 321, 421))
        self.listView.setTextElideMode(QtCore.Qt.ElideRight)
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(460, 80, 321, 421))
        self.listView_2.setObjectName("listView_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 281, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 50, 241, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 530, 221, 41))
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(470, 90, 301, 401))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(60, 90, 301, 401))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Twitto"))
        self.listView.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "                     DESCRIPTION LIST"))
        self.label_2.setText(_translate("MainWindow", "FREQUENTLY USED WORDS"))
        self.label_3.setText(_translate("MainWindow", "ACCURACY  :  0.4836722119531731"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "aa"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "aaron"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "abc"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "aberdeen"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "ability"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "able"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "absolute"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "absolutely"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "absurdity"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "abuse"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "ac"))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "academia"))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "academic"))
        item = self.listWidget.item(13)
        item.setText(_translate("MainWindow", "academy"))
        item = self.listWidget.item(14)
        item.setText(_translate("MainWindow", "acc"))
        item = self.listWidget.item(15)
        item.setText(_translate("MainWindow", "accept"))
        item = self.listWidget.item(16)
        item.setText(_translate("MainWindow", "accepted"))
        item = self.listWidget.item(17)
        item.setText(_translate("MainWindow", "accepting"))
        item = self.listWidget.item(18)
        item.setText(_translate("MainWindow", "access"))
        item = self.listWidget.item(19)
        item.setText(_translate("MainWindow", "accessible"))
        item = self.listWidget.item(20)
        item.setText(_translate("MainWindow", "accessory"))
        item = self.listWidget.item(21)
        item.setText(_translate("MainWindow", "accident"))
        item = self.listWidget.item(22)
        item.setText(_translate("MainWindow", "accommodation"))
        item = self.listWidget.item(23)
        item.setText(_translate("MainWindow", "accomplish"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "i sing my own rhythm"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "i m the author of novel filled with family drama and romance"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "louis whining and squealing and all"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "mobile guy er shazam google kleiner perkins yahoo sprint pc airtouch air force stanford gsb uva dad husband brother golfer"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "ricky wilson the best frontman kaiser chief the best band xxxx thank you kaiser chief for an incredible year of gig and memory to cherish always xxxxxxx"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("MainWindow", "you don t know me"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("MainWindow", "a global marketplace for image video and music sharing photo inspiration design tip video for the creative community"))
        item = self.listWidget_2.item(7)
        item.setText(_translate("MainWindow", "the secret of getting ahead is getting started"))
        item = self.listWidget_2.item(8)
        item.setText(_translate("MainWindow", "pll fan crazy about mcd ramen is bae"))
        item = self.listWidget_2.item(9)
        item.setText(_translate("MainWindow", "renaissance art historian university of nottingham fuelled by haribo partial to coffee and with a soft spot for renaissance china national teaching fellow"))
        item = self.listWidget_2.item(10)
        item.setText(_translate("MainWindow", "clean food that taste great while providing energy nutrient no guilt granola vegan paleo friendly option too cert organic gf kosher"))
        item = self.listWidget_2.item(11)
        item.setText(_translate("MainWindow", "highly extraordinary auction"))
        item = self.listWidget_2.item(12)
        item.setText(_translate("MainWindow", "senior xi xii mmxiv"))
        item = self.listWidget_2.item(13)
        item.setText(_translate("MainWindow", "come join the fastest blog network online today http t co s mfpa vgk and http t co mpuuqtyf g we cover credit repair credit card and bankruptcy"))
        item = self.listWidget_2.item(14)
        item.setText(_translate("MainWindow", "im just here for t p bo burnham and disney world"))
        item = self.listWidget_2.item(15)
        item.setText(_translate("MainWindow", "jmkm"))
        item = self.listWidget_2.item(16)
        item.setText(_translate("MainWindow", "over enthusiastic f fan model collector music fan and a film fanatic also an aspergian"))
        item = self.listWidget_2.item(17)
        item.setText(_translate("MainWindow", "artisan specializing in paper mache print making and fibre art art teacher and cat devotee find my page on fb http t co g bstg icv"))
        item = self.listWidget_2.item(18)
        item.setText(_translate("MainWindow", "he bled and died to take away my sin"))
        item = self.listWidget_2.item(19)
        item.setText(_translate("MainWindow", "union j xxxx"))
        item = self.listWidget_2.item(20)
        item.setText(_translate("MainWindow", "you had me from the start"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

