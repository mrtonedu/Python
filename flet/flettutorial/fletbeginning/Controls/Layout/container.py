# import flet as ft   
# def main(page:ft.Page):
# 	page.title="Container-clickable and not"
# 	page.vertical_alignment=ft.MainAxisAlignment.CENTER
# 	page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

# 	page.add(
# 		ft.Row(
# 			[
# 				ft.Container(
# 					content=ft.Text("Non clickable"),
# 					bgcolor=ft.colors.AMBER,
# 					margin=10,
# 					padding=10,
# 					width=150,
# 					height=150,
# 					border_radius=10,
# 					alignment=ft.alignment.center
# 					),
# 				ft.Container(
#                     content=ft.Text("Clickable without Ink"),
#                     margin=10,
#                     padding=10,
#                     alignment=ft.alignment.center,
#                     bgcolor=ft.colors.GREEN_200,
#                     width=150,
#                     height=150,
#                     border_radius=10,

#                     on_click=lambda e: print("Clickable without Ink clicked!")
#                     ),
# 				ft.Container(
#                     content=ft.Text("Clickable with Ink"),
#                     margin=10,
#                     padding=10,
#                     alignment=ft.alignment.center,
#                     bgcolor=ft.colors.CYAN_200,
#                     width=150,
#                     height=150,
#                     border_radius=10,
#                     ink=True,
#                     ink_color='red',
#                     on_click=lambda e: print("Clickable with Ink clicked!"),
#                 ),
#                 ft.Container(
#                     content=ft.Text("Clickable transparent with Ink"),
#                     margin=10,
#                     padding=10,
#                     alignment=ft.alignment.center,
#                     width=150,
#                     height=150,
#                     border_radius=10,
#                     ink=True,
#                     on_click=lambda e: print("Clickable transparent with Ink clicked!"),
#                 ),
# 			],alignment=ft.MainAxisAlignment.CENTER,
# 			)
# 		)

# ft.app(target=main)

#-------------------------------------------------------------------------------------------------------------
# import flet as ft

# def main(page: ft.Page):
#     # Yellow page theme with SYSTEM (default) mode
#     page.theme = ft.Theme(
#         color_scheme_seed=ft.colors.YELLOW,
#     )

#     page.add(
#         # Page theme
#         ft.Container(
#             content=ft.ElevatedButton("Page theme button"),
#             bgcolor=ft.colors.SURFACE_VARIANT,
#             padding=20,
#             width=300,
#         ),

#         # Inherited theme with primary color overridden
#         ft.Container(
#             theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.PINK)),
#             content=ft.ElevatedButton("Inherited theme button"),
#             bgcolor=ft.colors.SURFACE_VARIANT,
#             padding=20,
#             width=300,
#         ),
        
#         # Unique always DARK theme
#         ft.Container(
#             theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
#             theme_mode=ft.ThemeMode.DARK,
#             content=ft.ElevatedButton("Unique theme button"),
#             bgcolor=ft.colors.SURFACE_VARIANT,
#             padding=20,
#             width=300,
#         ),
#     )

# ft.app(main)

#------------------------------------------------------------------------------------------
# import flet as ft

# def main(page: ft.Page):
#     def on_hover(e):
#         e.control.bgcolor = "blue" if e.data == "true" else "red"
#         e.control.update()

#     page.add(
#         ft.Container(width=100, height=100, bgcolor="red", ink=False, on_hover=on_hover)
#     )

# ft.app(target=main)

#-------------------------------------------------------------------------------------------------------
import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def on_long_press(e):
        print("on long press")
        page.add(ft.Text("on_long_press triggered"))

    def on_click(e):
        print("on click")
        page.add(ft.Text("on_click triggered"))

    def on_tap_down(e: ft.ContainerTapEvent):
        print("on tap down", e.local_x, e.local_y)
        page.add(ft.Text("on_tap_down triggered"))

    c = ft.Container(
        bgcolor=ft.colors.RED,
        content=ft.Text("Test Long Press"),
        height=100,
        width=100,
        on_click=on_click,
        on_long_press=on_long_press,
        on_tap_down=on_tap_down,
    )
    
    page.add(c)

ft.app(target=main)