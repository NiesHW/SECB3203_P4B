import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Flatten, Input, Conv2D, MaxPooling2D, Dropout, BatchNormalization, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.vgg19 import preprocess_input
import pathlib
from google.colab import files

# Upload the Kaggle API key
uploaded = files.upload()

# Move the Kaggle API key to the correct directory
!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# Download the dataset using Kaggle API
!kaggle datasets download -d saifuddin0324/malaria-cell-detection -p /content/dataset --unzip --force

# Use the data path from the previous code
path = "/content/dataset/cell_images"

data_dir = pathlib.Path(path).with_suffix('')
image_count = len(list(data_dir.glob('*/*.png')))
print("Total number of images:", image_count)

uninfected = list(data_dir.glob("Uninfected/*"))
parasitized = list(data_dir.glob("Parasitized/*"))
print("Number of uninfected cells:", len(uninfected))
print("Number of parasitized cells:", len(parasitized))

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

X_train, y_train = next(training_data)

# Display a sample of images
fig = plt.figure(figsize=(10, 5))

for i in range(10):
    ax = fig.add_subplot(2, 5, i+1)
    ax.imshow(X_train[i])
    ax.axis("off")
    ax.set_title("Uninfected" if y_train[i] == 1 else "Parasitized", fontsize=10)
fig.suptitle("Sample of Malaria Cells")
plt.tight_layout()

# Model architecture
input_tensor = Input(shape=(img_width, img_height, 3), dtype=tf.float32, name="malaria_cells")
X = Conv2D(filters=64, kernel_size=(3, 3), strides=(1, 1), padding="same", activation="relu")(input_tensor)
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

model = Model(inputs=input_tensor, outputs=output)
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
model.save("malaria_cnn_model.h5")

# Evaluate the model on the validation data
model.evaluate(validation_data)

# Plot training history
plt.figure(figsize=(7, 4))
ax = plt.axes()
epochs_range = range(1, len(history.history["loss"]) + 1)

ax.plot(epochs_range, history.history["loss"], marker="o", label="Training loss")
ax.plot(epochs_range, history.history["val_loss"], marker="*", ls="--", label="Validation loss")
ax.legend()
plt.show()

# Plot accuracy history
plt.figure(figsize=(7, 4))
ax = plt.axes()
ax.plot(epochs_range, history.history["accuracy"], marker="o", label="Training accuracy")
ax.plot(epochs_range, history.history["val_accuracy"], marker="*", ls="--", label="Validation accuracy")
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

# Additional code for VGG19 model

image_gen_vgg = ImageDataGenerator(
    validation_split=0.3,
    preprocessing_function=preprocess_input
)

training_data_vgg = image_gen_vgg.flow_from_directory(
    data_dir,
    subset="training",
    class_mode="binary",
    target_size=(img_width, img_height),
    batch_size=batch_size
)

validation_data_vgg = image_gen_vgg.flow_from_directory(
    data_dir,
    subset="validation",
    class_mode="binary",
    target_size=(img_width, img_height),
    batch_size=batch_size
)

base_model = VGG19(weights="imagenet", include_top=False, input_shape=(img_width, img_height, 3))
base_model.trainable = False

input_vgg = Input(shape=(img_width, img_height, 3), dtype=tf.float32)
vgg_model = base_model(input_vgg)
X_vgg = Flatten()(vgg_model)
output_vgg = Dense(1, activation="sigmoid", name="cell_classes")(X_vgg)

model_vgg = Model(inputs=input_vgg, outputs=output_vgg)
model_vgg.summary()

optim_vgg = tf.keras.optimizers.Adam()
loss_vgg = tf.keras.losses.BinaryCrossentropy()

model_vgg.compile(optimizer=optim_vgg, loss=loss_vgg, metrics=["accuracy"])
epochs_vgg = 5
early_stopping_vgg = tf.keras.callbacks.EarlyStopping(patience=3, min_delta=1e-3, restore_best_weights=True)

history_vgg = model_vgg.fit(training_data_vgg, epochs=epochs_vgg, validation_data=validation_data_vgg, callbacks=[early_stopping_vgg])
model_vgg.evaluate(validation_data_vgg)
