from datetime import datetime, timedelta
from flask import Blueprint, request, render_template, flash, url_for,redirect
from alchemyClasses import db
from alchemyClasses.rentar import Rentar
rentar_blueprint = Blueprint('rentar', __name__, url_prefix='/rentar')

@rentar_blueprint.route('/')
def menu_rentar():
    return render_template('rentar.html')

@rentar_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'POST':
        # Obtener datos del formulario
        id_usuario = request.form.get('usuario_id')
        id_pelicula = request.form.get('pelicula_id')

        # Validar que los campos no estén vacíos
        if not id_usuario or not id_pelicula:
            flash('Por favor, complete todos los campos.', 'error')
            return redirect(url_for('rentar.agregar_renta'))

        # Obtener la fecha y hora actual
        fecha_actual = datetime.now()

        # Crear una nueva instancia de Rentar con los datos proporcionados
        nueva_renta = Rentar(
            idUsuario=id_usuario,
            idPelicula=id_pelicula,
            fecha_renta=fecha_actual
        )

        # Agregar la nueva renta a la sesión de la base de datos
        db.session.add(nueva_renta)

        # Confirmar los cambios en la base de datos
        db.session.commit()

        flash('Se ha agregado la renta exitosamente.', 'success')
        return redirect(url_for('rentar.agregar_renta'))

    return render_template('agregar_renta.html')

@rentar_blueprint.route('/ver_rentas')
def ver_rentas():
    # Obtener todas las rentas
    rentas = Rentar.query.all()

    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()

    # Lista para almacenar las rentas vencidas
    rentas_vencidas = []

    # Verificar si la renta está vencida y agregar a la lista rentas_vencidas
    for renta in rentas:
        fecha_vencimiento = renta.fecha_renta + timedelta(days=renta.dias_de_renta)
        if fecha_vencimiento < fecha_actual:
            rentas_vencidas.append(renta)

    return render_template('ver_rentas.html', rentas=rentas, rentas_vencidas=rentas_vencidas)

@rentar_blueprint.route('/solicitar_id_renta')
def solicitar_id_renta():
    return render_template('solicitar_id_renta.html')

@rentar_blueprint.route('/actualizar_renta', methods=['POST'])
def actualizar_renta():
    renta_id = request.form.get('rentar_id')
    renta = Rentar.query.get(renta_id)
    if renta:
        return render_template('actualizar_renta.html', renta_id=renta_id, renta=renta)
    else:
        flash('No se encontró ninguna renta con ese ID.', 'error')
        return redirect(url_for('rentar.solicitar_id_renta'))

@rentar_blueprint.route('/actualizar_datos_renta', methods=['POST'])
def actualizar_datos_renta():
    renta_id = request.form.get('renta_id')
    renta = Rentar.query.get(renta_id)
    if renta:
        renta.estatus = request.form.get('estatus')
        db.session.commit()
        flash('Datos de la renta actualizados correctamente.', 'success')
        return redirect(url_for('rentar.menu_rentar'))
    else:
        flash('No se encontró ninguna renta con ese ID.', 'error')
        return redirect(url_for('rentar.solicitar_id_renta'))


