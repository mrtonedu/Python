import flet as ft


def main(page: ft.Page):

    
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar=ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.colors.GREEN_ACCENT,
        
        actions=[
                ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                ft.IconButton(ft.icons.FILTER_3_SHARP),
                ft.PopupMenuButton(items=[ft.PopupMenuItem(text="Item 1",checked=False,on_click=check_item_clicked),])                    
                ]
            
        
    )



    


ft.app(main)
