import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap, QColor
import Message
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget
class MessageWidget(QWidget):
    __message: Message
    clicked = pyqtSignal()
    __selected = False
    __color = None
    __text_color = None
    __username_label = None
    __text_label = None
    def __init__(self, message:Message):
        super(MessageWidget, self).__init__()
        self.__message = message
        status = message.get_status()
        if status == 'ban':
            self.__color = "red"
            self.__text_color = self.__color
        elif status == 'mute':
            self.__color = "yellow"
            self.__text_color = self.__color
        elif status == 'warning':
            self.__color = "green"
            self.__text_color = self.__color
        else:
            self.__color = "transparent"
            self.__text_color = "black"

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        messages = message.get_user_from_message().get_username()
        self.__username_label = QLabel(messages)
        self.__username_label.setStyleSheet("color: black; font-weight: bold;")

        self.__text_label = QLabel(message.get_message())
        self.__text_label.setStyleSheet("color: black; font-weight: bold;")

        layout.addWidget(self.__username_label)
        layout.addWidget(self.__text_label)

        self.setStyleSheet(f"background-color: {self.__color};")
        self.setLayout(layout)

    def mousePressEvent(self, event):
        self.clicked.emit()

    def set_selected(self, selected):
        self.selected = selected
        if self.selected:
            self.setStyleSheet("background-color: lightblue;")
            self.__text_label.setStyleSheet(f"color: {self.__text_color}; font-weight: bold;")
            self.__username_label.setStyleSheet(f"color: {self.__text_color}; font-weight: bold;")
        else:
            self.setStyleSheet(f"background-color: {self.__color};")
            self.__text_label.setStyleSheet("color: black; font-weight: bold;")
            self.__username_label.setStyleSheet(f"color: {self.__text_color}; font-weight: bold;")