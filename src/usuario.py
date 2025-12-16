class Usuario:
    """
    Representa un usuario del sistema de streaming,
    incluyendo su lista de favoritos.
    """

    def __init__(self, username, password, email, favoritos=None):
        self.username = username
        self.password = password
        self.email = email
        self.favoritos = favoritos if favoritos else []

    def to_dict(self):
        """
        Convierte el objeto Usuario a diccionario
        para guardarlo en JSON.
        """
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "favoritos": self.favoritos
        }
