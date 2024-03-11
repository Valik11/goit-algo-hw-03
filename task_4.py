from datetime import datetime, timedelta

# Дані про користувачі та їхні дні народження
users_data = [
    {"name": "John Doe", "birthday": "1985.03.17"},
    {"name": "Jane Smith", "birthday": "1990.03.16"},
    {"name": "Bruce Wayne", "birthday": "1990.03.11"}
]

def find_next_weekday(d, weekday: int):
    # Функція, що знаходить наступний робочий день
    days_ahead = weekday - d.weekday()
    if days_ahead < 0:
        days_ahead += 7
    return d + timedelta(days=days_ahead)

def prepare_users(users):
    # Функція для перетворення рядків дати народження в об'єкти datetime та підготовки списку користувачів
    prepared_users_list = []

    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
            prepared_users_list.append({"name": user['name'], 'birthday': birthday})
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')

    return prepared_users_list

def get_upcoming_birthdays(users):
    # Функція для знаходження користувачів, дні народження яких наступають на цьому тижні
    days = 7
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        # Якщо день народження вже пройшов у поточному році, розглядаємо його наступним роком
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи день народження наступає наступного тижня та чи не є він вихідним
        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                # Якщо вихідний, переносимо привітання на наступний понеділок
                birthday_this_year = find_next_weekday(birthday_this_year, 0)

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays

# Підготовка та вивід результату
prepared_users = prepare_users(users_data)
upcoming_birthdays = get_upcoming_birthdays(prepared_users)
print(upcoming_birthdays)
