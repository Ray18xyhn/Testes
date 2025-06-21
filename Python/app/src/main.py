import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0, color=ft.colors.BLACK)
    page.bgcolor = ft.colors.RED

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            height=100,
            width=100
        )
    )


ft.app(main)
