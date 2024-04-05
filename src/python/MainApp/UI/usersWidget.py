import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap, QColor

class UserWidget(QWidget):
    def __init__(self, image_path, username, message, action):
        super(UserWidget, self).__init__()
        if action == 'ban':
            background_color = "red"
        elif action == 'mute':
            background_color = "yellow"
        elif action == 'warning':
            background_color = "green"
        else:
            background_color = "transparent"
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        pixmap = QPixmap(image_path).scaled(50, 50)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setStyleSheet(f"background-color: {background_color};")

        name_label = QLabel(username)
        name_label.setStyleSheet("color: black; font-weight: bold;")

        text_label = QLabel(message)

        layout.addWidget(image_label)
        layout.addWidget(name_label)
        layout.addWidget(text_label)

        self.setLayout(layout)
