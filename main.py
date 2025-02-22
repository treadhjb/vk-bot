import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os

TOKEN = os.getenv("VK_TOKEN")  # Токен берется из переменных окружения

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)

def send_message(user_id, message):
    vk_session.method("messages.send", {"user_id": user_id, "message": message, "random_id": 0})

print("Бот запущен...")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        send_message(event.user_id, "Привет! Я бот.")
