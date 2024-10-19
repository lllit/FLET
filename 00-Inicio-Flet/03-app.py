import flet as ft

def main(page: ft.Page):
    page.title = "Adesivos"
    page.bgcolor = ft.colors.BLUE_GREY_900
    note = ft.TextField(value="Mi primera nota", multiline=True)
    page.add(note)

ft.app(target=main)