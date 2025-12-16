class Streaming:
    """
    Clase que gestiona la reproducción de contenidos
    (películas y series) y muestra el catálogo disponible.
    """

    def __init__(self, gestor_usuarios):
        """
        Inicializa la clase Streaming.
        :param gestor_usuarios: instancia de GestorUsuarios para manejar favoritos
        """
        self.gestor = gestor_usuarios

    def reproducir(self, titulo, duracion, username, es_serie=False):
        """
        Simula la reproducción de una película o serie.

        :param titulo: Nombre del contenido
        :param duracion: Duración en minutos (película) o número de capítulos (serie)
        :param username: Usuario que está reproduciendo
        :param es_serie: Booleano, True si es serie, False si es película
        """
        progreso = 1  # Minuto actual o capítulo actual

        while True:
            print(f"\n🎬 Reproduciendo: {titulo}")

            # Mostrar progreso según tipo de contenido
            if es_serie:
                print(f"📺 Capítulo: {progreso}/{duracion}")
                print("3. ⏭ Siguiente capítulo")
                print("4. ⏮ Capítulo anterior")
            else:
                print(f"⏱ Minutos: {progreso}/{duracion}")

            # Opciones generales
            print("1. ▶ Play")
            print("2. ⏸ Pause")
            print("5. ❤️ Guardar como favorito")
            print("6. ⏹ Stop")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                print("▶ Reproduciendo...")
                progreso += 1 if es_serie else 5  # Avanzar capítulo o minutos
            elif opcion == "2":
                print("⏸ Reproducción en pausa.")
            elif opcion == "3" and es_serie:
                if progreso < duracion:
                    progreso += 1
                else:
                    print("📌 Último capítulo.")
            elif opcion == "4" and es_serie:
                if progreso > 1:
                    progreso -= 1
                else:
                    print("📌 Primer capítulo.")
            elif opcion == "5":
                # Guardar contenido como favorito del usuario
                exito = self.gestor.guardar_favorito(username, titulo)
                if exito:
                    print(f"❤️ {titulo} guardado como favorito.")
                else:
                    print("❌ No se pudo guardar como favorito.")
            elif opcion == "6":
                print(f"⏹ Saliendo de {titulo}...")
                break
            else:
                print("❌ Opción no válida.")

            # Finalización automática si se alcanza la duración
            if progreso >= duracion:
                print(f"✅ Has terminado de ver {titulo}.")
                break

    # Mostrar todo el catálogo (películas y series)
    def mostrar_todo(self, username):
        print("\n🎞️ --- TODO EL CATÁLOGO ---")
        print("\n🎬 Películas:")
        print("1. Avengers (143 min)")
        print("2. Matrix (136 min)")
        print("3. Interstellar (169 min)")
        print("\n📺 Series:")
        print("4. Breaking Bad (62 capítulos)")
        print("5. Dark (26 capítulos)")
        print("6. Stranger Things (34 capítulos)")
        print("7. Volver")

        opcion = input("Qué deseas ver: ")

        if opcion == "1":
            self.reproducir("Avengers", 143, username)
        elif opcion == "2":
            self.reproducir("Matrix", 136, username)
        elif opcion == "3":
            self.reproducir("Interstellar", 169, username)
        elif opcion == "4":
            self.reproducir("Breaking Bad", 62, username, es_serie=True)
        elif opcion == "5":
            self.reproducir("Dark", 26, username, es_serie=True)
        elif opcion == "6":
            self.reproducir("Stranger Things", 34, username, es_serie=True)
        elif opcion == "7":
            return
        else:
            print("❌ Opción no válida.")

    # Mostrar solo películas
    def mostrar_peliculas(self, username):
        print("\n--- Películas ---")
        print("1. Avengers")
        print("2. Matrix")
        print("3. Interstellar")
        print("4. Volver")

        opcion = input("Qué película deseas ver: ")

        if opcion == "1":
            self.reproducir("Avengers", 143, username)
        elif opcion == "2":
            self.reproducir("Matrix", 136, username)
        elif opcion == "3":
            self.reproducir("Interstellar", 169, username)
        elif opcion == "4":
            return
        else:
            print("❌ Opción no válida.")

    # Mostrar solo series
    def mostrar_series(self, username):
        print("\n--- Series ---")
        print("1. Breaking Bad (62 capítulos)")
        print("2. Dark (26 capítulos)")
        print("3. Stranger Things (34 capítulos)")
        print("4. Volver")

        opcion = input("Qué serie deseas ver: ")

        if opcion == "1":
            self.reproducir("Breaking Bad", 62, username, es_serie=True)
        elif opcion == "2":
            self.reproducir("Dark", 26, username, es_serie=True)
        elif opcion == "3":
            self.reproducir("Stranger Things", 34, username, es_serie=True)
        elif opcion == "4":
            return
        else:
            print("❌ Opción no válida.")
