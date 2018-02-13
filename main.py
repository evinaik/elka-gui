import sys
from PyQt5 import QtWidgets
from ui.EntryWindow import EntryWindow




app = QtWidgets.QApplication(sys.argv)
ui = EntryWindow()
ui.show()
sys.exit(app.exec_())