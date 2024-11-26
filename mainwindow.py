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
from pandas import DataFrame

class MainWindow(QMainWindow):
#   Dados
    planilha: DataFrame = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.buttonSendEmail.clicked.connect(self.enviar_emails)
        self.ui.buttonSelectFile.clicked.connect(self.selecionar_planilha)


    def resetar_email(self):
        try:
            resposta = QMessageBox.question(
                self,
                "Aviso",
                "Esta ação vai apagar todo o texto na caixa acima. Tem certeza de que deseja resetar o seu e-mail?",
                QMessageBox.Yes | QMessageBox.No
            )

            if resposta == QMessageBox.Yes:
                self.ui.inputText.setPlainText("Insira seu texto aqui")

        except Exception as e:
            print(f"Erro ao resetar o texto: {e}")

    def enviar_emails(self):
        try:
            ...
        except Exception as e:
            print(f"Não foi possível enviar os emails: {e}")

    def selecionar_planilha(self):
        try:
            caminho_arquivo = QFileDialog.getOpenFileName(
                self, 'Selecione a planilha bacana com os CNPJs', ''
            )

            if len(caminho_arquivo[0]) == 0:
                QMessageBox.information(
                    self,
                    "Erro!",
                    "Nenhum arquivo foi selecionado"
                )
                return

#            if self.planilha != None:
#                resposta = QMessageBox.question(
#                    self,
#                    "Aviso!",
#                    f"Já existe uma planilha ({self.planilha}) aberta. Deseja fechá-la e abrir a planilha {caminho_arquivo}",
#                    QMessageBox.Yes | QMessageBox.No
#                )
#                if resposta == QMessageBox.No:
#                    return

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

            self.planilha = df_cnpjs
            return df_cnpjs
        except Exception as e:
            print(f"Erro ao selecionar planilha: \033[31m{e}\033[0m")

    def atualizar_dataframe(self):
        try:
            print("Ainda não implementado!")
        except Exception as e:
            print(f"Erro ao atualizar os dados no dataframe: {e}")

    def atualizar_lista(self):
        try:
            print("Ainda não implementado!")
        except Exception as e:
            print(f"Erro ao atualizar a lista de empresas: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
#    apply_stylesheet(app, theme='dark_teal.xml')
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

