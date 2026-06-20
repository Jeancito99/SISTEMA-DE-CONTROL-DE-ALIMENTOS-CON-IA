import tensorflow as tf
import numpy as np

from keras.preprocessing import image

modelo = tf.keras.models.load_model(
    "models/cnn_alimentos.keras"
)

clases = [
    "lechuga",
    "platano",
    "pollo",
    "tomate"
]

ruta_imagen = "prueba.jpg"

img = image.load_img(
    ruta_imagen,
    target_size=(224,224)
)

img_array = image.img_to_array(img)

img_array = img_array / 255.0

img_array = np.expand_dims(
    img_array,
    axis=0
)

prediccion = modelo.predict(
    img_array
)

indice = np.argmax(prediccion)

print(
    "Alimento:",
    clases[indice]
)

print(
    "Confianza:",
    round(
        float(
            np.max(prediccion)
        ) * 100,
        2
    ),
    "%"
)