from main import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem, QDialog, QWidget
from actual_case import Actual_Case


class Actual_Main(Ui_MainWindow):
    def __init__(self):
        super(Actual_Main, self).__init__()
        self.setupUi(self)
        self.load_data()
        self.dialog = QDialog()

    def show_add_case_from(self):
        ac = Actual_Case()
        # set up ui 是qtdesginer工具生成的函数，可以把生成的窗体信息设置到一个dialog或者window中去
        # 需要注意的是生成出来的class无法直接show，此外容器还必须放入主线程类的对象中，否则会一闪而过（由于show完之后立马继续运行，与win平台的差异不会默认在主线程中show）
        ac.setupUi(self.dialog)
        ac.bind_add()
        self.dialog.show()

    def load_data(self):
        # 获取数据，并动态加载到table中   pyqt没有直接绑定的函数，故只能代码实现
        self.tableWidget.setRowCount(1)
        test_item = QTableWidgetItem("测试")
        self.tableWidget.setItem(0, 0, test_item)
