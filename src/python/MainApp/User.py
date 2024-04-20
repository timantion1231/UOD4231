import uuid
import Message


class User:
    __messages_id = []
    __user_id = None
    __username = None
    __avatar_path = None
    __user_status = None

    def __init__(self, username, avatar_path='resources/user_icon.png', status='none'):
        self.__user_id = uuid.uuid4()
        self.__username = username
        self.__avatar_path = avatar_path
        self.__user_status = status

    def get_user_id(self):
        return self.__user_id

    def get_username(self):
        return self.__username

    def get_messages(self):
        return self.__messages_id

    def get_avatar(self):
        return self.__avatar_path

    def get_status(self):
        return self.__user_status

    def add_message(self, message: Message):
        self.__messages_id.append(message.get_message_id())

    def change_status(self, status):
        self.__user_status = status
