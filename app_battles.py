import asyncio
import random
import flet as ft


#настройка шрифта, названия, цвет.
async def main(page: ft.Page) -> None:
    page.title = "Monsters and Mortals"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = '#141221'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {'MursGothic-WideDark': 'fonts/MursGothic-WideDark.ttf'}
    page.theme = ft.Theme(font_family='MursGothic-WideDark')


    score = ft.Text(value='100', size=100, data=100)
    score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN))
    image_to_use = ft.Image(src='/image/pngegg.png', fit=ft.ImageFit.CONTAIN, animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE))
    image_boss = ft.Image(src='/image/peach.png', fit=ft.ImageFit.CONTAIN, animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE))
    progress_bar = ft.ProgressBar(value=1, width=page.width - 100, bar_height=20, color='#ff0000', bgcolor='#bc544b')

    async def score_up(event: ft.ContainerTapEvent) -> None:
        tap_strength = 1
        score.data -= tap_strength
        score.value = str(score.data)

        image_to_use.scale = 0.95

        # Генерируем случайные координаты для позиционирования текста score_counter можно сделать под себя
        # score_counter.right = random.randint(event.control.right - 100 if event.control.right else page.width - 100, event.control.right if event.control.right else page.width)
        # score_counter.right = random.randint(
        #     int(event.control.right - 100) if event.control.right else int(page.width - 100),
        #     int(event.control.right) if event.control.right else int(page.width))
        #
        # score_counter.left = random.randint(event.control.left if event.control.left else 0, event.control.left + 100 if event.control.left else 100)
        # score_counter.top = random.randint(event.control.top - 50 if event.control.top else 0, event.control.top + 50 if event.control.top else 50)
        # score_counter.bottom = random.randint(event.control.bottom - 50 if event.control.bottom else 0, event.control.bottom + 50 if event.control.bottom else 50)

        progress_bar.value -= (tap_strength/100)
        print(progress_bar.value)
        if score.data < 1:
            page.snack_bar = ft.SnackBar(content=ft.Text(value="DEFEAT THE BOSS!", size=20, color='#ff8b1f',text_align=ft.TextAlign.CENTER), bgcolor='#bc544b')
            score.data = 500
            score.value = '500'
            # hp_boss = 500

            page.snack_bar.open = True
            progress_bar.value = 1

            image_to_use.src = "/image/apple.png"

        score_counter.opacity = 100
        score_counter.value = f'-1 🧡'

        page.update()
        await asyncio.sleep(0.1)
        image_to_use.scale = 1
        score_counter.opacity = 0
        page.update()

    ref_button = ft.ElevatedButton(text="Ref", on_click=score_up)
    task_button = ft.ElevatedButton(text="Task", on_click=score_up)
    boost_button = ft.ElevatedButton(text="Boost", on_click=score_up)

    page.add(
        score,
        ft.Container(
            content=ft.Stack(controls=[image_to_use, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30),
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        ),
        ft.Row(
            controls=[ref_button, task_button, boost_button],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=8000)