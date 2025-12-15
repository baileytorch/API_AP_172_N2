from negocio import registrar_usuario_db, login_usuario,listado_users_api,crear_user_api,modificar_user_api,eliminar_user_api
from interfaces import menu_principal, sub_menu

def app():
    print('Aplicación API')
    print('==============')
    while True:
        print()
        menu_principal()
        opcion_menu = input('Seleccione su Opción [0-2]: ')
        if opcion_menu == '1':
            registrar_usuario_db()
        elif opcion_menu == '2':
            acceso = login_usuario()
            if acceso == True:
                print('Ingresando...')
                while True:
                    print()
                    sub_menu()
                    opcion_submenu = input('Seleccione su Opción [0-4]: ')
                    if opcion_submenu == '1':
                        listado_users_api()
                    elif opcion_submenu == '2':
                        crear_user_api()
                    elif opcion_submenu == '3':
                        modificar_user_api()
                    elif opcion_submenu == '4':
                        eliminar_user_api()
                    elif opcion_submenu == '0':
                        print('Volviendo al Menú Principal...')
                        break
                    else:
                        print('Opción Incorrecta, Intente Nuevamente...')
        elif opcion_menu == '0':
            print('Saliendo...')
            break
        else:
            print('Opción Incorrecta, Intente Nuevamente...')
            
app()
