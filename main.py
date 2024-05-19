# import flet as ft
# import time
#
#
# def main(page):
#     page.window_width, page.window_height = 390, 844
#     def add_clicked(e):
#         page.add(ft.Checkbox(label=new_task.value))
#         new_task.value = ""
#         new_task.focus()
#         new_task.update()
#
#     new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
#     page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
#
#     print(page.window_width, page.window_height)
#
# ft.app(target=main)

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.client.


API_TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)













