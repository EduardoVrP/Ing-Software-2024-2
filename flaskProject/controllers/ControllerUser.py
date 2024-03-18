from flask import Blueprint, request, render_template, flash, url_for,redirect
from alchemyClasses import db
from alchemyClasses.usuario import Usuario
usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/')
def menu_usuario():
    return render_template('usuario.html')

@usuario_blueprint.route('/ver_usuarios')
def ver_usuarios():
    usuarios = Usuario.query.all()
    return render_template('ver_usuarios.html', usuarios=usuarios)

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apPat = request.form.get('apPat')
        apMat = request.form.get('apMat')
        password = request.form.get('password')
        email = request.form.get('email')
        profile_picture = request.files.get('profile_picture')
        super_user = True if request.form.get('super_user') == 'on' else False

        # Verifica si el correo electrónico ya existe en la base de datos
        if Usuario.query.filter_by(email=email).first():
            flash('El correo electrónico ya está registrado.', 'error')
            return redirect(url_for('usuario.agregar_usuario'))

        # Si el correo electrónico no existe, crea un nuevo usuario
        nuevo_usuario = Usuario(
            nombre=nombre,
            apPat=apPat,
            apMat=apMat,
            password=password,
            email=email,
            superUser=super_user
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario agregado exitosamente.', 'success')
        return redirect(url_for('usuario.agregar_usuario'))

    return render_template('agregar_usuario.html')


@usuario_blueprint.route('/solicitar_id_usuario')
def solicitar_id_usuario():
    return render_template('solicitar_id_usuario.html')

@usuario_blueprint.route('/actualizar_usuario', methods=['POST'])
def actualizar_usuario():
    usuario_id = request.form.get('usuario_id')
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        return render_template('actualizar_usuario.html', usuario_id=usuario_id, usuario=usuario)
    else:
        flash('No se encontró ningún usuario con ese ID.', 'error')
        return redirect(url_for('usuario.solicitar_id_usuario'))

@usuario_blueprint.route('/actualizar_datos_usuario', methods=['POST'])
def actualizar_datos_usuario():
    usuario_id = request.form.get('usuario_id')
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        usuario.nombre = request.form.get('nombre')
        usuario.apPat = request.form.get('apPat')
        usuario.apMat = request.form.get('apMat')
        usuario.password = request.form.get('password')
        usuario.email = request.form.get('email')
        usuario.superUser = True if request.form.get('super_user') == 'on' else False
        db.session.commit()
        flash('Datos del usuario actualizados correctamente.', 'success')
        return redirect(url_for('usuario.menu_usuario'))
    else:
        flash('No se encontró ningún usuario con ese ID.', 'error')
        return redirect(url_for('usuario.solicitar_id_usuario'))


@usuario_blueprint.route('/borrar_usuario', methods=['POST'])
def borrar_usuario():
    usuario_id = request.form.get('usuario_id')
    usuario = Usuario.query.get(usuario_id)

    if usuario:
        # Verificar si el usuario está involucrado en alguna renta
        if usuario.rentas:
            flash('No se puede borrar este usuario porque está involucrado en rentas activas.', 'error')
        else:
            db.session.delete(usuario)
            db.session.commit()
            flash('Usuario borrado correctamente.', 'success')
    else:
        flash('No se encontró ningún usuario con ese ID.', 'error')

    return redirect(url_for('usuario.menu_usuario'))