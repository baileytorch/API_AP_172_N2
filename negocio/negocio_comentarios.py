import requests
import json
from modelos import Comment, Post
from datos import insertar_objeto
from .negocio_publicacion import crear_publicacion


def obtener_data_comentarios(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data...")
        comentarios = respuesta.json()
        for comentario in comentarios:
            id_publicación = crear_publicacion(
                comentario['company']['name'],
                comentario['company']['catchPhrase'],
                comentario['company']['bs']
            )

            crear_comentario(
                comentario['id'],
                comentario['name'],
                comentario['email'],
                comentario['body'],
                id_publicación
            )

    elif respuesta.status_code == 204:
        print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")


def crear_comentario(numero, nombre, correo, contenido, id_post):
    comentario = Comment(
        id=numero,
        name=nombre,
        email=correo,
        body=contenido,
        postId=id_post
    )
    try:
        id_comentario = insertar_objeto(comentario)
        return id_comentario
    except Exception as error:
        print(f'Error al guardar al usuario: {error}')
