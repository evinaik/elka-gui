# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entry.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.PlotWindow import Ui_PlotWindow

import pyqtgraph

import numpy as np

class InfoWindow(QtGui.QMainWindow, Ui_PlotWindow):
    def __init__(self):
        super(InfoWindow, self).__init__()

        self.data1 = np.random.normal(size=300)
        self.data2 = np.random.normal(size=300)
        self.data3 = np.random.normal(size=300)
        self.data4 = np.random.normal(size=300)
        
        self.ptr = 0
        self.b1 = 1
        self.b0 = np.random.normal()

        self.setupUi(self)

        self.topLeft.getPlotItem().setMouseEnabled(x=False, y=False)
        self.topLeft.getPlotItem().setDownsampling(mode='peak')
        self.topLeft.getPlotItem().setClipToView(True)
        self.topLeft.getPlotItem().setRange(xRange=[-100, 0])
        self.topLeft.getPlotItem().setLimits(xMax=0)

        self.timerTL = QtCore.QTimer()
        self.timerTL.timeout.connect(lambda: self.update(self.topLeft, self.data1))
        self.timerTL.start(50)

        self.topRight.setMouseEnabled(x=False, y=False)

        self.timerTR = QtCore.QTimer()
        self.timerTR.timeout.connect(lambda: self.update(self.topRight, self.data2))
        self.timerTR.start(50)

        self.bottomLeft.setMouseEnabled(x=False, y=False)

        self.timerBL = QtCore.QTimer()
        self.timerBL.timeout.connect(lambda: self.update(self.bottomLeft, self.data3))
        self.timerBL.start(50)

        self.bottomRight.setMouseEnabled(x=False, y=False)
        
        self.timerBR = QtCore.QTimer()
        self.timerBR.timeout.connect(lambda: self.update(self.bottomRight, self.data4))
        self.timerBR.start(50)

    def update(self, plt, data):
        plt.plot(data, clear=True)
        data[:-1] = data[1:]
        data[-1] = np.random.normal()
        self.ptr += 1

    # def update_line(self, plt, data):
    #     plt.plot(data, clear=True)
    #     data[:-1] = data[1:]
    #     data[-1] = (self.ptr % 10) * self.b1 + self.b0
    #     self.ptr += 1



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = InfoWindow()
    ui.show()
    sys.exit(app.exec_())

