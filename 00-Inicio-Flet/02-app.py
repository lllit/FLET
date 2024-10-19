import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.title = "Lista de tarea"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Mi lista de tareas",
                    size=30,
                    weight=ft.FontWeight.BOLD)

    def agregar_tarea(e):
        if campo_tarea.value:
            tarea = ft.ListTile(
                title=ft.Text(campo_tarea.value),
                leading=ft.Checkbox(on_change=seleccionar_tarea)
            )
            tareas.append(tarea)
            campo_tarea.value = ""
            actualizar_lista()

    def seleccionar_tarea(e):
        selecionadas = [t.title.value for t in tareas if t.leading.value]
        tareas_seleccionadas.value = "Tareas seleccionadas: "+ ", ".join(selecionadas)
        page.update()

    def actualizar_lista():
        lista_tarea.controls.clear()
        lista_tarea.controls.extend(tareas)
        page.update()
    
    campo_tarea= ft.TextField(hint_text="Escribe una tarea")
    boton_agregar = ft.FilledButton(text="Agregar tarea", on_click=agregar_tarea)

    lista_tarea = ft.ListView(expand=1,spacing=3)
    
    tareas = []

    tareas_seleccionadas = ft.Text("",size=15,weight=ft.FontWeight.NORMAL)

    page.add(titulo,campo_tarea,boton_agregar,lista_tarea,tareas_seleccionadas)

ft.app(target=main)