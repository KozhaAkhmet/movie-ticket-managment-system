import datetime
from abc import ABC


class Notification(ABC):
    def __init__(self,
                 notification_id: int,
                 content: str):
        self.__notification_id = notification_id
        self.__created_on = datetime.date.today()
        self.__content = content

    def send_notification(self):
        pass


class EmailNotification(Notification):
    def send_notification(self):
        pass


class SmsNotification(Notification):
    def send_notification(self):
        pass
