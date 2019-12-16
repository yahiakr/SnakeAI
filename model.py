from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(8,input_dim=12, activation='sigmoid', name='fc1'),
    layers.Dense(6, activation='relu', name='fc2'),
    layers.Dense(4,activation='softmax', name='output')])

model.compile(optimizer=keras.optimizers.Adam(0.01),loss='categorical_crossentropy', metrics=['accuracy'])