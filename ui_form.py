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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(696, 471)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
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
        self.buttonSelectFile = QPushButton(self.frame_2)
        self.buttonSelectFile.setObjectName(u"buttonSelectFile")

        self.horizontalLayout.addWidget(self.buttonSelectFile)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonSelectAll = QPushButton(self.frame_2)
        self.buttonSelectAll.setObjectName(u"buttonSelectAll")

        self.horizontalLayout.addWidget(self.buttonSelectAll)

        self.buttonFilter = QPushButton(self.frame_2)
        self.buttonFilter.setObjectName(u"buttonFilter")

        self.horizontalLayout.addWidget(self.buttonFilter)


        self.verticalLayout.addWidget(self.frame_2)

        self.treeView = QTreeView(self.frame)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.treeView)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.inputText = QPlainTextEdit(self.frame_4)
        self.inputText.setObjectName(u"inputText")
        self.inputText.setMaximumSize(QSize(16777215, 16777215))
        self.inputText.setReadOnly(False)

        self.verticalLayout_2.addWidget(self.inputText)

        self.buttonSendEmail = QPushButton(self.frame_4)
        self.buttonSendEmail.setObjectName(u"buttonSendEmail")
        self.buttonSendEmail.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.buttonSendEmail)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 696, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.buttonSendEmail.clicked.connect(self.inputText.show)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonSelectFile.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivo", None))
        self.buttonSelectAll.setText(QCoreApplication.translate("MainWindow", u"Selecionar tudo", None))
        self.buttonFilter.setText(QCoreApplication.translate("MainWindow", u"Filtros", None))
        self.inputText.setPlainText(QCoreApplication.translate("MainWindow", u"Escreva seu texto", None))
        self.buttonSendEmail.setText(QCoreApplication.translate("MainWindow", u"Enviar e-mails", None))
    # retranslateUi

