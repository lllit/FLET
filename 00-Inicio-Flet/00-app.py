import flet as ft


def main(page: ft.Page):
    page.title = "Titulo APP"
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    text = ft.Text("APP")
    
    text2 = ft.Text("Subtexto")
    
    def cambiar_texto(e):
        text2.value = "Cambiando texto"
        page.update()

    button = ft.FilledButton(text="Cambiar texto", on_click=cambiar_texto)

    page.add(text,text2,button)

ft.app(target=main)