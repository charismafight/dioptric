import sys
from actual_main import Actual_Main
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Actual_Main()
    ui.show()
    sys.exit(app.exec_())
