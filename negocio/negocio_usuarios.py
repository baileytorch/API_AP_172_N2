from modelos import Usuario
from datos import insertar_objeto, obtener_usuario_nombre
import getpass
import bcrypt


def registrar_usuario_db():
    nombre_usuario = input('Ingrese Nombre Usuario:')
    correo = input('Correo electrónico: ')
    contrasena = getpass.getpass('Ingrese Contraseña: ')

    if nombre_usuario != '' and correo != '' and contrasena != '':
        hashed = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())

        usuario = Usuario(
            nombre=nombre_usuario,
            correo=correo,
            contrasena_hash=hashed,
        )

        id_usuario = insertar_objeto(usuario)
        if id_usuario is not None:
            print(f'Usuario registrado con id: {id_usuario}')


def login_usuario():
    nombre_usuario = input('Ingrese Nombre Usuario:')
    if nombre_usuario != '':
        usuario = obtener_usuario_nombre(nombre_usuario)
        if usuario:
            contrasena = getpass.getpass('Ingrese Contraseña: ')
            if contrasena != '':
                if bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena_hash.encode('utf-8')):
                    print("Acceso Concedido!")
                    return True
                else:
                    print("Contraseña Incorrecta")
        else:
            print('Usuario NO registrado.')
