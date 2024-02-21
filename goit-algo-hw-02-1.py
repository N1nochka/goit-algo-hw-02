from queue import Queue
import random

# Створення черги для заявок
queue = Queue()

# Функція для генерації нової заявки та додавання її до черги
def generate_request():
    new_request = "Заявка " + str(random.randint(1, 1000))  # Генеруємо випадковий номер
    queue.put(new_request)  # Додаємо заявку до черги
    print("Нова заявка:", new_request)

# Функція для обробки заявки з черги
def process_request():
    if not queue.empty():  # Перевіряємо, чи черга не порожня
        processed_request = queue.get()  # Видаляємо заявку з черги
        print("Оброблена заявка:", processed_request)
    else:
        print("Черга порожня")

# Головний цикл програми
try:
    while True:
        generate_request()  # Генерація нової заявки
        process_request()   # Обробка заявок
except KeyboardInterrupt:
    print("Користувач завершив програму")