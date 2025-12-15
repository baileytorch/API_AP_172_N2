from datos.conexion import sesion
from sqlalchemy import func
from modelos import Usuario


def obtener_listado_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if len(listado_objetos) > 0:
        return listado_objetos


def obtener_usuario_nombre(valor):
    objeto_identificado = sesion.query(Usuario).filter_by(nombre = valor).first()
    if objeto_identificado:
        return objeto_identificado
