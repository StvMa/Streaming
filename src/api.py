from flask import Flask, jsonify, request
from gestor_usuarios import GestorUsuarios
import json
import os

app = Flask(__name__)
gestor = GestorUsuarios()

# ----------------------------
# RUTA CONTENIDOS
# ----------------------------
RUTA_CONTENIDOS = 'data/contenidos.json'

# ----------------------------
# SERIALIZACIÓN CONTENIDOS
# ----------------------------
def cargar_contenidos():
    if not os.path.exists(RUTA_CONTENIDOS):
        return []
    with open(RUTA_CONTENIDOS, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_contenidos(contenidos):
    with open(RUTA_CONTENIDOS, 'w', encoding='utf-8') as f:
        json.dump(contenidos, f, indent=4, ensure_ascii=False)

# ----------------------------
# SERVICIO 1 - INICIO
# ----------------------------
@app.route('/', methods=['GET'])
def inicio():
    return jsonify({
        "estado": "API del Sistema de Streaming funcionando",
        "endpoints": [
            "/", "/contenidos", "/peliculas", "/series",
            "/usuarios"
        ]
    })

# ----------------------------
# SERVICIO 2 - VER CONTENIDOS
# ----------------------------
@app.route('/contenidos', methods=['GET'])
def ver_contenidos():
    return jsonify(cargar_contenidos())

# ----------------------------
# SERVICIO 3 - VER PELÍCULAS
# ----------------------------
@app.route('/peliculas', methods=['GET'])
def ver_peliculas():
    contenidos = cargar_contenidos()
    peliculas = [c for c in contenidos if c.get("tipo") == "pelicula"]
    return jsonify(peliculas)

# ----------------------------
# SERVICIO 4 - VER SERIES
# ----------------------------
@app.route('/series', methods=['GET'])
def ver_series():
    contenidos = cargar_contenidos()
    series = [c for c in contenidos if c.get("tipo") == "serie"]
    return jsonify(series)

# ----------------------------
# SERVICIO 5 - VER USUARIOS
# ----------------------------
@app.route('/usuarios', methods=['GET'])
def ver_usuarios():
    return jsonify(gestor.cargar_usuarios())
# ----------------------------
# MAIN
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)
