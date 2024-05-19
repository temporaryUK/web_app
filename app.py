import asyncio
import flet as ft


async def main(page: ft.Page) -> None:
    page.title = 'Monsters and Mortals'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = '#141221'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {'MursGothic-WideDark': 'fonts/MursGothic-WideDark.ttf'}
    page.theme = ft.Theme(font_family='MursGothic-WideDark')
    image_to_use = ft.Image(src='/image/pngegg.png', fit=ft.ImageFit.CONTAIN,
                            animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE))
    name1 = ft.Text(value="Monster's", size=50, text_align="CENTER")
    name2 = ft.Text(value="and", size=50, text_align="CENTER")
    name3 = ft.Text(value="Mortals", size=50, text_align="CENTER")

    async def color_change(event: ft.ContainerTapEvent) -> None:
        asyncio.timeout(3)
        event.control.color = '#00FF00'
        page.update()

    tg_channel_button = ft.ElevatedButton(text="Tg Channel", width=150, on_click=color_change, url='https://google.com')
    tg_chat_button = ft.ElevatedButton(text="Tg Chat", width=150, on_click=color_change, url='https://google.com')
    discord_button = ft.ElevatedButton(text="Discord", width=150, on_click=color_change, url="https://discord.gg/WnbAhDNtJh")
    x_button = ft.ElevatedButton(text="X", width=150, on_click=color_change, url='https://google.com')

    button_row1 = ft.Row(controls=[tg_channel_button, tg_chat_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
    button_row2 = ft.Row(controls=[discord_button, x_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10)

    page.add(
        ft.Container(
            ft.Column(controls=[name1, name2, name3])
        ),
        ft.Container(
            image_to_use
        ),
        button_row1,
        button_row2,
    )

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
