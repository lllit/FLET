import flet as ft
import pyodbc


SERVER = 'L-L-L\\SQLEXPRESS'  # Doble barra para escapar la barra invertida
DATABASE = 'usuariosFlet'

try:
    # Connection string con Trusted_Connection
    connectionString = f"DRIVER={{ODBC Driver 18 for SQL Server}};Server={SERVER};Database={DATABASE};Trusted_Connection=yes;TrustServerCertificate=yes;"

    # Intentar la conexión
    conn = pyodbc.connect(connectionString)
    

except pyodbc.Error as e:
    print("Error al conectar:", e)







def main(page: ft.Page):
    page.title = "FLET __ SQL SERVER"
    page.padding=20
    page.bgcolor = ft.colors.BLUE_GREY_900
    #page.theme_mode = "light"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Flet + SQL SERVER", size=30)  


    #
    nametxt = ft.TextField(label="name")
    apellidotxt = ft.TextField(label="apellido")
    agetxt = ft.TextField(label="age")

    #Crear edit input
    edit_nametxt = ft.TextField(label="name")
    edit_apellidotxt = ft.TextField(label="apellido")
    edit_agetxt = ft.TextField(label="age")
    edit_id = ft.Text()

    mydt = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Apellido")),
            ft.DataColumn(ft.Text("Edad")),
            ft.DataColumn(ft.Text("Fecha")),
            ft.DataColumn(ft.Text("Accción")),
        ],
        rows=[]
    )

    def deletebtn(e):
        print(f"select {e.control.data['id']}")
        try:
            query= "delete from usuario where id = ?"
            val = (e.control.data['id'])
            cursor = conn.cursor()
            cursor.execute(query,val)
            cursor.commit()
            print("eliminado")
            cursor.close()
            
            mydt.rows.clear()
            load_data()

            page.snack_bar = ft.SnackBar(
                ft.Text("Eliminado con exito", size=30),
                bgcolor="red"
            )
            page.snack_bar.open = True

            page.update()
            
        except pyodbc.Error as e:
            print("Error eliminar", e)
            
    

    def savedata(e):
        try:
            query = "update usuario set nombre = ?, apellido = ?, edad = ? where id = ?"
            val = (edit_nametxt.value, edit_apellidotxt.value, edit_agetxt.value, edit_id.value)
            
            cursor = conn.cursor()
            cursor.execute(query,val)
            
            cursor.commit()
            print("Edicion exitosa")
            cursor.close()
            dialog.open = False
            page.update()

            edit_nametxt.value = ""
            edit_apellidotxt.value = ""
            edit_agetxt.value = ""
            edit_id.value = ""


            mydt.rows.clear()
            load_data()

            page.snack_bar = ft.SnackBar(
                ft.Text("Editado con exito", size=30),
                bgcolor="green"
            )
            page.snack_bar.open = True

            
            page.update()
            
        except pyodbc.Error as e:
            print("Error editar ", e)
    
    # creando dialog boton 
    dialog = ft.AlertDialog(
        title=ft.Text("Editar datos"),
        content= ft.Column([
            edit_nametxt,
            edit_apellidotxt,
            edit_agetxt
        ]),
        actions=[
            ft.TextButton("Save",
                        on_click=savedata)
        ]
    )
    
    def editbtn(e):
        edit_nametxt.value = e.control.data['nombre']
        edit_apellidotxt.value = e.control.data['apellido']
        edit_agetxt.value = e.control.data['edad']

        edit_id.value = e.control.data['id']
        
        page.dialog = dialog
        dialog.open = True
        page.update()
    
    def load_data():
        SQL_QUERY = "SELECT * FROM usuario"

        cursor = conn.cursor()
        cursor.execute(SQL_QUERY)
        result = cursor.fetchall()

        #enviar la data a un diccionario
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns,row)) for row in result]

        # bucle y enviar
        for row in rows:
            fecha_formateada = row['FechaRegistro'].strftime('%d/%m/%Y %H:%M')  # Formato de la fecha
            mydt.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(row['id'])
                        ),
                        ft.DataCell(
                            ft.Text(row['nombre'])
                        ),
                        ft.DataCell(
                            ft.Text(row['apellido'])
                        ),
                        ft.DataCell(
                            ft.Text(row['edad'])
                        ),
                        ft.DataCell(
                            ft.Text(fecha_formateada)
                        ),
                        ft.DataCell(
                            ft.Row([
                                ft.IconButton(ft.icons.DELETE_OUTLINE,
                                            icon_color="red", 
                                            data=row,
                                            on_click=deletebtn),
                                ft.IconButton(ft.icons.CREATE_OUTLINED, 
                                            icon_color="red", 
                                            data=row,
                                            on_click=editbtn),
                            ])
                        ),
                    ]
                )
            )
        page.update()

    load_data()
        
    
    def addtobd(e):
        try:
            query="insert into usuario(nombre, apellido, edad) values (?,?,?);"
            val = (nametxt.value,apellidotxt.value,agetxt.value)
            cursor = conn.cursor()
            cursor.execute(query,val)
            conn.commit()
            print(cursor.rowcount, "Registro insertado correctamente.")
            mydt.rows.clear()
            load_data()

            page.snack_bar = ft.SnackBar(
                ft.Text("Datos guardados exitosamente", size=30),
                bgcolor="green"
            )
            page.snack_bar.open = True

            page.update()
        
        except pyodbc.Error as e:
            print("Error agregar", e)
            
        nametxt.value =""
        apellidotxt.value =""
        agetxt.value =""
        page.update()

    
    colum_text = ft.Column([
        nametxt,
        apellidotxt,
        agetxt,
        ft.ElevatedButton("Agregar", on_click=addtobd),
        mydt
    ])


    
    page.add(titulo,colum_text)

ft.app(target=main)