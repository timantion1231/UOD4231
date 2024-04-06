import uuid
import Message


class User:
    __messages_id = []
    __user_id = ''
    __username = ''
    __avatar_path = ''
    __status = ''

    def __init__(self, username, avatar_path, status):
        self.__user_id = uuid.uuid4()
        self.__username = username
        self.__avatar_path = avatar_path
        self.__status = status

    def get_user_id(self):
        return self.__user_id

    def get_username(self):
        return self.__username

    def get_messages(self):
        return self.__messages_id

    def get_avatar(self):
        return self.__avatar_path

    def get_status(self):
        return self.__status

    def add_message(self, message: Message):
        self.__messages_id.append(message.get_message_id())

    def change_status(self, status):
        self.__status = status