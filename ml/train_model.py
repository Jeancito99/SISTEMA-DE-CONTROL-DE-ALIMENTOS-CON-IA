import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

# ==========================
# CARGAR DATASET
# ==========================

df = pd.read_csv("dataset_ml.csv")

# ==========================
# CONVERTIR TEXTO A NUMEROS
# ==========================

encoder_alimento = LabelEncoder()
encoder_estado = LabelEncoder()

df["alimento"] = encoder_alimento.fit_transform(
    df["alimento"]
)

df["estado"] = encoder_estado.fit_transform(
    df["estado"]
)

# ==========================
# VARIABLES
# ==========================

X = df[
    [
        "temperatura",
        "humedad",
        "alimento",
        "estado"
    ]
]

y = df["vida_util"]

# ==========================
# DIVISION TRAIN TEST
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# MODELO
# ==========================

modelo = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

modelo.fit(
    X_train,
    y_train
)

# ==========================
# EVALUACION
# ==========================

predicciones = modelo.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predicciones
)

r2 = r2_score(
    y_test,
    predicciones
)

print()
print("RESULTADOS")
print("-" * 30)

print("MAE:", round(mae,2))
print("R2 :", round(r2,2))

# ==========================
# GUARDAR MODELO
# ==========================

joblib.dump(
    modelo,
    "models/random_forest.pkl"
)

joblib.dump(
    encoder_alimento,
    "models/encoder_alimento.pkl"
)

joblib.dump(
    encoder_estado,
    "models/encoder_estado.pkl"
)

print()
print("Modelo guardado correctamente")