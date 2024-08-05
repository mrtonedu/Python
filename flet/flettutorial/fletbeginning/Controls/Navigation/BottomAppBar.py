import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = page.vertical_alignment = "center"
    page.add(ft.Text("Body!"))

    page.appbar = ft.AppBar(
        title=ft.Text("Bottom AppBar Demo"),
        center_title=True,
        bgcolor=ft.colors.GREEN_300,
        automatically_imply_leading=True,
    )

    page.bottom_appbar=ft.BottomAppBar(
        bgcolor=ft.colors.GREEN_300,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
        controls=[
            ft.IconButton(icon=ft.icons.MENU,icon_color=ft.colors.WHITE),
            ft.Container(expand=True),
            ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
            
        ]
        )
    )
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    page.update()

ft.app(target=main)
