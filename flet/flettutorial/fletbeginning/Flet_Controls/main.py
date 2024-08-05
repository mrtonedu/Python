#Starting
# import flet as ft


# def main(page: ft.Page):
#     page.add(ft.SafeArea(ft.Text(value="Hello, Flet!",color='red')))


# ft.app(main)

#Flet controls
# import flet as ft

# def main(page: ft.Page):
#     t = ft.Text(value="Hello, world!", color="green")
#     page.controls.append(t)
#     page.update()

# ft.app(target=main)
#-------------------------------------------------------------------------------------
# import flet as ft
# import time
# def main(page:ft.Page):
#     t = ft.Text()
#     page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

#     for i in range(10):
#         t.value = f"Step {i}"
#         page.update()
#         time.sleep(1)

# ft.app(target=main)

#-------------------------------------------------------------------------------------
# import flet as ft
# def main(page:ft.Page):
#     page.add(
#     ft.Row(controls=[
#         ft.Text("A"),
#         ft.Text("B"),
#         ft.Text("C")
#     ]),
#     ft.Row(controls=[
#         ft.TextField(label="Your name"),
#         ft.ElevatedButton(text="Say my name!")
#     ])
#     )
#     page.update()

# ft.app(target=main)

#-------------------------------------------------------------------------------------
# import flet as ft
# import time

# def main(page: ft.Page):
#     for i in range(10):
#         page.controls.append(ft.Text(f"Line {i}"))
#         time.sleep(1)
#         if i > 4:
#              page.controls.pop(0)
#         page.update()
# ft.app(target=main)

#-------------------------------------------------------------------------------------

# import flet as ft

# def main(page:ft.Page):
#     clicked=ft.Text(f"Clicked!")
#     def button_clicked(e):
#         page.add(clicked)
#         page.update()

#     page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))
# ft.app(target=main)

#-------------------------------------------------------------------------------------

# import flet as ft 

# def main(page:ft.Page):
    
    
    
#     def add_clicked(e):
#         page.add(ft.Checkbox(label=new_task.value))
#         new_task.value=""
#         new_task.focus=""
#         page.update()

#     new_task=ft.TextField(hint_text="Whats needs to be done?",width=300)
#     add_btn=ft.ElevatedButton("Add",on_click=add_clicked)

#     page.add(ft.Row([new_task,add_btn]))




# ft.app(target=main)


#-------------------------------------------------------------------------------------
#EVENT HANDLERS

# import flet as ft 

# def main(page:ft.Page):
#     page.title="Counter"
#     page.vertical_alignment=ft.MainAxisAlignment.CENTER
#     page.bgcolor="#b3ff33"
   

#     def minus(e):
#         minuser=int(number.value)-1
#         number.value=minuser
#         number.update()

#     def plus(e):
#         minuser=int(number.value)+1
#         number.value=str(minuser)
#         number.update()

#     number=ft.TextField(value="0",width=50,text_align="center",bgcolor="#ffffc0",color="black")
#     ROW=ft.Row([
#             ft.IconButton(ft.icons.REMOVE,on_click=minus,bgcolor='#ffffc0'),
#             number,
#             ft.IconButton(ft.icons.ADD,on_click=plus,bgcolor="#ffffc0")
#         ],alignment=ft.MainAxisAlignment.CENTER
#     )    
#     page.add(ROW)

# ft.app(target=main)

#-------------------------------------------------------------------------------------
#Textbox
# import flet as ft

# def main(page):
#     def btn_click(e):
#         if not txt_name.value:
#             txt_name.error_text = "Please enter your name"
#             page.update()
#         else:
#             name = txt_name.value
#             page.clean()
#             page.add(ft.Text(f"Hello, {name}!"))

#     txt_name = ft.TextField(label="Your name")

#     page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

# ft.app(target=main)

#-------------------------------------------------------------------------------------
#Checkbox
# import flet as ft


# def main(page):
#     def checkbox_changed(e):
#         output_text.value = (
#             f"You have learned how to ski :  {todo_check.value}."
#         )
#         page.update()

#     output_text = ft.Text()
#     todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
#     page.add(todo_check, output_text)

# ft.app(target=main)


#-------------------------------------------------------------------------------------
#Dropdown
import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)

ft.app(target=main)