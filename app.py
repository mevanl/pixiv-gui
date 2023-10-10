import flet as ft

def app(page: ft.Page) -> None:

    # Page data
    page.title = "Pixiv GUI"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 700
    page.window_height = 700
    page.window_resizable = False

    # widgets
    id_field: ft.TextField = ft.TextField(label='id', 
                                          text_align=ft.TextAlign.LEFT,
                                          width=400)
    download_button: ft.ElevatedButton = ft.ElevatedButton(text='Download',
                                                           width=200,
                                                           disabled=True)
    
    # functions
    def id_validation(event: ft.ControlEvent) -> None:
        if (id_field.value and id_field.value.isnumeric()):
            download_button.disabled = False
            
        else:
            download_button.disabled = True

        page.update()

    
    def download(event: ft.ControlEvent) -> None:
        print(f"Printing...\nid: {id_field.value}")

        id_field.value = ""
        download_button.disabled = True
        page.update()


    id_field.on_change = id_validation
    download_button.on_click = download

    # Page Layout
    page.add(
        ft.Row(
            controls=[
                id_field, download_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == '__main__':
    ft.app(target=app)