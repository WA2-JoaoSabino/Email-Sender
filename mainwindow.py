# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

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
    planilha: DataFrame = pd.DataFrame
    teste = [
        (False, "Nome 1", None, 25),
        (True, None, "Dado 2", 345),
        (False, "Nome 3", "Dado 3", None)
    ]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.buttonSendEmail.clicked.connect(self.enviar_emails)
        self.ui.buttonSelectFile.clicked.connect(self.selecionar_planilha)

        self.ui.treeView.setItemsExpandable(False)

        self.atualizar_lista()


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
            self.printError("Erro ao resetar o texto", e)

    def enviar_emails(self):
        try:
            ...
        except Exception as e:
            self.printError("Não foi possível enviar os emails.", e)

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

            if not(self.planilha.empty):
                resposta = QMessageBox.question(
                    self,
                    "Aviso!",
                    f"Já existe uma planilha aberta. Deseja fechá-la e abrir a planilha em {caminho_arquivo[0]}",
                    QMessageBox.Yes | QMessageBox.No
                )
                if resposta == QMessageBox.No:
                    return

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

            self.atualizar_lista()

            self.planilha = df_cnpjs
            return df_cnpjs
        except Exception as e:
            self.printError("Erro ao selecionar a planilha.", e)

    def atualizar_dataframe(self):
        try:
            print("Ainda não implementado!")
        except Exception as e:
            self.printError("Erro ao atualizar os dados no dataframe.", e)

    def atualizar_lista(self):
        try:
            model = QStandardItemModel()
            dados = self.teste

            headerCheck = QStandardItem()
            headerCheck.setCheckable(True)
            model.setHorizontalHeaderLabels(["", "Nome da empresa", "CNPJ", "e-mail"])
            model.setHorizontalHeaderItem(0, headerCheck)

            for i in dados:
                col1 = QStandardItem()
                col1.setCheckable(True)
                col1.setCheckState(Qt.CheckState(2 if bool(i[0]) else 0))
                col1.setEditable(False)
                col2 = QStandardItem(str(i[1]))
                col2.setEditable(False)
                col3 = QStandardItem(str(i[2]))
                col3.setEditable(False)
                col4 = QStandardItem(str(i[3]))
                col4.setEditable(False)

                model.appendRow([col1, col2, col3, col4])
            
            self.ui.treeView.setModel(model)
            self.ui.treeView.setColumnWidth(0, 40)
            self.ui.treeView.setColumnWidth(1, 200)
            self.ui.treeView.setColumnWidth(2, 100)
            self.ui.treeView.setColumnWidth(3, 200)
            # Implementar função de alterar a checkbox quando a linha for clicada
            # self.ui.treeView.clicked.connect()

            print("Ainda não implementado!")
        except Exception as e:
            self.printError("Erro ao atualizar a lista de empresas.", e)

#   Mostra mensagens de erro no console de forma formatada. Auxilia a analisar mensagens de erro.
#   Uso: self.printError("mensagem", exception)
    def printError(self, message: str, error: Exception):
        print(f"\033[33m{message}\nMotivo: \033[31m{error}\033[0m")

if __name__ == "__main__":
    app = QApplication(sys.argv)
#    apply_stylesheet(app, theme='dark_teal.xml')
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

