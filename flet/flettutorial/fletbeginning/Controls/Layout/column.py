# import flet as ft
# import math
# def main(page: ft.Page):

#     def item(coun):
#         items=[]
#         for i in range(1,coun+1):
#             items.append(
#                 ft.Container(
#                     content=ft.Text(value=str(i)),
#                     alignment=ft.alignment.center,
#                     width=50,
#                     height=50,
#                     bgcolor=ft.colors.AMBER,
#                     border_radius=ft.border_radius.all(5),
#                     )
#                 )
#         return items

#     def spacing_slider(e):
#         grade.value=f"Volume:{math.floor(float(gap_slider.value))}"
#         col.spacing=math.floor(float(gap_slider.value))
#         page.update()

#     gap_slider=ft.Slider(
#         min=0,
#         max=100,
#         value=0,
#         label="Label",
#         width=500,
#         on_change=spacing_slider
#         )
#     grade=ft.Text(f"Volume:{gap_slider.value}")
#     col=ft.Column(spacing=0,controls=item(3))
#     page.add(ft.Row([ft.Text("Spacing between items"),gap_slider,grade]),ft.Row([col]))

# ft.app(target=main)