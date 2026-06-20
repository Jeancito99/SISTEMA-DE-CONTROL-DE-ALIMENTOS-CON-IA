import pandas as pd
import random

# ==========================
# CONFIGURACIÓN
# ==========================

alimentos = [
    "Platano",
    "Tomate",
    "Lechuga",
    "Pollo"
]

estados = [
    "Fresco",
    "Maduro",
    "Deteriorado"
]

datos = []

# ==========================
# GENERAR REGISTROS
# ==========================

for i in range(5000):

    alimento = random.choice(alimentos)

    estado = random.choice(estados)

    temperatura = round(
        random.uniform(18,35),
        2
    )

    humedad = round(
        random.uniform(40,90),
        2
    )

    # VIDA UTIL SIMULADA

    if estado == "Fresco":
        vida_util = random.randint(7,15)

    elif estado == "Maduro":
        vida_util = random.randint(3,7)

    else:
        vida_util = random.randint(1,3)

    datos.append([
        temperatura,
        humedad,
        alimento,
        estado,
        vida_util
    ])

# ==========================
# DATAFRAME
# ==========================

df = pd.DataFrame(
    datos,
    columns=[
        "temperatura",
        "humedad",
        "alimento",
        "estado",
        "vida_util"
    ]
)

# ==========================
# GUARDAR CSV
# ==========================

df.to_csv(
    "dataset_ml.csv",
    index=False
)

print(
    "Dataset creado correctamente"
)

print(df.head())