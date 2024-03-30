import AI
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(945, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 291, 611))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 609))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(270, 0, 16, 611))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 55, 16))
        self.label_4.setObjectName("label_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(290, 0, 651, 521))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 649, 519))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(630, 0, 16, 531))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setGeometry(QtCore.QRect(10, 90, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setGeometry(QtCore.QRect(10, 140, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setGeometry(QtCore.QRect(10, 190, 55, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setGeometry(QtCore.QRect(10, 170, 55, 16))
        self.label_12.setObjectName("label_12")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.te_message = QtWidgets.QTextEdit(self.centralwidget)
        self.te_message.setGeometry(QtCore.QRect(290, 570, 531, 41))
        self.te_message.setObjectName("te_message")

        self.btn_ban = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ban.setGeometry(QtCore.QRect(290, 520, 141, 51))
        self.btn_ban.setObjectName("btn_ban")
        self.btn_ban.clicked.connect(self.btn_ban_click)

        self.btn_mute = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mute.setGeometry(QtCore.QRect(450, 520, 141, 51))
        self.btn_mute.setObjectName("btn_mute")
        self.btn_mute.clicked.connect(self.btn_ban_click)

        self.btn_warning = QtWidgets.QPushButton(self.centralwidget)
        self.btn_warning.setGeometry(QtCore.QRect(610, 520, 141, 51))
        self.btn_warning.setObjectName("btn_warning")
        self.btn_warning.clicked.connect(self.btn_warning_click)

        self.btn_skip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_skip.setGeometry(QtCore.QRect(770, 520, 141, 51))
        self.btn_skip.setObjectName("btn_skip")
        self.btn_skip.clicked.connect(self.btn_skip_click)

        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send.setGeometry(QtCore.QRect(850, 570, 81, 41))
        self.btn_send.setObjectName("btn_send")
        self.btn_send.clicked.connect(self.btn_send_click)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "User 1"))
        self.label_2.setText(_translate("MainWindow", "User 2"))
        self.label_3.setText(_translate("MainWindow", "User 3"))
        self.label_4.setText(_translate("MainWindow", "User 4"))
        self.label_5.setText(_translate("MainWindow", "User 1"))
        self.label_6.setText(_translate("MainWindow", "Message1"))
        self.label_7.setText(_translate("MainWindow", "Message2"))
        self.label_8.setText(_translate("MainWindow", "User 2"))
        self.label_9.setText(_translate("MainWindow", "Message3"))
        self.label_10.setText(_translate("MainWindow", "User 1"))
        self.label_11.setText(_translate("MainWindow", "Message4"))
        self.label_12.setText(_translate("MainWindow", "User 3"))
        self.btn_ban.setText(_translate("MainWindow", "Бан"))
        self.btn_mute.setText(_translate("MainWindow", "Мут"))
        self.btn_warning.setText(_translate("MainWindow", "Предупреждение"))
        self.btn_skip.setText(_translate("MainWindow", "Пропустить"))
        self.btn_send.setText(_translate("MainWindow", "Отправить"))

    def btn_ban_click(self):
        pass

    def btn_send_click(self):
        s = AI.Tokens
        tokens, words = s.get_tokens_from_text(self.te_message.toPlainText().split())
        print(tokens)
        print(words)

    def btn_mute_ckick(self):
        pass

    def btn_warning_click(self):
        pass

    def btn_skip_click(self):
        pass


def startUI():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def ch():
    print("clicked")