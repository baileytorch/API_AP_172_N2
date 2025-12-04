from prettytable import PrettyTable
import requests
import json
from datos import obtener_listado_objetos
from modelos import Comment, Post
from datos import insertar_objeto


def obtener_data_comentarios(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data...")
        comentarios = respuesta.json()
        for comentario in comentarios:
            crear_comentario(
                comentario['id'],
                comentario['name'],
                comentario['email'],
                comentario['body'],
                comentario['postId']
            )

    elif respuesta.status_code == 204:
        print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")

def listado_comentarios():
    tabla_comentarios = PrettyTable()
    tabla_comentarios.field_names = [
        'N°', 'Nombre', 'Email','Comentario','Id Publicación']
    listado_comentarios = obtener_listado_objetos(Comment)

    if listado_comentarios:
        for comentario in listado_comentarios:
            tabla_comentarios.add_row(
                [comentario.id, comentario.name, comentario.email,comentario.body,comentario.postId])
        # tabla_comentarios._min_width = {"N°": 5, "Título": 50,"Contenido":100}
        # tabla_comentarios._max_width = {"N°": 5, "Título": 50,"Contenido":100}
        print(tabla_comentarios)


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
