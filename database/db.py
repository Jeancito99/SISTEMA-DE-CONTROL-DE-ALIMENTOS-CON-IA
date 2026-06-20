# import mysql.connector

# # def obtener_conexion():

# #     conexion = mysql.connector.connect(
# #         host="localhost",
# #         user="root",
# #         password="admin",
# #         database="alimentos_iot"
# #     )

# #     return conexion

# def obtener_conexion():

#     conexion = mysql.connector.connect(
#         host="turntable.proxy.rlwy.net",
#         port=45347,
#         user="root",
#         password="zQFeKipPVXmlGBTsqJATKJfxlmOcKYtV",
#         database="alimentos_iot"
#     )

#     return conexion


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Construir la URI con variables de entorno
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:TU_PASSWORD@turntable.proxy.rlwy.net:45347/alimentos_iot"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
