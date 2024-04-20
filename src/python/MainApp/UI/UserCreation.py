import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit

from User import User


class UserCreationDialog(QDialog):
    created_user = pyqtSignal(User)
    __created_user: User
    cancel_creating = pyqtSignal()
    __username = None
    __text_field = None

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Диалоговое окно')

        layout = QVBoxLayout()

        title_label = QLabel('Заголовок диалогового окна')
        layout.addWidget(title_label)

        self.__text_field = QLineEdit()
        layout.addWidget(self.__text_field)

        ok_button = QPushButton('Ок')
        ok_button.clicked.connect(self.__btn_ok_click)
        layout.addWidget(ok_button)

        cancel_button = QPushButton('Отмена')
        cancel_button.clicked.connect(self.__btn_cancel_click)
        layout.addWidget(cancel_button)

        self.setLayout(layout)

    def __btn_ok_click(self):
        print(f"printed: {self.__text_field.text()}")
        self.created_user.emit(User(self.__text_field.text()))
        self.accept()

    def __btn_cancel_click(self):
        self.cancel_creating.emit()
        self.reject()
