# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(900, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.botaoAbrir = QPushButton(self.frame_2)
        self.botaoAbrir.setObjectName(u"botaoAbrir")

        self.horizontalLayout.addWidget(self.botaoAbrir)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.totalCNPJs = QLabel(self.frame_4)
        self.totalCNPJs.setObjectName(u"totalCNPJs")

        self.horizontalLayout_3.addWidget(self.totalCNPJs)

        self.filtroPorte = QComboBox(self.frame_4)
        self.filtroPorte.setObjectName(u"filtroPorte")

        self.horizontalLayout_3.addWidget(self.filtroPorte)

        self.filtroNatJuridica = QComboBox(self.frame_4)
        self.filtroNatJuridica.setObjectName(u"filtroNatJuridica")

        self.horizontalLayout_3.addWidget(self.filtroNatJuridica)

        self.filtroCNAE = QComboBox(self.frame_4)
        self.filtroCNAE.setObjectName(u"filtroCNAE")

        self.horizontalLayout_3.addWidget(self.filtroCNAE)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.editorTexto = QTextEdit(self.frame_5)
        self.editorTexto.setObjectName(u"editorTexto")
        self.editorTexto.setMaximumSize(QSize(16777215, 16777215))
        self.editorTexto.setStyleSheet(u"border-color: rgb(141, 141, 141);")
        self.editorTexto.setFrameShape(QFrame.Shape.StyledPanel)
        self.editorTexto.setFrameShadow(QFrame.Shadow.Raised)
        self.editorTexto.setLineWidth(1)
        self.editorTexto.setMidLineWidth(0)

        self.verticalLayout_2.addWidget(self.editorTexto)

        self.botaoEnviar = QPushButton(self.frame_5)
        self.botaoEnviar.setObjectName(u"botaoEnviar")
        self.botaoEnviar.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.botaoEnviar)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.frame)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.botaoAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir Planilha", None))
        self.totalCNPJs.setText(QCoreApplication.translate("MainWindow", u"Total CNPJs: ", None))
        self.botaoEnviar.setText(QCoreApplication.translate("MainWindow", u"Enviar e-mails", None))
    # retranslateUi

