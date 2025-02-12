Custom controls



------------------------------------------------------------------------------------
Styled controls
import flet as ft
class Button(ft.ElevatedButton):
    def __init__(self,text):
        super().__init__()
        self.bgcolor=ft.colors.ORANGE_300
        self.color=ft.colors.GREEN_800
        self.text=text

def main(page:ft.Page):
    def ok(e):
        print("OK")
    def cancel(e):
        print("CANCEL")



    page.add(Button(text="OK"),Button(text="Cancel"))


ft.app(target=main)

------------------------------------------------------------------------------------
Composite controls
import flet as ft
class Task(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(
            visible=False, icon=ft.icons.SAVE, on_click=self.save
        )
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
        ]

    def edit(self, e):
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()

def main(page: ft.Page):

    page.add(
        Task(text="Do laundry"),
        Task(text="Cook dinner"),
    )


ft.app(target=main)