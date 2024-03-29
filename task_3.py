import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, окрім цифр та "+".
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)
    
     # Перевіряємо, чи номер починається з "+".
    if not cleaned_number.startswith('+'):

        # Додаємо міжнародний код "+380" до українських номерів.
        if cleaned_number.startswith('380'):
            cleaned_number = "+" + cleaned_number

        elif cleaned_number.startswith('80'):
            cleaned_number = "+3" + cleaned_number

        elif cleaned_number.startswith('0'):
            cleaned_number = "+38" + cleaned_number

        # Додаємо "+" до всіх потенційних закордонних номерів.
        else:
            cleaned_number = '+' + cleaned_number

    return cleaned_number

# Приклад використання:
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+442071838750",
    "442071838326",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)





