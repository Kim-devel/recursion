def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки равна 1, возвращаем числовое значение цифры или 1, если это ноль
    if len(str_number) == 1:
        return int(str_number) if str_number != "0" else 1

    # Преобразуем первую цифру в число
    first = int(str_number[0])

    # Если первая цифра — ноль, пропускаем её
    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))

    # Рекурсивно умножаем первую цифру на результат работы функции с оставшимися цифрами
    return first * get_multiplied_digits(int(str_number[1:]))


# Примеры использования
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24

result2 = get_multiplied_digits(402030)
print(result2)  # Вывод: 24
