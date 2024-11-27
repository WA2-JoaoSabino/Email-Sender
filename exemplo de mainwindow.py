# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from Interface.ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_treeview()
        self.populate_comboboxes()

        self.ui.pushButton_2.clicked.connect(self.btn_limpar)

    def setup_treeview(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Empresa", "Data"])

        item_coluna1 = QStandardItem("ItemColuna1")
        item_coluna2 = QStandardItem("ItemColuna2")

        model.appendRow([item_coluna1, item_coluna2])

        self.ui.treeView.setModel(model)

        header = self.ui.treeView.header()
        for i in range(header.count()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

    def populate_comboboxes(self):
        self.ui.comboBox.clear()
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()

        self.ui.comboBox.addItem("Item 1")
        self.ui.comboBox.addItem("Item 2")
        self.ui.comboBox.addItem("Item 3")

        self.ui.comboBox_2.addItem("Item 1")
        self.ui.comboBox_2.addItem("Item 2")
        self.ui.comboBox_2.addItem("Item 3")

        self.ui.comboBox_3.addItem("Item 1")
        self.ui.comboBox_3.addItem("Item 2")
        self.ui.comboBox_3.addItem("Item 3")

        self.ui.comboBox.setCurrentIndex(-1)
        self.ui.comboBox_2.setCurrentIndex(-1)
        self.ui.comboBox_3.setCurrentIndex(-1)

    def btn_limpar(self):
        self.ui.treeView.clearSelection()
        self.ui.comboBox.setCurrentIndex(-1)
        self.ui.comboBox_2.setCurrentIndex(-1)
        self.ui.comboBox_3.setCurrentIndex(-1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    widget = MainWindow()
    widget.setWindowIcon(QIcon("icone.ico"))
    widget.show()
    sys.exit(app.exec())
