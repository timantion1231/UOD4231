import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QPixmap, QColor

class MessageWidget(QWidget):
    def __init__(self, username, message, action):
        super(MessageWidget, self).__init__()

        if action == 'ban':
            background_color = "red"
        elif action == 'mute':
            background_color = "yellow"
        elif action == 'warning':
            background_color = "green"
        else:
            background_color = "transparent"

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # pixmap = QPixmap(image_path)
        # image_label = QLabel()
        # image_label.setPixmap(pixmap)

        username_label = QLabel(username)
        username_label.setStyleSheet("color: black; font-weight: bold;")

        text_label = QLabel(message)

        #layout.addWidget(image_label)
        layout.addWidget(username_label)
        layout.addWidget(text_label)

        self.setStyleSheet(f"background-color: {background_color};")
        self.setLayout(layout)
