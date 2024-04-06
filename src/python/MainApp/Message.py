import uuid


class Message:
    __message_id = ''
    __user_id = ''
    __message_text = ''

    def __init__(self, user_id, message):
        self.__message_id = uuid.uuid4()
        self.__message_text = message
        self.__user_id = user_id

    def get_message(self):
        return self.__message_text

    def get_user_from_message(self):
        return self.__user_id

    def get_message_id(self):
        return self.__message_id
