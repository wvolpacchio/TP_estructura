from telefono import Telefono

def mostrar_menu_principal(telefono):
    while True:
        print("\n--- Menu Principal ---")
        print("1. Contactos")
        print("2. Mensajeria SMS")
        print("3. Llamadas")
        print("4. Email")
        print("5. App Store")
        print("6. Configuracion")
        print("7. Encender/Apagar Telefono")
        print("0. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_contactos(telefono)
        elif opcion == "2":
            menu_sms(telefono)
        elif opcion == "3":
            menu_llamadas(telefono)
        elif opcion == "4":
            menu_email(telefono)
        elif opcion == "5":
            menu_app_store(telefono)
        elif opcion == "6":
            menu_configuracion(telefono)
        elif opcion == "7":
            if telefono.encendido:
                telefono.apagar()
            else:
                telefono.encender()
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

def menu_contactos(telefono):
    while True:
        print("\n--- Menu de Contactos ---")
        print("1. Agendar Contacto")
        print("2. Actualizar Contacto")
        print("3. Mostrar Contactos")
        print("0. Volver al Menu Principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            numero = input("Ingrese el numero de telefono: ")
            telefono.contactos.agendar_contacto(nombre, numero)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto a actualizar: ")
            nuevo_numero = input("Ingrese el nuevo numero: ")
            telefono.contactos.actualizar_contacto(nombre, nuevo_numero)
        elif opcion == "3":
            telefono.contactos.mostrar_contactos()
        elif opcion == "0":
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

def menu_sms(telefono):
    while True:
        print("\n--- Menu de Mensajeria SMS ---")
        print("1. Enviar SMS")
        print("2. Ver Bandeja de Entrada")
        print("3. Eliminar SMS")
        print("0. Volver al Menu Principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            numero_destino = input("Ingrese el numero de destino: ")
            mensaje = input("Ingrese el mensaje: ")
            telefono.sms_bandeja.append(SMS(telefono.num_telefono, numero_destino, mensaje))
            telefono.sms_bandeja[-1].enviar()
        elif opcion == "2":
            for sms in telefono.sms_bandeja:
                sms.listar_sms()
        elif opcion == "3":
            index = int(input("Ingrese el indice del mensaje a eliminar: "))
            if 0 <= index < len(telefono.sms_bandeja):
                telefono.sms_bandeja[index].eliminar_sms()
                del telefono.sms_bandeja[index]
            else:
                print("Indice no valido.")
        elif opcion == "0":
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

def menu_llamadas(telefono):
    while True:
        print("\n--- Menu de Llamadas ---")
        print("1. Realizar Llamada")
        print("2. Recibir Llamada")
        print("3. Terminar Llamada")
        print("0. Volver al Menu Principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            numero_destino = input("Ingrese el numero de destino: ")
            telefono.llamadas.append(Llamada())
            telefono.llamadas[-1].realizar_llamada(numero_destino)
        elif opcion == "2":
            numero_origen = input("Ingrese el numero de origen: ")
            telefono.llamadas.append(Llamada())
            telefono.llamadas[-1].recibir_llamada(numero_origen)
        elif opcion == "3":
            if telefono.llamadas:
                telefono.llamadas[-1].terminar_llamada()
                telefono.llamadas.pop()
            else:
                print("No hay llamadas en curso.")
        elif opcion == "0":
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

def menu_email(telefono):
    while True:
        print("\n--- Menu de Email ---")
        print("1. Enviar Email")
        print("2. Ver Emails No Leidos")
        print("3. Ver Emails por Fecha")
        print("4. Eliminar Email")
        print("0. Volver al Menu Principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            destinatario = input("Ingrese el destinatario: ")
            asunto = input("Ingrese el asunto: ")
            cuerpo = input("Ingrese el cuerpo del mensaje: ")
            telefono.email.enviar_email(destinatario, asunto, cuerpo)
        elif opcion == "2":
            telefono.email.ver_email_no_leido()
        elif opcion == "3":
            telefono.email.ver_email_por_fecha()
        elif opcion == "4":
            id_email = int(input("Ingrese el ID del email a eliminar: "))
            telefono.email.eliminar_email(id_email)
        elif opcion == "0":
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

def menu_app_store(telefono):
    while True:
        print("\n--- Menu de App Store ---")
        print("1. Buscar App")
        print("2. Descargar App")
        print("0. Volver al Menu Principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre_app = input("Ingrese el nombre de la app a buscar: ")
            telefono.app_store.buscar_app(nombre_app)
        elif opcion == "2":
            nombre_app = input("Ingrese el nombre de la app a descargar: ")
            telefono.app_store.descargar_app(telefono, nombre_app)
        elif opcion == "0":
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

def menu_configuracion(telefono):
    while True:
        print("\n--- Menu de Configuracion ---")
        print("1. Cambiar Nombre del Telefono")
        print("2. Cambiar Codigo de Desbloqueo")
        print("3. Activar/Desactivar Red Movil")
        print("4. Activar/Desactivar Datos Moviles")
        print("0. Volver al Menu Principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            telefono.configuracion.cambiar_nombre(nuevo_nombre)
        elif opcion == "2":
            nuevo_codigo = input("Ingrese el nuevo codigo de desbloqueo: ")
            telefono.configuracion.cambiar_codigo_desbloqueo(nuevo_codigo)
        elif opcion == "3":
            telefono.configuracion.alternar_red_movil()
            print("Red movil activada." if telefono.configuracion.red_movil_activa else "Red movil desactivada.")
        elif opcion == "4":
            telefono.configuracion.alternar_datos_moviles()
            print("Datos moviles activados." if telefono.configuracion.datos_movil_activos else "Datos moviles desactivados.")
        elif opcion == "0":
            break
        else:
            print("Opcion no valida. Intente de nuevo.")