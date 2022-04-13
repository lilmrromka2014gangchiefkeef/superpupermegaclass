from aiogram import executor
from misc import dp, shutdown, startup

# Импорт пакетов с хэндлерами и клавиатурами
import handlers

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True)  # Запуск основного потока с ботом

