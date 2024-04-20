from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLabel, \
    QListWidgetItem, QWidget
import sys
from UI.UserCreation import *

from PyQt5.QtCore import pyqtSignal

import User, UI.usersWidget
from UI.UserCreation import UserCreationDialog


class UserSelectionDialog(QDialog):
    user_selected = pyqtSignal(User.User)
    __selected_user: User
    cancel_selection = pyqtSignal()
    __user_creation = None
    
    __list_widget = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выбор пользователя")
        layout = QVBoxLayout()

        self.selected_user_label = QLabel("Выбранный пользователь:")
        layout.addWidget(self.selected_user_label)

        self.__list_widget = QListWidget()

        self.__add_demo_users()

        def on_item_clicked(item):
            widget: UI.usersWidget.UserWidget = self.__list_widget.itemWidget(item)
            self.__selected_user = widget.get_user_fromWidget()
            print("selected")

        self.__list_widget.itemClicked.connect(on_item_clicked)

        layout.addWidget(self.__list_widget)

        create_user_button = QPushButton("Создать пользователя")
        create_user_button.clicked.connect(self.__btn_create_user_click)
        layout.addWidget(create_user_button)

        buttons_layout = QHBoxLayout()
        ok_button = QPushButton("Ок")
        ok_button.clicked.connect(self.__btn_ok_clicked)
        cancel_button = QPushButton("Отмена")
        cancel_button.clicked.connect(self.__btn_cancel_click)

        buttons_layout.addWidget(ok_button)
        buttons_layout.addWidget(cancel_button)

        layout.addLayout(buttons_layout)

        self.setLayout(layout)
        
    def __add_demo_users(self):
        for i in range(0, 10):
            usr = User.User(f"User {i}", 'D:/study/чмв/овтеты/design/free-icon-image-4577383.png', "f")
            uw = UI.usersWidget.UserWidget(usr)
            item = QListWidgetItem()
            self.__list_widget.addItem(item)
            self.__list_widget.setItemWidget(item, uw)

    def __btn_ok_clicked(self):
        print('ok clicked')
        self.user_selected.emit(self.__selected_user)
        self.accept()

    def __btn_cancel_click(self):
        self.cancel_selection.emit()
        self.reject()

    def __btn_create_user_click(self):
        self.__user_creation = UserCreationDialog()

        self.__user_creation.created_user.connect(self.user_created)
        self.__user_creation.cancel_creating.connect(self.cancel_creation)
        self.__user_creation.show()
        self.setDisabled(True)

    def user_created(self, user: User):
        self.__selected_user = user
        print(f"user_created{user}")
        self.setDisabled(False)

    def cancel_creation(self):
        self.setDisabled(False)
