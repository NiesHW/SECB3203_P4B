import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PIL
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Flatten, Input, Conv2D, MaxPooling2D, Dropout, BatchNormalization, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve
from tensorflow.keras.utils import plot_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img, array_to_img
from tensorflow.keras.applications.vgg19 import VGG19
import seaborn as sns
import pathlib

# Data exploration using Pandas
path = "/kaggle/input/cell-images-for-detecting-malaria"
data_dir = pathlib.Path(path).with_suffix('')
image_count = len(list(data_dir.glob('*/*.png')))
print(image_count)




# Image data preprocessing
batch_size = 32
img_height = 150
img_width = 150
image_gen = ImageDataGenerator(
    rotation_range=40,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.3,
    rescale=1/255
)

# Training and validation data
training_data = image_gen.flow_from_directory(
    data_dir,
    subset="training",
    class_mode="binary",
    target_size=(img_width, img_height),
    batch_size=batch_size
)

validation_data = image_gen.flow_from_directory(
    data_dir,
    subset="validation",
    class_mode="binary",
    target_size=(img_width, img_height),
    batch_size=batch_size
)

# Model architecture
input = Input(shape=(img_width, img_height, 3), dtype=tf.float32, name="malaria_cells")
X = Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding="same", activation="relu")(input)
X = MaxPooling2D(pool_size=(2, 2))(X)
X = BatchNormalization()(X)
X = Dropout(0.3)(X)
X = Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding="same", activation="relu")(X)
X = MaxPooling2D(pool_size=(2, 2))(X)

X = GlobalAveragePooling2D()(X)
X = Dense(512, activation="relu")(X)
X = BatchNormalization()(X)
X = Dropout(0.3)(X)
X = Dense(256, activation="relu")(X)
X = BatchNormalization()(X)
output = Dense(1, activation="sigmoid", name="cell_classes")(X)

model = Model(inputs=input, outputs=output)
plot_model(model, "model.png", show_layer_activations=True)
model.summary()

# Model compilation
optim = tf.keras.optimizers.Adam()
loss = tf.keras.losses.BinaryCrossentropy()
model.compile(optimizer=optim, loss=loss, metrics=["accuracy"])

# Model training
epochs = 5
checkpoint_filepath = '/tmp/checkpoint'
model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_filepath,
    save_weights_only=True,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True
)

early_stopping = tf.keras.callbacks.EarlyStopping(patience=3, min_delta=1e-3, restore_best_weights=True)

history = model.fit(training_data, epochs=epochs, validation_data=validation_data, callbacks=[model_checkpoint_callback, early_stopping])

# Save the model
model.save("malaria-cnn-v1.keras")

# Evaluate the model on the validation data
model.evaluate(validation_data)

# Plot training history
plt.figure(figsize=(7, 4))
ax = plt.axes()
ax.plot(range(1, epochs+1), history.history["loss"], marker="o", label="Training loss")
ax.plot(range(1, epochs+1), history.history["val_loss"], marker="*", ls="--", label="Validation loss")
ax.legend()
plt.show()

# Plot accuracy history
plt.figure(figsize=(7, 4))
ax = plt.axes()
ax.plot(range(1, epochs+1), history.history["accuracy"], marker="o", label="Training accuracy")
ax.plot(range(1, epochs+1), history.history["val_accuracy"], marker="*", ls="--", label="Validation accuracy")
ax.legend()
plt.show()

# Predictions on random images
def evaluate_random_image(path, ax):
    image = load_img(str(path), target_size=(img_width, img_height))
    img_arr = img_to_array(image)
    img_arr /= 255
    pred = model.predict(img_arr.reshape(1, *img_arr.shape), verbose=0).flatten()
    label = "Parasitized" if pred < 0.5 else "Uninfected"
    ax.imshow(img_arr, vmin=1, vmax=1)
    ax.set_title(f"{label} - {pred[0]:.2%}", size=10)
    ax.axis("off")

parasitized_path = list(data_dir.glob("Parasitized/*"))
uninfected_path = list(data_dir.glob("Uninfected/*"))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
index = np.random.randint(len(parasitized_path))
evaluate_random_image(parasitized_path[index], ax1)
evaluate_random_image(uninfected_path[index], ax2)
plt.tight_layout()

# Transfer learning using VGG19
base_model = VGG19(weights="imagenet", include_top=False, input_shape=(img_width, img_height, 3))
base_model.trainable = False

# VGG19-based model
input = Input(shape=(img_width, img_height, 3), dtype=tf.float32)
vgg_model = base_model(input)
X = Flatten()(vgg_model)
output = Dense(1, activation="sigmoid", name="cell_classes")(X)

model_vgg = Model(inputs=input, outputs=output)
model_vgg.summary()

# Model compilation
optim = tf.keras
