from database.db import obtener_conexion

def obtener_lecturas():

    conexion = obtener_conexion()

    cursor = conexion.cursor(
        dictionary=True
    )

    sql = """
    SELECT *
    FROM lecturas
    ORDER BY fecha DESC
    """

    cursor.execute(sql)

    datos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return datos

# from database.select import obtener_lecturas

# lecturas = obtener_lecturas()

# for lectura in lecturas:
#     print(lectura)