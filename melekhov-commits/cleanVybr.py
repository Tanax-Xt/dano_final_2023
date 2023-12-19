def remove_outliers_iqr(data):
    # Сортируем данные
    sorted_data = sorted(data)

    # Вычисляем первый и третий квартили
    q1_index = int(len(sorted_data) * 0.25)
    q3_index = int(len(sorted_data) * 0.75)

    Q1 = sorted_data[q1_index]
    Q3 = sorted_data[q3_index]

    # Вычисляем межквантильный размах
    IQR = Q3 - Q1

    # Определяем границы для определения выбросов
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Удаляем выбросы из данных
    data_cleaned = [value for value in data if lower_bound <= value <= upper_bound]

    return data_cleaned


# Пример использования
# Замените 'your_data' на ваш список данных
your_data = [-10000, 1, 2, 3, 4, 5, 10, 15, 20, 25, 100]

data_cleaned = remove_outliers_iqr(your_data)

# Теперь data_cleaned содержит данные без выбросов по межквантильному размаху.
print(data_cleaned)