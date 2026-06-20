import tensorflow as tf
from keras.models import Sequential
from keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)
from keras.preprocessing.image import ImageDataGenerator

# ==========================
# CONFIGURACIÓN
# ==========================

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

TRAIN_DIR = "dataset_final/train"
VALID_DIR = "dataset_final/valid"

# ==========================
# GENERADORES
# ==========================

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

valid_datagen = ImageDataGenerator(
    rescale=1./255
)

train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

valid_generator = valid_datagen.flow_from_directory(
    VALID_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# ==========================
# MODELO CNN
# ==========================

model = Sequential()

# Capa 1
model.add(
    Conv2D(
        32,
        (3,3),
        activation='relu',
        input_shape=(224,224,3)
    )
)

model.add(
    MaxPooling2D((2,2))
)

# Capa 2
model.add(
    Conv2D(
        64,
        (3,3),
        activation='relu'
    )
)

model.add(
    MaxPooling2D((2,2))
)

# Capa 3
model.add(
    Conv2D(
        128,
        (3,3),
        activation='relu'
    )
)

model.add(
    MaxPooling2D((2,2))
)

# Aplanar
model.add(
    Flatten()
)

# Densa
model.add(
    Dense(
        128,
        activation='relu'
    )
)

model.add(
    Dropout(0.5)
)

# Salida

model.add(
    Dense(
        train_generator.num_classes,
        activation='softmax'
    )
)

# ==========================
# COMPILAR
# ==========================

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# ==========================
# ENTRENAMIENTO
# ==========================

history = model.fit(
    train_generator,
    validation_data=valid_generator,
    epochs=10
)

# ==========================
# GUARDAR MODELO
# ==========================

model.save(
    "models/cnn_alimentos.keras"
)

print("Modelo guardado correctamente")