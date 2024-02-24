from datetime import datetime

from flask import Flask
from sqlalchemy import and_, or_
from alchemyClasses import db
#from cryptoUtils.CryptoUtils import cipher
from modelos.usuarios import Usuario
from modelos.peliculas import Pelicula
from modelos.rentar import Rentar


def pedir_numero():
    entrada = -1
    while entrada == -1:
        try:
            entrada = int(input())
        except(ValueError):
            print("Lo ingresado no es un numero entero, ingresa el numero nuevamente.\n")
            entrada = -1
    return entrada
def imprimir_menu_principal():
    print("1. Ver los registros de una tabla.")
    print("2. Filtrar los registros de una tabla por ID.")
    print("3. Modificar el nombre de un usuario o pelicula, o modificar la fecha de renta de una pelicula.")
    print("4. ELiminar un registro por ID.")
    print("5. ELiminar todos los registros de una tabla")
    print("6. Salir\n")
    print("¿Que deseas hacer? (ingresa el numero)\n")
    entrada = pedir_numero()
    return entrada

def imprimir_eleccion_tablas():
    print("Ingresa el número de la tabla para hacer la operacion:")
    print("1.Usuarios")
    print("2.Peliculas")
    print("3.Rentar")
    entrada = pedir_numero()
    return entrada



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

def ver_registros_tabla(tabla):
    try:
        # Realiza la consulta para obtener todos los registros de la tabla especificada
        registros = tabla.query.all()

        # Imprime los registros
        for registro in registros:
            print(registro)

    except Exception as e:
        print("Error al consultar la base de datos:", e)

def filtra_usuario(id):
    registro = Usuario.query.filter(Usuario.idUsuario == id).first()
    # Si se encontró el registro, imprímelo
    if registro:
        print(registro)
    else:
        print("No se encontró ningún registro con el ID proporcionado.")

def filtra_pelicula(id):
    registro = Pelicula.query.filter(Pelicula.idPelicula == id).first()
    # Si se encontró el registro, imprímelo
    if registro:
        print(registro)
    else:
        print("No se encontró ningún registro con el ID proporcionado.")

def filtra_renta(id):
    registro = Rentar.query.filter(Rentar.idRentar == id).first()
    # Si se encontró el registro, imprímelo
    if registro:
        print(registro)
    else:
        print("No se encontró ningún registro con el ID proporcionado.")

def actualiza_nombre_usuario(id_usuario, nuevo_nombre):
    usuario = Usuario.query.filter_by(idUsuario=id_usuario).first()

    # Si se encontró el usuario, actualiza su nombre y confirma los cambios
    if usuario:
        usuario.nombre = nuevo_nombre
        db.session.commit()
        print("Nombre del usuario actualizado correctamente.")
    else:
        print("No se encontró ningún usuario con el ID proporcionado.")

def actualiza_nombre_pelicula(id_pelicula, nuevo_nombre):
    pelicula = Pelicula.query.filter_by(idPelicula=id_pelicula).first()

    # Si se encontró, actualiza su nombre y confirma los cambios
    if pelicula:
        pelicula.nombre = nuevo_nombre
        db.session.commit()
        print("Nombre actualizado correctamente.")
    else:
        print("No se encontró registro con el ID proporcionado.")

def actualizar_fecha_renta(id_renta, nueva_fecha):
    # Busca la renta por su ID
    renta = Rentar.query.filter_by(idRentar=id_renta).first()

    # Si se encontró la renta, actualiza su fecha y confirma los cambios
    if renta:
        renta.fecha_renta = nueva_fecha
        db.session.commit()
        print("Fecha de la renta actualizada correctamente.")
    else:
        print("No se encontró ninguna renta con el ID proporcionado.")

def eliminar_usuario_por_id(id_registro):
    # Busca el registro por su ID
    registro = Usuario.query.filter_by(idUsuario=id_registro).first()

    # Si se encontró el registro, elimínalo y confirma los cambios
    if registro:
        db.session.delete(registro)
        db.session.commit()
        print("Registro eliminado correctamente.")
    else:
        print("No se encontró ningún registro con el ID proporcionado.")

