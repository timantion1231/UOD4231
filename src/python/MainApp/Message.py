import uuid
import User
from AI import *
class Message:
    __message_id = None
    __user: User
    __message_text = None
    __message_status = None
    ai: ArtInt

    def __init__(self, user: User, message):
        self.__message_id = uuid.uuid4()
        self.__message_text = message
        self.__user = user
        self.ai = ArtInt()
        self.__message_status = self.ai.get_emotion(message)



    def get_message(self):
        return self.__message_text

    def get_user_from_message(self):
        return self.__user

    def get_message_id(self):
        return self.__message_id

    def get_status(self):
        return self.__message_status

    def set_status(self, status):
        self.__message_status = status
