import mysql.connector

# def obtener_conexion():

#     conexion = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="admin",
#         database="alimentos_iot"
#     )

#     return conexion

def obtener_conexion():

    conexion = mysql.connector.connect(
        host="turntable.proxy.rlwy.net",
        port=45347,
        user="root",
        password="zQFeKipPVXmlGBTsqJATKJfxlmOcKYtV",
        database="alimentos_iot"
    )

    return conexion