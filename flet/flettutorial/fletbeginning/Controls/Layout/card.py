import flet as ft


class buttonok(ft.TextButton):
    def __init__(self,text):
        super().__init__()
        self.text=text

def main(page):
    page.title = "Card Example"
    page.window.width=500
    page.window.resizable=False

    page.add(

        ft.Row(
            [
            ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Tilshunos"),
                            subtitle=ft.Text("M1nor vs Green battle!!!!!")
                        ),
                        ft.Row(
                            [buttonok("Buy"), buttonok("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        ),

        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Tilshunos"),
                            subtitle=ft.Text("M1nor vs Green battle!!!!!")
                        ),
                        ft.Row(
                            [buttonok("Buy"), buttonok("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        ),


        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Tilshunos"),
                            subtitle=ft.Text("M1nor vs Green battle!!!!!")
                        ),
                        ft.Row(
                            [buttonok("Buy"), buttonok("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        ),

        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Tilshunos"),
                            subtitle=ft.Text("M1nor vs Green battle!!!!!")
                        ),
                        ft.Row(
                            [buttonok("Buy"), buttonok("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        ),

            ])
        
    )


ft.app(target=main)
