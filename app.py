import flet as ft

def app(page: ft.Page) -> None:

    # Page data
    page.title = "Pixiv GUI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 700
    page.window_height = 700
    page.window_resizable = False

    # widgets
    selection: ft.Dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Artwork"),
            ft.dropdown.Option("Novel"),])
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
        if selection.value == "Novel":
            selection.value = "Novel"
            page.update()
            download_novel(event=event)
        else:
            selection.value = "Artwork"
            page.update()
            download_artwork(event=event)
    
    
    def download_artwork(event: ft.ControlEvent) -> None:
        print(f"Printing artwork...\nid: {id_field.value}")

        id_field.value = ""
        download_button.disabled = True
        page.update()
    

    def download_novel(event: ft.ControlEvent) -> None:
        print(f"Print novel...\nid: {id_field.value}")

        id_field.value = ""
        download_button.disabled = True
        page.update()


    id_field.on_change = id_validation
    download_button.on_click = download

    # Page Layout
    page.add(
        ft.Row(
            controls=[
                selection, id_field, download_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == '__main__':
    ft.app(target=app)