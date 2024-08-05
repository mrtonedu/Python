import flet as ft
import requests

def main(page:ft.Page):
    page.title="Погоднаю программа"
    page.theme_mode="light"

    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    user_data=ft.TextField(label="Введите город",width=400)
    weather_data=ft.Text("")
    def get_info(e):

        city=user_data.value
        API="23d07c3ff544bdbf38934a44b42c157f"
        URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
        res=requests.get(URL).json()
        temp=res['main']['temp']
        weather_data.value="Погода: "+str(temp)
        page.update()


    def change_theme(e):
        #page.theme_mode=="light" if page.theme_mode=='dark' else "dark"
        if page.theme_mode=="dark":
            page.theme_mode=='light'
            page.update()
        else:
            page.theme_mode=='dark'
            page.update()

    page.add(
        ft.Row
        (
            [
                ft.IconButton(ft.icons.SUNNY,on_click=change_theme),
                ft.Text("Погоднаю программа")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text="Получить",on_click=get_info)],alignment=ft.MainAxisAlignment.CENTER)

    )

ft.app(target=main)
