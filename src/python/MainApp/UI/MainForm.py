import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, \
    QPushButton, QLineEdit, QTextEdit
from UI.usersWidget import UserWidget
from UI.MessageWidgets import MessageWidget


class MainForm(QWidget):
    user_path = 'D:/study/чмв/овтеты/design/free-icon-image-4577383.png'
    def __init__(self):
        super(MainForm, self).__init__()
        self.setGeometry(150, 150, 800, 800)
        grid_layout = QGridLayout(self)
        user_scroll_area = QScrollArea()
        user_scroll_area.setWidgetResizable(True)
        user_scroll_area_widget = QWidget()
        user_scroll_area_layout = QVBoxLayout(user_scroll_area_widget)
        for i in range(50):
            user_scroll_area_layout.addWidget(
                UserWidget(self.user_path, f"User {i + 1}", f"User {i + 1} description", "dmute"))
        user_scroll_area.setWidget(user_scroll_area_widget)

        message_scroll_area = QScrollArea()
        message_scroll_area.setWidgetResizable(True)
        message_scroll_area_widget = QWidget()
        message_scroll_area_layout = QVBoxLayout(message_scroll_area_widget)
        for i in range(5):
            message_scroll_area_layout.addWidget(
                MessageWidget( f"User {i + 1}", f"Message {i + 1}", "ban"))

        message_scroll_area.setWidget(message_scroll_area_widget)

        grid_layout.addWidget(user_scroll_area, 0, 0)
        grid_layout.addWidget(message_scroll_area, 0, 1)

        buttons_layout = QHBoxLayout()

        ban_button = QPushButton("Бан")
        mute_button = QPushButton("Мут")
        warning_button = QPushButton("Предупреждение")
        skip_button = QPushButton("Пропустить")

        buttons_layout.addWidget(ban_button)
        buttons_layout.addWidget(mute_button)
        buttons_layout.addWidget(warning_button)
        buttons_layout.addWidget(skip_button)

        grid_layout.addLayout(buttons_layout, 1, 0, 1, 2)

        text_field = QTextEdit()
        text_field.setPlaceholderText("Введите текст сообщения...")

        send_button = QPushButton("Отправить")

        grid_layout.addWidget(text_field, 2, 0)
        grid_layout.addWidget(send_button, 2, 1)



def runApp():
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())
