import flet as ft

def app(page: ft.Page) -> None:

    # Page data
    page.title = "Pixiv GUI"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 700
    page.window_height = 700
    page.window_resizable = False

    id_field: ft.TextField = ft.TextField(label='id', 
                                          text_align=ft.TextAlign.LEFT,
                                          width=400)