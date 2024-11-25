# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
# import qdarkstyle
from qt_material import apply_stylesheet
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.buttonSendEmail.clicked.connect(self.resetText)
        self.ui.buttonSelectFile.clicked.connect(self.selecionar_planilha)


    def resetText(self):
        try:
            self.ui.inputText.setPlainText("Insira seu texto aqui")
        except Exception as e:
            print(f"Erro ao resetar o texto: {e}")

    def enviar_emails(self):
        ...

    def selecionar_planilha(self):
        try:
            caminho_arquivo = QFileDialog.getOpenFileName(
                self, 'Selecione a planilha bacana com os CNPJs', ''
            )

            QMessageBox.information(
                self,
                "Informação Bacana",
                f"Planilha selecionada: {caminho_arquivo[0]}"
            )

            df_cnpjs = pd.read_excel(caminho_arquivo[0])

            QMessageBox.information(
                self,
                "Outra informação",
                f"Quantidade de CNPJs: {len(df_cnpjs)}"
            )

            return df_cnpjs
        except Exception as e:
            print(f"Erro ao selecionar planilha: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
#    apply_stylesheet(app, theme='dark_teal.xml')
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

