import random
from datetime import datetime

from database.insert import guardar_lectura

hogares = {
    1: "Hogar A",
    2: "Hogar B",
    3: "Hogar C"
}


def generar_todos_los_hogares():

    datos = []

    for hogar_id, nombre in hogares.items():

        temperatura = round(
            random.uniform(18, 35),
            2
        )

        humedad = round(
            random.uniform(40, 90),
            2
        )

        fecha = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        lectura = {
            "hogar_id": hogar_id,
            "hogar": nombre,
            "temperatura": temperatura,
            "humedad": humedad,
            "fecha": fecha
        }

        # Guardar en MySQL
        guardar_lectura(
            hogar_id,
            temperatura,
            humedad,
            fecha
        )

        datos.append(lectura)

    return datos


if __name__ == "__main__":

    resultado = generar_todos_los_hogares()

    for dato in resultado:
        print(dato)