from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLabel, \
    QListWidgetItem, QWidget
import sys

from PyQt5.QtCore import pyqtSignal

import User, UI.usersWidget


class UserSelectionDialog(QDialog):
    user_selected = pyqtSignal(User.User)
    __selected_user: User

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выбор пользователя")

        layout = QVBoxLayout()

        self.selected_user_label = QLabel("Выбранный пользователь:")
        layout.addWidget(self.selected_user_label)

        list_widget = QListWidget()

        for i in range(0, 10):
            usr = User.User(f"User {i}", 'D:/study/чмв/овтеты/design/free-icon-image-4577383.png', "f")
            uw = UI.usersWidget.UserWidget(usr)
            item = QListWidgetItem()
            list_widget.addItem(item)
            list_widget.setItemWidget(item, uw)

        def on_item_clicked(item):
            widget: UI.usersWidget.UserWidget = list_widget.itemWidget(item)
            self.__selected_user = widget.get_user_fromWidget()
            print("selected")


        list_widget.itemClicked.connect(on_item_clicked)

        layout.addWidget(list_widget)

        create_user_button = QPushButton("Создать пользователя")
        layout.addWidget(create_user_button)

        buttons_layout = QHBoxLayout()
        ok_button = QPushButton("Ок")
        ok_button.clicked.connect(self.__btn_ok_clicked)
        cancel_button = QPushButton("Отмена")
        cancel_button.clicked.connect(self.reject)

        buttons_layout.addWidget(ok_button)
        buttons_layout.addWidget(cancel_button)

        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def __btn_ok_clicked(self):
        print('ok clicked')
        self.user_selected.emit(self.__selected_user)
        self.accept()
