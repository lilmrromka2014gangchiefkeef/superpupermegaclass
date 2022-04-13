from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура с отправкой местоположения (Запрашивает местоположение пользователя)
my_geo_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Моё местоположение 🌍', request_location=True))

# Клавиатура главного меню
button_history_peter = KeyboardButton('История Санкт-петербурга')
button_city = KeyboardButton('Достопримечательности Санкт-петербурга')
button_ways = KeyboardButton('Маршруты Санкт-петербурга')
main_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_history_peter).add(button_city).add(button_ways)

# Клавиатура выбора истории санкт петербурга
button_small = KeyboardButton('Краткая история')
button_big = KeyboardButton('Полная история')
button_back = KeyboardButton('⬅ Назад')
history_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_small).add(button_big).add(button_back)



# Клавиатура кнопка назад
button_back = KeyboardButton('⬅ Назад')
back_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_back)