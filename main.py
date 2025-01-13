from telebot import TeleBot
from telebot import types

import constants
from database import create_tables
from todo.controllers import get_task_list, add_new_task, get_task

bot = TeleBot(constants.TOKEN)
create_tables()  # создаем БД и таблицы


@bot.message_handler(commands=["start"])
def handle_start(msg: types.Message):
    user_id = msg.from_user.id
    kb = get_task_list(user_id)
    bot.send_message(msg.chat.id, text="Ваши задачи:", reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def handle_signals(call: types.CallbackQuery):
    if call.data == "add":
        bot.send_message(call.message.chat.id, "Укажите суть задачи")
        bot.register_next_step_handler(call.message, handle_add)

    if "task" in call.data:
        id = int(call.data.split("/")[1])
        text, kb = get_task(id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=text,
            reply_markup=kb,
        )

    if call.data == "back":
        kb = get_task_list(call.from_user.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="Ваши задачи:",
            reply_markup=kb,
        )
    
    


def handle_add(msg: types.Message):
    text = msg.text
    user_id = msg.from_user.id
    add_new_task(user_id, text)

    kb = get_task_list(user_id)
    bot.send_message(msg.chat.id, text="Ваши задачи:", reply_markup=kb)


bot.polling(interval=1, non_stop=True)
