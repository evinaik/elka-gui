# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../qt-ui/PlotWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        PlotWindow.setObjectName("PlotWindow")
        PlotWindow.resize(1024, 640)
        self.centralwidget = QtWidgets.QWidget(PlotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 991, 561))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.propertiesLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.propertiesLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.propertiesLabel.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.propertiesLabel.setFont(font)
        self.propertiesLabel.setObjectName("propertiesLabel")
        self.verticalLayout.addWidget(self.propertiesLabel)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.idLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.idLabel.setObjectName("idLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.idLabel)
        self.idLabelEdit = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.idLabelEdit.setObjectName("idLabelEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idLabelEdit)
        self.typeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.typeLabel.setObjectName("typeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.typeLabel)
        self.typeLabelEdit = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.typeLabelEdit.setObjectName("typeLabelEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.typeLabelEdit)
        self.batteryLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.batteryLabel.setObjectName("batteryLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.batteryLabel)
        self.batteryLabelEdit = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.batteryLabelEdit.setObjectName("batteryLabelEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.batteryLabelEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.bottomRight = PlotWidget(self.horizontalLayoutWidget)
        self.bottomRight.setObjectName("bottomRight")
        self.gridLayout.addWidget(self.bottomRight, 1, 2, 1, 1)
        self.topRight = PlotWidget(self.horizontalLayoutWidget)
        self.topRight.setObjectName("topRight")
        self.gridLayout.addWidget(self.topRight, 0, 2, 1, 1)
        self.bottomLeft = PlotWidget(self.horizontalLayoutWidget)
        self.bottomLeft.setObjectName("bottomLeft")
        self.gridLayout.addWidget(self.bottomLeft, 1, 0, 1, 1)
        self.topLeft = PlotWidget(self.horizontalLayoutWidget)
        self.topLeft.setObjectName("topLeft")
        self.gridLayout.addWidget(self.topLeft, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        PlotWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PlotWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        PlotWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PlotWindow)
        self.statusbar.setObjectName("statusbar")
        PlotWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PlotWindow)
        QtCore.QMetaObject.connectSlotsByName(PlotWindow)

    def retranslateUi(self, PlotWindow):
        _translate = QtCore.QCoreApplication.translate
        PlotWindow.setWindowTitle(_translate("PlotWindow", "ELKA Node Info"))
        self.propertiesLabel.setText(_translate("PlotWindow", "Properties"))
        self.idLabel.setText(_translate("PlotWindow", "ID:"))
        self.idLabelEdit.setText(_translate("PlotWindow", "TestID 1"))
        self.typeLabel.setText(_translate("PlotWindow", "Type:"))
        self.typeLabelEdit.setText(_translate("PlotWindow", "Ground Station"))
        self.batteryLabel.setText(_translate("PlotWindow", "Battery:"))
        self.batteryLabelEdit.setText(_translate("PlotWindow", "87%"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotWindow = QtWidgets.QMainWindow()
    ui = Ui_PlotWindow()
    ui.setupUi(PlotWindow)
    PlotWindow.show()
    sys.exit(app.exec_())

