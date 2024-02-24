import pymysql.cursors
from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker()

def obtener_ids_usuarios():
    # Conexión a la base de datos
    connection = pymysql.connect(host='localhost',
                                 user='lab',
                                 password='Developer123!',
                                 database='lab_ing_software',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Consulta para obtener todos los IDs de usuarios
            sql = "SELECT idUsuario FROM usuarios"
            cursor.execute(sql)
            # Obtener resultados
            results = cursor.fetchall()
            # Extraer los IDs de los resultados y almacenarlos en una lista
            ids_usuarios = [result['idUsuario'] for result in results]
            return ids_usuarios
    finally:
        connection.close()

def obtener_ids_peliculas():
    # Conexión a la base de datos
    connection = pymysql.connect(host='localhost',
                                 user='lab',
                                 password='Developer123!',
                                 database='lab_ing_software',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Consulta para obtener todos los IDs de películas
            sql = "SELECT idPelicula FROM peliculas"
            cursor.execute(sql)
            # Obtener resultados
            results = cursor.fetchall()
            # Verificar si hay resultados antes de intentar acceder a ellos
            if results:
                # Extraer los IDs de los resultados y almacenarlos en una lista
                ids_peliculas = [result['idPelicula'] for result in results]
                return ids_peliculas
            else:
                # Si no hay resultados, devolver una lista vacía
                return []
    finally:
        connection.close()


# Función para insertar registros
def insertar_registros():
    # Conexión a la base de datos
    connection = pymysql.connect(host='localhost',
                                 user='lab',
                                 password='Developer123!',
                                 database='lab_ing_software',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Generar datos aleatorios
            nombre_usuario = fake.first_name()
            apPat_usuario = fake.last_name()
            apMat_usuario = fake.last_name()
            password_usuario = fake.password()
            email_usuario = fake.email()

            nombre_pelicula = fake.sentence(nb_words=4)
            genero_pelicula = random.choice(["Acción","Comedia","Drama","Ciencia ficción","Aventura","Terror","Romance","Animación","Suspense","Documental"])
            duracion_pelicula = random.randint(60, 240)
            inventario_pelicula = random.randint(1, 50)

            # Insertar un registro en la tabla usuarios
            sql = "INSERT INTO usuarios (nombre, apPat, apMat, password, email) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (nombre_usuario, apPat_usuario, apMat_usuario, password_usuario, email_usuario))
            connection.commit()

            # Insertar un registro en la tabla peliculas
            sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nombre_pelicula, genero_pelicula, duracion_pelicula, inventario_pelicula))
            connection.commit()

            # Obtener el ID
            ids_usuario = obtener_ids_usuarios()
            ids_peliculas = obtener_ids_peliculas()
            id_usuario = random.choice(ids_usuario)
            id_pelicula = random.choice(ids_peliculas)

            # Generar fecha de renta (entre hoy y 30 días atrás)
            fecha_renta = datetime.now() - timedelta(days=random.randint(0, 30))

            # Insertar un registro en la tabla rentar
            sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id_usuario, id_pelicula, fecha_renta, 5))
            connection.commit()

    finally:
        connection.close()

# Ejecutar la función para insertar registros
insertar_registros()


# Función para filtrar usuarios por apellido
def filtrar_usuarios_por_apellido(apellido_termina_con):
    # Conexión a la base de datos
    connection = pymysql.connect(host='localhost',
                                 user='lab',
                                 password='Developer123!',
                                 database='lab_ing_software',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Consulta SQL para filtrar usuarios por apellido
            sql = "SELECT * FROM usuarios WHERE apPat LIKE %s OR apMat LIKE %s"
            # Agregamos '%' al final de la cadena para encontrar coincidencias de cualquier longitud
            apellido_pattern = f'%{apellido_termina_con}'
            cursor.execute(sql, (apellido_pattern,apellido_pattern))
            result = cursor.fetchall()
            return result

    finally:
        connection.close()

# Ejemplo de uso
apellido_termina_con = input("Ingrese la cadena con la que desea filtrar los apellidos: ")
usuarios_filtrados = filtrar_usuarios_por_apellido(apellido_termina_con)

if usuarios_filtrados:
    print("Usuarios encontrados:")
    for usuario in usuarios_filtrados:
        print(usuario)
else:
    print("No se encontraron usuarios con ese criterio de búsqueda.")

def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero):
    # Conexión a la base de datos
    connection = pymysql.connect(host='localhost',
                                 user='lab',
                                 password='Developer123!',
                                 database='lab_ing_software',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Verificar si la película existe
            sql = "SELECT * FROM peliculas WHERE nombre = %s"
            cursor.execute(sql, (nombre_pelicula,))
            pelicula = cursor.fetchone()

            if pelicula:
                # La película existe, actualizar el género
                sql_update = "UPDATE peliculas SET genero = %s WHERE idPelicula = %s"
                cursor.execute(sql_update, (nuevo_genero, pelicula['idPelicula']))
                connection.commit()
                print(f"Se ha actualizado el género de la película '{nombre_pelicula}' a '{nuevo_genero}'.")
            else:
                print(f"No se encontró la película '{nombre_pelicula}'. No se realizó ninguna actualización.")

    finally:
        connection.close()

# Ejemplo de uso
nombre_pelicula = input("Ingrese el nombre de la película: ")
nuevo_genero = input("Ingrese el nuevo género para la película: ")

cambiar_genero_pelicula(nombre_pelicula, nuevo_genero)

def eliminar_rentas_antiguas():
    # Conexión a la base de datos
    connection = pymysql.connect(host='localhost',
                                 user='lab',
                                 password='Developer123!',
                                 database='lab_ing_software',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Calcular la fecha límite para eliminar rentas
            fecha_limite = datetime.now() - timedelta(days=3)

            # Eliminar rentas antiguas
            sql = "DELETE FROM rentar WHERE fecha_renta <= %s"
            cursor.execute(sql, (fecha_limite,))
            connection.commit()

            # Obtener el número de filas afectadas
            num_filas_afectadas = cursor.rowcount
            print(f"Se eliminaron {num_filas_afectadas} rentas antiguas.")

    finally:
        connection.close()

# Ejemplo de uso
eliminar_rentas_antiguas()

