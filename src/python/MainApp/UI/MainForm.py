import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, \
    QPushButton, QLineEdit, QTextEdit
from UI.usersWidget import UserWidget
from UI.MessageWidgets import MessageWidget
import User
import Message


class MainForm(QWidget):
    __user_path = 'D:/study/чмв/овтеты/design/free-icon-image-4577383.png'
    __grid_layout = ''

    __message_scroll_area = ''
    __message_scroll_area_widget = ''
    __message_scroll_area_layout = ''

    __user_scroll_area = ''
    __user_scroll_area_widget = ''
    __user_scroll_area_layout = ''

    __user_list = []
    __message_list = []
    def __init__(self):
        super(MainForm, self).__init__()
        self.setGeometry(150, 150, 800, 800)
        self.__grid_layout = QGridLayout(self)

        self.__user_scroll_area = QScrollArea()
        self.__user_scroll_area.setWidgetResizable(True)
        self.__user_scroll_area_widget = QWidget()
        self.__user_scroll_area_layout = QVBoxLayout(self.__user_scroll_area_widget)
        self.__user_scroll_area.setWidget(self.__user_scroll_area_widget)

        for i in range(50):
            act = random.randint(0, 6)
            if act == 0:
                act = 'ban'
            elif act == 1:
                act = 'mute'
            elif act == 2:
                act = "warning"
            else:
                act = "pass"
            usr = User.User(f"User {i + 1}", self.__user_path, act)
            self.__add_user(usr)

        self.__message_scroll_area = QScrollArea()
        self.__message_scroll_area.setWidgetResizable(True)
        self.__message_scroll_area_widget = QWidget()
        self.__message_scroll_area_layout = QVBoxLayout(self.__message_scroll_area_widget)
        self.__message_scroll_area.setWidget(self.__message_scroll_area_widget)

        for i in range(50):
            act = random.randint(0, 6)
            if act == 0:
                act = 'ban'
            elif act == 1:
                act = 'mute'
            elif act == 2:
                act = "warning"
            else:
                act = "pass"
            msg = Message.Message(self.__user_list[i], f"Message {i + 1}", act)
            self.__add_message(msg)

        buttons_layout = QHBoxLayout()

        ban_button = QPushButton("Бан")
        ban_button.setStyleSheet('background-color: red;')
        mute_button = QPushButton("Мут")
        mute_button.setStyleSheet('background-color: yellow;')
        warning_button = QPushButton("Предупреждение")
        warning_button.setStyleSheet('background-color: green;')
        skip_button = QPushButton("Пропустить")
        skip_button.setStyleSheet('background-color: cyan;')

        buttons_layout.addWidget(ban_button)
        buttons_layout.addWidget(mute_button)
        buttons_layout.addWidget(warning_button)
        buttons_layout.addWidget(skip_button)

        self.__grid_layout.addLayout(buttons_layout, 1, 0, 1, 2)

        text_field = QTextEdit()
        text_field.setPlaceholderText("Введите текст сообщения...")

        send_button = QPushButton("Отправить")

        self.__grid_layout.addWidget(text_field, 2, 0)
        self.__grid_layout.addWidget(send_button, 2, 1)

    def __add_user(self, user: User):

        self.__user_scroll_area_layout.addWidget(
            UserWidget(user))

        self.__grid_layout.addWidget(self.__user_scroll_area, 0, 0)
        self.__user_list.append(user)

    def __add_message(self, message: Message):

        self.__message_scroll_area_layout.addWidget(
            MessageWidget(message))

        self.__grid_layout.addWidget(self.__message_scroll_area, 0, 1)
        self.__message_list.append(message)


def run_app():
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())
