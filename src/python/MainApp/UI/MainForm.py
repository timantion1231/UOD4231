import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, \
    QPushButton, QLineEdit, QTextEdit

from AI import *
from UI.usersWidget import UserWidget
from UI.MessageWidgets import MessageWidget
import User
import Message
from UI.AddMessage import *


class MainForm(QWidget):
    __user_path = 'resources/user_icon.png'
    __grid_layout = None

    __message_scroll_area = None
    __message_scroll_area_widget = None
    __message_scroll_area_layout = None

    __user_scroll_area = None
    __user_scroll_area_widget = None
    __user_scroll_area_layout = None

    __user_list = []
    __message_list = []

    __dialog = None

    __message_field = None

    __selected_message_widgets = []

    __message_widget = None

    __ai: ArtInt


    def __init__(self):
        self.__ai = ArtInt()
        super(MainForm, self).__init__()
        self.setGeometry(150, 150, 800, 800)
        self.__grid_layout = QGridLayout(self)

        self.__user_scroll_area = QScrollArea()
        self.__user_scroll_area.setWidgetResizable(True)
        self.__user_scroll_area_widget = QWidget()
        self.__user_scroll_area_layout = QVBoxLayout(self.__user_scroll_area_widget)
        self.__user_scroll_area.setWidget(self.__user_scroll_area_widget)
        self.add_demo_users()

        self.__message_scroll_area = QScrollArea()
        self.__message_scroll_area.setWidgetResizable(True)
        self.__message_scroll_area_widget = QWidget()
        self.__message_scroll_area_layout = QVBoxLayout(self.__message_scroll_area_widget)
        self.__message_scroll_area.setWidget(self.__message_scroll_area_widget)
        self.add_demo_messages()

        buttons_layout = QHBoxLayout()

        ban_button = QPushButton("Бан")
        ban_button.setStyleSheet('background-color: red;')
        ban_button.clicked.connect(self.ban_click)

        mute_button = QPushButton("Мут")
        mute_button.setStyleSheet('background-color: yellow;')
        mute_button.clicked.connect(self.mute_click)

        warning_button = QPushButton("Предупреждение")
        warning_button.setStyleSheet('background-color: green;')
        warning_button.clicked.connect(self.warning_click)

        skip_button = QPushButton("Пропустить")
        skip_button.setStyleSheet('background-color: cyan;')
        skip_button.clicked.connect(self.skip_click)

        buttons_layout.addWidget(ban_button)
        buttons_layout.addWidget(mute_button)
        buttons_layout.addWidget(warning_button)
        buttons_layout.addWidget(skip_button)

        self.__grid_layout.addLayout(buttons_layout, 1, 0, 1, 2)

        self.__message_field = QTextEdit()
        self.__message_field.setPlaceholderText("Введите текст сообщения...")

        send_button = QPushButton("Отправить")
        send_button.clicked.connect(self.__btn_send_click)

        self.__grid_layout.addWidget(self.__message_field, 2, 0)
        self.__grid_layout.addWidget(send_button, 2, 1)

    def __add_user(self, user: User):

        self.__user_scroll_area_layout.addWidget(
            UserWidget(user))

        self.__grid_layout.addWidget(self.__user_scroll_area, 0, 0)
        self.__user_list.append(user)

    def __add_message(self, message: Message):

        self.__message_widget = MessageWidget(message)
        self.__message_widget.clicked.connect(self.on_message_widget_clicked)

        self.__message_scroll_area_layout.addWidget(self.__message_widget)

        self.__grid_layout.addWidget(self.__message_scroll_area, 0, 1)
        self.__message_list.append(message)

    def __btn_send_click(self):
        self.__dialog = UI.AddMessage.UserSelectionDialog()
        self.__dialog.show()
        self.setDisabled(True)
        self.__dialog.user_selected.connect(self.selected_user)
        self.__dialog.cancel_selection.connect(self.cancel_selection)

    def selected_user(self, user):
        print(f"Выбран пользователь в главной форме: {user.get_username()}")
        self.setDisabled(False)
        msg_text = self.__message_field.toPlainText()
        msg = Message.Message(user, msg_text, self.__ai)
        self.__add_message(msg)

    def cancel_selection(self):
        self.setDisabled(False)

    def add_selected_message_widget(self, message_widget):
        # Добавить виджет сообщения в список выделенных элементов
        self.__selected_message_widgets.append(message_widget)
        message_widget.set_selected(True)

    def on_message_widget_clicked(self):
        sender_widget = self.sender()  # Получаем отправителя события
        if sender_widget in self.__selected_message_widgets:
            self.__selected_message_widgets.remove(sender_widget)
            sender_widget.set_selected(False)
            sender_widget.update()
        else:
            self.add_selected_message_widget(sender_widget)
            sender_widget.update()

    def add_demo_messages(self):
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
            msg = Message.Message(self.__user_list[i], f"Message {i + 1}", self.__ai)
            self.__add_message(msg)

    def add_demo_users(self):
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

    def mute_click(self):
        for widget in self.__selected_message_widgets:
            message = widget.get_message()
            if message:
                self.change_message_status(message, 'mute')

    def ban_click(self):
        for widget in self.__selected_message_widgets:
            message = widget.get_message()
            if message:
                self.change_message_status(message, 'ban')

    def warning_click(self):
        for widget in self.__selected_message_widgets:
            message = widget.get_message()
            if message:
                self.change_message_status(message, 'warning')

    def skip_click(self):
        for widget in self.__selected_message_widgets:
            message = widget.get_message()
            if message:
                self.change_message_status(message, 'pass')

    def change_message_status(self, message: Message, status):
        selected_widgets_copy = self.__selected_message_widgets.copy()
        for widget in selected_widgets_copy:
            if widget.get_message() == message:
                widget.set_selected(False)
                widget.setStyleSheet(f"background-color: {self.get_color_by_status(status)};")
                message.set_status(status)
                widget.update()
                self.__selected_message_widgets.remove(widget)
        for widget in self.__selected_message_widgets:
            widget.set_selected(True)



    def get_color_by_status(self, status: str) -> str:
        if status == 'ban':
            return 'red'
        elif status == 'mute':
            return 'yellow'
        elif status == 'warning':
            return 'green'
        elif status == 'pass':
            return 'cyan'
        else:
            return 'white'

    def change_user_status(self, user: User, status):
        pass

    def __add_user_to_blacklist(self, user: User):
        pass


def run_app():
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())

