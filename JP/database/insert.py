from database.db import obtener_conexion

def guardar_lectura(
    hogar_id,
    temperatura,
    humedad,
    fecha
):

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    sql = """
    INSERT INTO lecturas(
        hogar_id,
        temperatura,
        humedad,
        fecha
    )
    VALUES(%s,%s,%s,%s)
    """

    valores = (
        hogar_id,
        temperatura,
        humedad,
        fecha
    )

    cursor.execute(sql, valores)

    conexion.commit()

    cursor.close()
    conexion.close()