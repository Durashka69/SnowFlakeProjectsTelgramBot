import logging
import config

from asgiref.sync import sync_to_async
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ContentType

from apps.projects.models import Project


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    await message.answer(
        """
        Привет! Я бот для создания проектов в админке.
        \nЧтобы начать, отправь мне название своего проекта.
    """
    )


# Словарь для хранения данных о проекте
project_data = {}


# Обработчик сообщений
@dp.message_handler(content_types=ContentType.ANY)
async def create_project(message: types.Message):
    chat_id = message.chat.id

    # Запрашиваем заголовок проекта
    if "title" not in project_data:
        project_data["title"] = message.text
        await bot.send_message(
            chat_id, "Отлично! Теперь отправьте мне описание вашего проекта."
        )
    # Запрашиваем описание проекта
    elif "description" not in project_data:
        project_data["description"] = message.text
        await bot.send_message(chat_id, "Загрузите изображение вашего проекта.")
    # Запрашиваем изображение проекта
    elif "image" not in project_data:
        if message.photo:
            # Сохраняем изображение
            file_id = message.photo[-1].file_id
            file = await bot.get_file(file_id)
            image_url = file.file_path
            project_data["image"] = image_url
            await bot.send_message(chat_id, "Отправьте ссылку на ваш проект.")
        else:
            await bot.send_message(
                chat_id,
                "Извините, я не могу обработать это изображение. Пожалуйста, отправьте другое.",
            )
    # Запрашиваем ссылку на проект
    elif "link" not in project_data:
        project_data["link"] = message.text
        # Создаем экземпляр модели и сохраняем в базе данных
        project = await sync_to_async(
            Project.objects.create)(
            title=project_data["title"],
            description=project_data["description"],
            image=project_data["image"],
            link=project_data["link"],
        )
        # Очищаем словарь project_data
        project_data.clear()
        await bot.send_message(chat_id, "Проект успешно создан!")
    else:
        await bot.send_message(chat_id, "Что-то пошло не так. Попробуйте еще раз.")


# Запускаем бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