def eliminar_pelicula_por_id(id_registro):
    # Busca el registro por su ID
    registro = Pelicula.query.filter_by(idPelicula=id_registro).first()

    # Si se encontró el registro, elimínalo y confirma los cambios
    if registro:
        db.session.delete(registro)
        db.session.commit()
        print("Registro eliminado correctamente.")
    else:
        print("No se encontró ningún registro con el ID proporcionado.")

def eliminar_renta_por_id(id_registro):
    # Busca el registro por su ID
    registro = Rentar.query.filter_by(idRentar=id_registro).first()

    # Si se encontró el registro, elimínalo y confirma los cambios
    if registro:
        db.session.delete(registro)
        db.session.commit()
        print("Registro eliminado correctamente.")
    else:
        print("No se encontró ningún registro con el ID proporcionado.")

def eliminar_todo_de_tabla(tabla):
    try:
        # Consulta todos los registros de la tabla
        registros = tabla.query.all()

        # Elimina cada registro de la tabla
        for registro in registros:
            # Si la tabla es Usuario, también eliminamos las rentas asociadas
            if tabla == Usuario or tabla == Pelicula:
                for renta in registro.rentas:
                    db.session.delete(renta)
            db.session.delete(registro)

        # Confirma los cambios
        db.session.commit()
        print("Todos los registros de la tabla han sido eliminados correctamente.")

    except Exception as e:
        # Revierte los cambios en caso de error
        db.session.rollback()
        print("Error al eliminar los registros de la tabla:", e)

    except Exception as e:
        print("Error al eliminar los registros de la tabla:", e)
if __name__ == '__main__':
    print("***BIENVENIDO***\n")
    with app.app_context():
        while(True):
            usuario = imprimir_menu_principal()
            if(usuario == 1):
                eleccion = imprimir_eleccion_tablas()
                if(eleccion == 1):
                    ver_registros_tabla(Usuario)
                elif(eleccion == 2):
                    ver_registros_tabla(Pelicula)
                elif(eleccion == 3):
                    ver_registros_tabla(Rentar)
                else:
                    print("Esa no es una opcion")
            elif(usuario == 2):
                eleccion = imprimir_eleccion_tablas()
                id = input("Ingresa el ID a buscar: ")
                if (eleccion == 1):
                    filtra_usuario(id)
                elif (eleccion == 2):
                    filtra_pelicula(id)
                elif (eleccion == 3):
                    filtra_renta(id)
                else:
                    print("Esa no es una opcion")
            elif (usuario == 3):
                eleccion = imprimir_eleccion_tablas()
                id = input("Ingresa el ID del registro a actualizar: ")
                nuevo = input("Ingresa el nuevo valor: ")
                if (eleccion == 1):
                    actualiza_nombre_usuario(id,nuevo)
                elif (eleccion == 2):
                    actualiza_nombre_pelicula(id,nuevo)
                elif (eleccion == 3):
                    actualizar_fecha_renta(id,nuevo)
                else:
                    print("Esa no es una opcion")
            elif (usuario == 4):
                eleccion = imprimir_eleccion_tablas()
                id = input("Ingresa el id del registro a eliminar: ")
                if (eleccion == 1):
                    eliminar_usuario_por_id(id)
                elif (eleccion == 2):
                    eliminar_pelicula_por_id(id)
                elif (eleccion == 3):
                    eliminar_renta_por_id(id)
                else:
                    print("Esa no es una opcion")
            elif (usuario == 5):
                eleccion = imprimir_eleccion_tablas()
                if (eleccion == 1):
                    eliminar_todo_de_tabla(Usuario)
                elif (eleccion == 2):
                    eliminar_todo_de_tabla(Pelicula)
                elif (eleccion == 3):
                    eliminar_todo_de_tabla(Rentar)
                else:
                    print("Esa no es una opcion")

            elif (usuario == 6):
                break
            else:
                print("Esa no es una opcion")