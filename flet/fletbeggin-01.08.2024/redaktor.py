import flet as ft

#GLOBAL
path=''
def main(page:ft.Page):
    page.title="Текстовый редактор"
    page.theme_mode="dark"
    page.window.width=300
    page.window.height=350
    page.window.resizable==False
    page.horizontal_alignment=ft.MainAxisAlignment.CENTER




    def picl_result(e:ft.FilePickerResultEvent):
        if not e.files:
            selected_file.value="Ничего не выбрано"
        else:
            selected_file.value=""
            global  path
            for el in e.files:
                path=el.path
            f=open(path,'r')
            text_field.value=f.read()

        page.update()


    def save_file(e):
        global path
        f=open(path,'w')
        f.write(text_field.value)
        f.close()

        text_field.value=''
        save_btn.text='Готова'
        page.update()

    save_btn=ft.FilledButton("Сахранить",on_click=save_file)

    pick_dialog=ft.FilePicker(on_result=picl_result)
    page.overlay.append(pick_dialog)
    selected_file=ft.Text()
    text_field=ft.TextField(label="Текс файла",width=180,multiline=True)

    page.add(
        ft.Row([ft.Text("Выбор файлов",size=25,weight=500)],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [
                ft.ElevatedButton("Выбор файлов",icon=ft.icons.UPLOAD_FILE,on_click=lambda _:pick_dialog.pick_files(allow_multiple=False))
            ]
        ),
        ft.Row([text_field]),
        ft.Row([save_btn]),
        ft.Row([selected_file])
    )

ft.app(target=main)