import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.title = "App Filas y columnas"

    h_text = ft.Text("LINK", size=12,color=ft.colors.AMBER)
    h_text2 = ft.Text("POST", size=12,color=ft.colors.AMBER)
    h_text3 = ft.Text("HOME", size=12,color=ft.colors.AMBER)
    
    fila_textos = ft.Row(
                controls=[h_text,h_text2,h_text3],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=50
                )

    #TEXTO
    text = ft.Text("Aqui solo texto con estas caracteristicas: size=24,color=ft.colors.WHITE", size=24,color=ft.colors.WHITE)
    text2 = ft.Text("Aqui solo texto con estas caracteristicas: size=20,color=ft.colors.WHITE", size=20,color=ft.colors.WHITE)
    text3 = ft.Text("Aqui solo texto con estas caracteristicas: size=18,color=ft.colors.WHITE", size=18,color=ft.colors.WHITE)

    texto_columnas=[
        ft.Text("TEXT: caracteristicas: size=24,color=ft.colors.WHITE", size=24,color=ft.colors.WHITE),
        ft.Text("TEXT: caracteristicas: size=20,color=ft.colors.WHITE", size=20,color=ft.colors.WHITE),
        ft.Text("TEXT: caracteristicas: size=18,color=ft.colors.WHITE", size=18,color=ft.colors.WHITE)
    ]
    texto_columnas2=[
        ft.Text("TEXT: caracteristicas: size=24,color=ft.colors.WHITE", size=24,color=ft.colors.WHITE),
        ft.Text("TEXT: caracteristicas: size=20,color=ft.colors.WHITE", size=20,color=ft.colors.WHITE),
        ft.Text("TEXT: caracteristicas: size=18,color=ft.colors.WHITE", size=18,color=ft.colors.WHITE)
    ]


    columna_texto =ft.Column(
        controls=texto_columnas,
        alignment=ft.MainAxisAlignment.END
    )
    columna_texto2 =ft.Column(
        controls=texto_columnas2
    )
    
    
    # BOTONES
    buton = ft.FilledButton(text="Soundcloud",
                            url="https://soundcloud.com/lllit_3/")
    buton2 = ft.FilledButton(text="Boton 2")
    buton3 = ft.FilledButton(text="Boton 3")

    fila_buton = ft.Row(
                controls=[buton,buton2,buton3],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=50
                )
    fila_colums = ft.Row(
        controls=[columna_texto,columna_texto2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )
    
    
    page.add(fila_textos,columna_texto,fila_buton,fila_colums)








ft.app(target=main)