from negocio import registrar_usuario_db, login_usuario
from interfaces import menu_principal, sub_menu


def app():
    print('Aplicación API')
    print('==============')
    while True:
        menu_principal()
        opcion_menu = input('Seleccione su Opción [0-2]: ')
        if opcion_menu == '1':
            registrar_usuario_db()
        elif opcion_menu == '2':
            acceso = login_usuario()
            if acceso == True:
                print('Ingresando...')
                sub_menu()
        elif opcion_menu == '0':
            print('Saliendo...')
            break
        else:
            print('Opción Incorrecta, Intente Nuevamente...')
            
app()
