# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entry.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.MainWindow import Ui_MainWindow
from ui.InfoWindow import InfoWindow

import numpy as np

class EntryWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(EntryWindow, self).__init__()

        self.data = np.random.normal(size=(10,1000))
        self.ptr = 0

        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(50)

        self.setupUi(self)
        self.pushButton.clicked.connect(self.openPlots)

    def openPlots(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = InfoWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def update(self):
        self.topLeft.setData(self.data[self.ptr%10])
        if self.ptr == 0:
            self.topLeft.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
        self.ptr += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = EntryWindow()
    ui.show()
    sys.exit(app.exec_())

