import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Тип хранилища состояний
from aiogram.contrib.middlewares.logging import LoggingMiddleware  # Встроенное в библиотеку aiogram логирование


# Инициализация бота и диспетчера
bot = Bot(token='5179000952:AAGsIIsRCIFhuDGOs-gk3uzh2TQb1f7zOYY')
dp = Dispatcher(bot)  # Указание типа хранилища состояний в оперативную память

# Логирование
logging.basicConfig(level=logging.INFO)


# Функция при отключении, закрывает соединения с хранилищем состояний бота
async def shutdown(dispatcher: Dispatcher):
    print('Отключаюсь')
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


# Вывод версии Python при старте
async def startup(dispatcher: Dispatcher):
    from sys import version_info
    r = version_info.releaselevel
    f = '' if r == 'final' else r
    print(f'Python {version_info.major}.{version_info.minor}.{version_info.micro} {f}')

