from modelos import Post
from datos import insertar_objeto


def crear_publicacion(titulo, contenido, id_usuario):
    publicacion = Post(
        title=titulo,
        body=contenido,
        userId=id_usuario
    )
    try:
        id_publicacion = insertar_objeto(publicacion)
        return id_publicacion
    except Exception as error:
        print(f'Error al guardar la geolocalización: {error}')
