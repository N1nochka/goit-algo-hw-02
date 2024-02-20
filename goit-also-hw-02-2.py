from collections import deque

def is_palindrome(s):
    # Видаляємо пробіли та переводимо рядок у нижній регістр
    s = s.replace(" ", "").lower()
    # Створюємо двосторонню чергу та додаємо усі символи рядка до неї
    queue = deque(s)
    
    # Порівнюємо символи з обох кінців черги
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True