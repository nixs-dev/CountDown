from PyQt5 import QtWidgets
from views.Main import Ui_MainWindow 
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())
