from gestor_usuarios import GestorUsuarios
from streaming import Streaming

# Crear instancias principales
gestor = GestorUsuarios()      # Maneja usuarios y favoritos
stream = Streaming(gestor)     # Maneja catálogo y reproducción de contenidos

def menu_catalogo(username):
    """
    Menú del catálogo de contenidos.
    Permite al usuario:
    - Ver todos los contenidos
    - Ver solo películas
    - Ver solo series
    - Volver al menú principal
    """
    while True:
        print("\n--- Catálogo de Contenidos ---")
        print("1. Ver todos los contenidos")
        print("2. Películas")
        print("3. Series")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            stream.mostrar_todo(username)
        elif opcion == "2":
            stream.mostrar_peliculas(username)
        elif opcion == "3":
            stream.mostrar_series(username)
        elif opcion == "4":
            break
        else:
            print("❌ Opción no válida.")

def menu_usuario(usuario):
    """
    Menú principal después de iniciar sesión.
    Permite al usuario:
    - Acceder al catálogo
    - Ver su lista de favoritos
    - Cerrar sesión
    """
    username = usuario["username"]

    while True:
        print(f"\n--- Bienvenido {username} ---")
        print("1. Ver catálogo")
        print("2. Ver favoritos")
        print("3. Cerrar sesión")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_catalogo(username)  # Accede al menú de catálogo
        elif opcion == "2":
            favoritos = gestor.obtener_favoritos(username)  # Obtiene favoritos del usuario
            if favoritos:
                print(f"\n--- Favoritos de {username} ---")
                for i, titulo in enumerate(favoritos, start=1):
                    print(f"{i}. {titulo}")
            else:
                print("No tienes favoritos aún.")
        elif opcion == "3":
            print("Cerrando sesión...")
            break
        else:
            print("❌ Opción no válida.")

def menu_principal():
    """
    Menú principal del sistema.
    Permite:
    - Registrar nuevos usuarios
    - Iniciar sesión
    - Salir del programa
    """
    while True:
        print("\n--- Sistema de Streaming ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Registro de un nuevo usuario
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            email = input("Correo: ")
            ok, msg = gestor.registrar_usuario(username, password, email)
            print(msg)

        elif opcion == "2":
            # Inicio de sesión
            username = input("Usuario: ")
            password = input("Contraseña: ")
            ok, usuario = gestor.login(username, password)
            if ok:
                print("Inicio de sesión exitoso.")
                menu_usuario(usuario)  # Accede al menú del usuario
            else:
                print("❌ Credenciales incorrectas.")

        elif opcion == "3":
            # Salida del programa
            print("Saliendo del sistema...")
            break

        else:
            print("❌ Opción no válida.")

# Punto de entrada del programa
menu_principal()
