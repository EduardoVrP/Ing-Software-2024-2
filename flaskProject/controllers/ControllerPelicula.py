from flask import Blueprint, request, render_template, flash, url_for,redirect
from alchemyClasses import db
from alchemyClasses.pelicula import Pelicula
pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/')
def menu_pelicula():
    return render_template('pelicula.html')

@pelicula_blueprint.route('/ver_peliculas')
def ver_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('ver_peliculas.html', peliculas=peliculas)

@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        genero = request.form.get('genero')
        duracion = request.form.get('duracion')
        inventario = request.form.get('inventario')

        # Verifica si el nombre ya existe en la base de datos
        if Pelicula.query.filter_by(nombre=nombre).first():
            flash('El nombre de la pelicula ya está registrado.', 'error')
            return redirect(url_for('pelicula.agregar_pelicula'))

        # Si la pelicula no existe, crea una nueva pelicula
        nueva_pelicula = Pelicula(
            nombre=nombre,
            duracion=duracion,
            genero=genero,
            inventario=inventario,
        )
        db.session.add(nueva_pelicula)
        db.session.commit()
        flash('Pelicula agregada exitosamente.', 'success')
        return redirect(url_for('pelicula.agregar_pelicula'))

    return render_template('agregar_pelicula.html')


@pelicula_blueprint.route('/solicitar_id_pelicula')
def solicitar_id_pelicula():
    return render_template('solicitar_id_pelicula.html')

@pelicula_blueprint.route('/actualizar_pelicula', methods=['POST'])
def actualizar_pelicula():
    pelicula_id = request.form.get('pelicula_id')
    pelicula = Pelicula.query.get(pelicula_id)
    if pelicula:
        return render_template('actualizar_pelicula.html', pelicula_id=pelicula_id, pelicula=pelicula)
    else:
        flash('No se encontró ninguna pelicula con ese ID.', 'error')
        return redirect(url_for('pelicula.solicitar_id_pelicula'))

@pelicula_blueprint.route('/actualizar_datos_pelicula', methods=['POST'])
def actualizar_datos_pelicula():
    pelicula_id = request.form.get('pelicula_id')
    pelicula = Pelicula.query.get(pelicula_id)
    if pelicula:
        pelicula.nombre = request.form.get('nombre')
        pelicula.genero = request.form.get('genero')
        pelicula.duracion = request.form.get('duracion')
        pelicula.inventario = request.form.get('inventario')
        db.session.commit()
        flash('Datos de la pelicula actualizados correctamente.', 'success')
        return redirect(url_for('pelicula.menu_pelicula'))
    else:
        flash('No se encontró ninguna pelicula con ese ID.', 'error')
        return redirect(url_for('pelicula.solicitar_id_pelicula'))


@pelicula_blueprint.route('/borrar_pelicula', methods=['POST'])
def borrar_pelicula():
    pelicula_id = request.form.get('pelicula_id')
    pelicula = Pelicula.query.get(pelicula_id)

    if pelicula:
        # Verificar si la pelicula está involucrada en alguna renta
        if pelicula.rentas:
            flash('No se puede borrar esta pelicula porque está involucrada en rentas activas.', 'error')
        else:
            db.session.delete(pelicula)
            db.session.commit()
            flash('Pelicula borrado correctamente.', 'success')
    else:
        flash('No se encontró ninguna pelicula con ese ID.', 'error')

    return redirect(url_for('pelicula.menu_pelicula'))