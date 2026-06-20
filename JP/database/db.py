import mysql.connector

def obtener_conexion():

    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="alimentos_iot"
    )

    return conexion