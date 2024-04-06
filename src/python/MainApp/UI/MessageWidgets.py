import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap, QColor
import Message

class MessageWidget(QWidget):
    __message: Message
    #, username, message, action
    def __init__(self, message:Message):
        super(MessageWidget, self).__init__()
        self.__message = message
        status = message.get_status()
        if status == 'ban':
            background_color = "red"
        elif status == 'mute':
            background_color = "yellow"
        elif status == 'warning':
            background_color = "green"
        else:
            background_color = "transparent"

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # pixmap = QPixmap(image_path)
        # image_label = QLabel()
        # image_label.setPixmap(pixmap)
        messages = message.get_user_from_message().get_username()
        username_label = QLabel(messages)
        username_label.setStyleSheet("color: black; font-weight: bold;")

        text_label = QLabel(message.get_message())

        #layout.addWidget(image_label)
        layout.addWidget(username_label)
        layout.addWidget(text_label)

        self.setStyleSheet(f"background-color: {background_color};")
        self.setLayout(layout)
