from tkinter import *
from tkinter import messagebox  #mensajes emergentes
import sqlite3


########### FUNCIONES

def conexionDB():
    conexion=sqlite3.connect("Usuarios")
    cursor=conexion.cursor()

    try:
        cursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(100),
                COMENTARIOS VARCHAR (250)
            )
        ''')
        messagebox.showinfo("BBDD", "Base de datos creada con éxito.")
    except:
        messagebox.showwarning("¡Atención!","La Base de Datos ya existe.")


def salirApp():
    valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
    if valor=="yes":
        root.destroy()


def limpiarCampos():
    txtNom.set("")
    txtId.set("")
    txtApe.set("")
    txtPass.set("")
    txtDir.set("")
    txtArea.delete(1.0,END)

def crear():
    conexion=sqlite3.connect("Usuarios")
    cursor=conexion.cursor()
    try:
        #cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+txtNom.get()+"','"+txtApe.get()+"','"+txtPass.get()+"','"+txtDir.get()+"','"+txtArea.get("1.0",END)+"')")
        datos=txtNom.get(), txtPass.get(), txtApe.get(), txtDir.get(),txtArea.get("1.0", END)
        cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",datos)
        
        conexion.commit()

        messagebox.showinfo("BBDD","Registro insertado con éxito")
    except:
        messagebox.showwarning("Atención","Error al crear el registro")

def leer():
    txtArea.delete(1.0,END)
    conexion=sqlite3.connect("Usuarios")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + txtId.get())
    users=cursor.fetchall()
    if users:
        for user in users:
            txtId.set(user[0])
            txtNom.set(user[1])
            txtPass.set(user[2])
            txtApe.set(user[3])
            txtDir.set(user[4])
            
            txtArea.insert("1.0", user[5])
    else:        
        txtId.set("")
        txtNom.set("")
        txtPass.set("")
        txtApe.set("")
        txtDir.set("")
            
        txtArea.insert("1.0", "No se han encontrado usuarios con el id. introducido")
    conexion.commit()
    

def actualizar():
    conexion=sqlite3.connect("Usuarios")
    cursor=conexion.cursor()
    """cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" +txtNom.get()+
        "', PASSWORD='"+ txtPass.get()+
        "', APELLIDO='"+txtApe.get()+
        "', DIRECCION='"+txtDir.get()+
        "', COMENTARIOS='"+txtArea.get("1.0",END)+
        "'WHERE ID="+txtId.get())"""
    try:
        datos=txtNom.get(), txtPass.get(), txtApe.get(), txtDir.get(),txtArea.get("1.0", END)
        cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=?"+
        "WHERE ID="+txtId.get(),datos) 
        conexion.commit()

        messagebox.showinfo("BBDD","Registro actualizado con éxito")
    except:
        messagebox.showwarning("Atención","Error al actualizar el registro")

def eliminar():
    conexion=sqlite3.connect("Usuarios")
    cursor=conexion.cursor()
    try:
        cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+txtId.get())
        conexion.commit()

        messagebox.showinfo("BBDD","Registro eliminado con éxito")
    except:
        messagebox.showwarning("¡Atención!", "Error al eliminar el registro")


def info():
    messagebox.showinfo("Sobre mi...","I LOVE PYTHON...I LOVE DATABASES...I LOVE CODING...")

############

root=Tk()

#configuracion barra menu
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

dbMenu = Menu(barraMenu,tearoff=0)
dbMenu.add_command(label="Conectar", command=conexionDB)
dbMenu.add_command(label="Salir", command=salirApp)

borrarMenu = Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu = Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu = Menu(barraMenu,tearoff=0)
#ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...", command=info)

barraMenu.add_cascade(label="BBDD", menu=dbMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

####### frame comienzo de campos #####

frame1= Frame(root)
frame1.pack() # empaquetamos

txtId=StringVar()
txtNom=StringVar()
txtApe=StringVar()
txtPass=StringVar()
txtDir=StringVar()
### campos
campoId=Entry(frame1,textvariable=txtId)
campoId.grid(row=0,column=1,padx=10,pady=10) 
campoId.config(fg="red",justify="right")

campoNombre=Entry(frame1,textvariable=txtNom)
campoNombre.grid(row=1,column=1,padx=10,pady=10) 

campoPass=Entry(frame1,textvariable=txtPass)
campoPass.grid(row=2,column=1,padx=10,pady=10) 
campoPass.config(show="*")

campoApe=Entry(frame1,textvariable=txtApe)
campoApe.grid(row=3,column=1,padx=10,pady=10)

campoDir=Entry(frame1,textvariable=txtDir)
campoDir.grid(row=4,column=1,padx=10,pady=10)

txtArea = Text(frame1, width=16, height=5)
txtArea.grid(row=5, column=1, padx=10,pady=10)
scrollVert=Scrollbar(frame1,command=txtArea.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
txtArea.config(yscrollcommand=scrollVert.set)

#### labels
idLabel=Label(frame1, text="Id:")
idLabel.grid(row=0,column=0,sticky="e", padx=10, pady=10)

nomLabel=Label(frame1, text="Nombre:")
nomLabel.grid(row=1,column=0,sticky="e", padx=10, pady=10)

passLabel=Label(frame1, text="Password:")
passLabel.grid(row=2,column=0,sticky="e", padx=10, pady=10)

apeLabel=Label(frame1, text="Apellido:")
apeLabel.grid(row=3,column=0,sticky="e", padx=10, pady=10)

dirLabel=Label(frame1, text="Direccion:")
dirLabel.grid(row=4,column=0,sticky="e", padx=10, pady=10)

comentariosLabel=Label(frame1, text="Comentarios:")
comentariosLabel.grid(row=5,column=0,sticky="e", padx=10, pady=10)


####### frame botones

frame2=Frame(root)
frame2.pack()

#botones
bCrear=Button(frame2,text="Crear", command=crear)
bCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

bLeer=Button(frame2,text="Consultar", command=leer)
bLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

bActualizar=Button(frame2,text="Actualizar", command=actualizar)
bActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

bBorrar=Button(frame2,text="Borrar", command=eliminar)
bBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)

root.mainloop()









