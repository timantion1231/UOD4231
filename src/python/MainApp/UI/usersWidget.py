import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap, QColor
import User

class UserWidget(QWidget):
    #, image_path, username, message, action
    __user: User
    def __init__(self, user: User):
        super(UserWidget, self).__init__()
        self.__user = user
        status = user.get_status()
        if status == 'ban':
            background_color = "red"
        elif status == 'mute':
            background_color = "yellow"
        elif status == 'warning':
            background_color = "green"
        else:
            background_color = "transparent"
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        pixmap = QPixmap(user.get_avatar()).scaled(50, 50)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setStyleSheet(f"background-color: {background_color};")

        name_label = QLabel(user.get_username())
        name_label.setStyleSheet("color: black; font-weight: bold;")

        text_label = QLabel(str(user.get_messages()))

        layout.addWidget(image_label)
        layout.addWidget(name_label)
        layout.addWidget(text_label)

        self.setLayout(layout)

    def get_user_fromWidget(self):
        return self.__user
