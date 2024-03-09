from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d').date()

        # Отримуємо поточну дату
        today = datetime.today().date()

        # Розраховуємо різницю у днях
        days_difference = (today - input_date).days

        return days_difference
    except ValueError:
        # Обробляємо виняток у разі неправильного формату вхідної дати
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

# Приклад використання:
current_date = datetime.today().strftime('%Y-%m-%d')
result = get_days_from_today("2025-01-01")

print(result)


