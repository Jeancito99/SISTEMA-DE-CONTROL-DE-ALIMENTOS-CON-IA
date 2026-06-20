from flask import Flask
from flask import render_template
from flask import jsonify

from simulador.generar_datos import generar_todos_los_hogares

from database.select import obtener_lecturas

app = Flask(__name__)

# ==========================
# DASHBOARD
# ==========================

@app.route("/")
def dashboard():

    lecturas = obtener_lecturas()

    ultima = None

    if lecturas:
        ultima = lecturas[0]

    return render_template(
        "index.html",
        ultima=ultima,
        lecturas=lecturas
    )

# ==========================
# API IOT
# ==========================

@app.route("/api/datos")
def api_datos():

    datos = generar_todos_los_hogares()

    return jsonify(datos)

# ==========================
# HISTORIAL
# ==========================

@app.route("/api/lecturas")
def api_lecturas():

    datos = obtener_lecturas()

    return jsonify(datos)

# ==========================
# PREDICCION
# ==========================

@app.route("/api/predecir")
def api_predecir():

    resultado = {
        "alimento":"Platano",
        "estado":"Maduro",
        "vida_util":4
    }

    return jsonify(resultado)

# ==========================
# MAIN
# ==========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )