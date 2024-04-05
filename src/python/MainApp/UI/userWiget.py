from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class CustomWidget(QWidget):
    def __init__(self, image_path, text, parent=None):
        super(CustomWidget, self).__init__(parent)

        layout = QHBoxLayout(self)

        pixmap = QPixmap(image_path).scaled(50, 50)  # Загрузка изображения и изменение размера до 50x50
        image_label = QLabel()
        image_label.setPixmap(pixmap)

        text_label = QLabel(text)

        layout.addWidget(image_label)
        layout.addWidget(text_label)