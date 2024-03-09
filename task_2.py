import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка валідності вхідних параметрів
    if not (1 <= min <= max <= 1000):
        return []

    # Генерація випадкових унікальних чисел
    numbers_set = set()
    while len(numbers_set) < quantity:
        random_number = random.randint(min, max)
        numbers_set.add(random_number)

    # Сортування та повернення результату
    result = sorted(list(numbers_set))
    return result

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)