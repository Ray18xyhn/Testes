import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    counter = ft.Text("0", size=50, data=0, color="WHIT", weight=ft.FontWeight.BOLD)
    page.bgcolor = "WHITE"

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
                bgcolor='BLUE',
                border_radius=13,
                shadow=ft.BoxShadow(
                    color='BLACK54',
                    blur_radius=14,
                    offset=ft.Offset(0, 8)
                    )
            ),
            height=600,
            width=400,
        ),
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
