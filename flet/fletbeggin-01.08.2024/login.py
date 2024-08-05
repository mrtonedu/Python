import flet as ft
import sqlite3

def main(page:ft.Page):
    page.title="Mr Ton App"
    page.theme_mode='dark'
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.window.width=350
    page.window.height=400
    page.window.resizable=False




    def register(e):
        db=sqlite3.connect("it.progres")
        cur=db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,login TEXT,pass TEXT)""")
        cur.execute(f"INSERT INTO users VALUES(NULL,'{user_login.value}','{user_pass.value}')")
        db.commit()
        db.close()
        user_pass.value=''
        user_login.value=''
        register_button.text='Добавить'
        page.update()

    def validate(e):
        if all([user_login.value,user_pass.value]):
            register_button.disabled=False
            auth_button.disabled=False
        else:
            register_button.disabled=True
            auth_button.disabled=True
        page.update()


    def authification(e):
        db = sqlite3.connect("it.progres")
        cur = db.cursor()
        cur.execute(f"SELECT * FROM users WHERE login='{user_login.value}' AND pass='{user_pass.value}'")
        if cur.fetchone() != None:

            user_pass.value = ''
            user_login.value = ''
            register_button.text = 'Авторизовать'
            if len(page.navigation_bar.destinations)==2:page.navigation_bar.destinations.append(ft.NavigationBarDestination(icon=ft.icons.BOOK,selected_icon=ft.icons.BOOKMARK , label="Личный кабинет"))



            page.update()
        else:
            page.snack_bar=ft.SnackBar(ft.Text("Неверна введенные данные!"))
            page.snack_bar.open=True
            page.update()

        db.commit()
        db.close()





    user_login=ft.TextField(label="Логин",width=200,on_change=validate)
    user_pass=ft.TextField(label="Пароль",width=200,on_change=validate)
    register_button=ft.OutlinedButton(text='Добавить',width=200,on_click=register,disabled=True)
    auth_button=ft.OutlinedButton(text='Авторизовать',width=200,on_click=authification,disabled=True)

    #USER CABINET
    user_list=ft.ListView(spacing=10,padding=20)


    #USER CABINET END




    pannel_register=ft.Row(
            [
                ft.Column(
                    [ft.Text("Регистрация"),
                    user_login,
                    user_pass,
                    register_button]
                )
            ],alignment=ft.MainAxisAlignment.CENTER
        )
    pannel_auth = ft.Row(
        [
            ft.Column(
                [ft.Text("Авторизация"),
                 user_login,
                 user_pass,
                 auth_button]
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )
    pannel_cabinet= ft.Row(
        [
            ft.Column(
                [ft.Text("Личный кабинет"),user_list]
            )
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    def navigate(e):
        index=(page.navigation_bar.selected_index)
        page.clean()
        if index==0:page.add(pannel_register)
        elif index==1:page.add(pannel_auth)
        elif index==2:
            user_list.controls.clear()
            db=sqlite3.connect("./it.progres")
            cur=db.cursor()
            cur.execute("SELECT * FROM users")
            res=cur.fetchall()
            print(res)
            if res!=None:
                for user in res:
                    user_list.controls.append(ft.Row([
                        ft.Text(f"{user[1]}"),
                        ft.Icon(ft.icons.VERIFIED_USER)
                    ]))

            db.commit()
            db.close()
            page.add(pannel_cabinet)


        page.update()
    page.navigation_bar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.LOGIN,label="Регистрация"),
            ft.NavigationBarDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label="Авторизовать")
        ],on_change=navigate
    )
    page.add(pannel_register)


ft.app(target=main)


