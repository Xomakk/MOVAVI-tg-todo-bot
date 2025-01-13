from telebot import types

from todo.models import Task


def make_buttons_for_tasks_list(tasks: list[Task]):
    kb = types.InlineKeyboardMarkup(row_width=1)
    for task in tasks:
        btn = types.InlineKeyboardButton(
            text=task.title, callback_data=f"task/{task.id}"
        )
        kb.add(btn)
    add_btn = types.InlineKeyboardButton(text="Добавить новую", callback_data="add")
    kb.add(add_btn)
    return kb


def make_buttons_for_task(task: Task):
    text = f"{task.title}\n\n"
    text += f"СТАТУС: {'ВЫПОЛНЕНО' if task.status else 'НЕ ВЫПОЛНЕНО'}"

    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton(
        text = 'ВЫПОЛНЕНО' if not task.status else 'НЕ ВЫПОЛНЕНО',
        callback_data=f"status/{task.id}"
    ))
    kb.add(types.InlineKeyboardButton(
        text = 'Изменить',
        callback_data=f"update/{task.id}"
    ))
    kb.add(types.InlineKeyboardButton(
        text = 'Удалить',
        callback_data=f"remove/{task.id}"
    ))
    kb.add(types.InlineKeyboardButton(
        text = '<- Назад',
        callback_data=f"back"
    ))
    return text, kb