import joblib
import pandas as pd

# ==========================
# CARGAR MODELOS
# ==========================

modelo = joblib.load(
    "models/random_forest.pkl"
)

encoder_alimento = joblib.load(
    "models/encoder_alimento.pkl"
)

encoder_estado = joblib.load(
    "models/encoder_estado.pkl"
)

# ==========================
# DATOS DE EJEMPLO
# ==========================

temperatura = 28
humedad = 80

alimento = "Platano"
estado = "Maduro"

# ==========================
# CONVERSION
# ==========================

alimento_cod = encoder_alimento.transform(
    [alimento]
)[0]

estado_cod = encoder_estado.transform(
    [estado]
)[0]

# ==========================
# DATAFRAME
# ==========================

entrada = pd.DataFrame(
    [[
        temperatura,
        humedad,
        alimento_cod,
        estado_cod
    ]],
    columns=[
        "temperatura",
        "humedad",
        "alimento",
        "estado"
    ]
)

# ==========================
# PREDICCION
# ==========================

resultado = modelo.predict(
    entrada
)

print()
print("PREDICCION")
print("-" * 30)

print(
    f"Alimento: {alimento}"
)

print(
    f"Estado: {estado}"
)

print(
    f"Vida útil estimada: "
    f"{round(resultado[0],2)} días"
)