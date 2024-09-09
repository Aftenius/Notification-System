import time
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, user, event_type):
        pass


class PushNotification(Notification):
    def send(self, user, event_type):
        print(f"Отправлено Push уведомление пользователю {user} о событии {event_type}")


class EmailNotification(Notification):
    def send(self, user, event_type):
        print(f"Отправлено Email уведомление пользователю {user} о событии {event_type}")


class MessengerNotification(Notification):
    def send(self, user, event_type):
        print(f"Отправлено Messenger уведомление пользователю {user} о событии {event_type}")


class NotificationFactory:
    def __init__(self):
        self._creators = {
            "push": PushNotification,
            "email": EmailNotification,
            "messenger": MessengerNotification,
        }

    def get_notification(self, notification_type):
        notification_class = self._creators.get(notification_type)
        if not notification_class:
            raise ValueError(f"Неизвестный тип уведомления: {notification_type}")
        return notification_class()


def send_notifications(user_settings_list, event_type):
    factory = NotificationFactory()
    
    for user_id, user_settings in user_settings_list.items():

        try:
            push_notification = factory.get_notification("push")
            push_notification.send(user_id, event_type)
        except ValueError as e:
            print(f"Ошибка: {e}")


        if user_settings.get(event_type):
            for notif_type in ["email", "messenger"]:
                if user_settings.get(notif_type):
                    try:
                        notification = factory.get_notification(notif_type)
                        notification.send(user_settings['first_name'], event_type)
                    except ValueError as e:
                        print(f"Ошибка: {e}")
        else:
            print(f"Пользователь {user_settings['first_name']} не настроил уведомления для события {event_type}")


users_settings_notifications = {
    1: {
        "first_name":"Bob",
        "email": True,
        "messenger": False,
        "new_task": True,
        "successful_task": False,
        "free_hand": True,
    },
    2: {
        "first_name":"Tom",
        "email": True,
        "messenger": False,
        "new_task": False,
        "successful_task": False,
        "free_hand": True,
    },
    3: {
        "first_name":"Lambert",
        "email": True,
        "messenger": False,
        "new_task": True,
        "successful_task": False,
        "free_hand": True,
    },
    4: {
        "first_name":"Wong",
        "email": True,
        "messenger": False,
        "new_task": False,
        "successful_task": False,
        "free_hand": True,
    },
}

start_time = time.time()

send_notifications(users_settings_notifications, "successful_task")

end_time = time.time()

print(f"Time taken: {end_time - start_time:.4f} seconds")