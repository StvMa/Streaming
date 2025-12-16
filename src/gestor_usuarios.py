import json
import os
from usuario import Usuario

# Ruta donde se guardarán los usuarios en formato JSON
RUTA_ARCHIVO = "data/usuarios.json"


class GestorUsuarios:
    """
    Clase encargada de la gestión de usuarios:
    - Registro
    - Inicio de sesión
    - Manejo de favoritos
    - Persistencia en archivo JSON
    """

    def __init__(self):
        """
        Constructor de la clase.
        Verifica que exista la carpeta 'data' y el archivo de usuarios.
        Si no existen, los crea automáticamente.
        """
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(RUTA_ARCHIVO):
            with open(RUTA_ARCHIVO, "w") as f:
                json.dump([], f)

    def cargar_usuarios(self):
        """
        Carga los usuarios desde el archivo JSON
        :return: lista de usuarios
        """
        with open(RUTA_ARCHIVO, "r") as f:
            return json.load(f)

    def guardar_usuarios(self, lista):
        """
        Guarda la lista de usuarios en el archivo JSON
        :param lista: lista de usuarios
        """
        with open(RUTA_ARCHIVO, "w") as f:
            json.dump(lista, f, indent=4)

    def registrar_usuario(self, username, password, email):
        """
        Registra un nuevo usuario en el sistema.
        Verifica que el nombre de usuario no exista.
        """
        usuarios = self.cargar_usuarios()

        for u in usuarios:
            if u["username"] == username:
                return False, "El usuario ya existe."

        # Crear usuario con lista de favoritos vacía
        nuevo = Usuario(username, password, email)

        usuarios.append(nuevo.to_dict())
        self.guardar_usuarios(usuarios)

        return True, "Usuario registrado correctamente."

    def login(self, username, password):
        """
        Verifica las credenciales del usuario
        :return: (True, usuario) o (False, mensaje)
        """
        usuarios = self.cargar_usuarios()

        for u in usuarios:
            if u["username"] == username and u["password"] == password:
                # Asegurarse de que 'favoritos' exista
                if "favoritos" not in u:
                    u["favoritos"] = []
                return True, u

        return False, "Credenciales incorrectas."

    def guardar_favorito(self, username, titulo):
        """
        Guarda un contenido como favorito para un usuario específico
        """
        usuarios = self.cargar_usuarios()

        for u in usuarios:
            if u["username"] == username:
                # Inicializar lista de favoritos si no existe
                if "favoritos" not in u:
                    u["favoritos"] = []

                if titulo not in u["favoritos"]:
                    u["favoritos"].append(titulo)
                    self.guardar_usuarios(usuarios)
                    return True

        return False

    def obtener_favoritos(self, username):
        """
        Devuelve la lista de favoritos de un usuario
        """
        usuarios = self.cargar_usuarios()

        for u in usuarios:
            if u["username"] == username:
                # Inicializar lista de favoritos si no existe
                if "favoritos" not in u:
                    u["favoritos"] = []
                return u["favoritos"]

        return []
