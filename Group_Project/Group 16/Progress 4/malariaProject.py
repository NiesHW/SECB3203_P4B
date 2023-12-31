import numpy as np
import matplotlib.pyplot as plt
import pathlib
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dense, Dropout, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from sklearn.model_selection import train_test_split
import random
from google.colab import files  # Import the files module for Google Colab

# Upload the Kaggle API key
uploaded = files.upload()

# Move the Kaggle API key to the correct directory
!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# Download a portion (5%) of the dataset using Kaggle API
!kaggle datasets download -d saifuddin0324/malaria-cell-detection -p /content/dataset --unzip --force

# Adjust the path to the dataset
data_dir = pathlib.Path("/content/dataset/cell_images")

# Select a smaller subset of the dataset
random.seed(42)

parasitized_files = list(data_dir.glob("Parasitized/*.png"))
uninfected_files = list(data_dir.glob("Uninfected/*.png"))

selected_parasitized = random.sample(parasitized_files, 100)
selected_uninfected = random.sample(uninfected_files, 100)

selected_files = selected_parasitized + selected_uninfected

# Image data preprocessing
batch_size = 16  # Adjusted batch size
img_height = 64  # Adjusted image size
img_width = 64   # Adjusted image size

# Data augmentation and normalization
train_datagen = ImageDataGenerator(
    rotation_range=40,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.3,
    rescale=1/255
)

train_data = train_datagen.flow_from_directory(
    data_dir,
    subset="training",
    class_mode="binary",
    target_size=(img_width, img_height),
    batch_size=batch_size,
    shuffle=True
)

validation_data = train_datagen.flow_from_directory(
    data_dir,
    subset="validation",
    class_mode="binary",
    target_size=(img_width, img_height),
    batch_size=batch_size,
    shuffle=False
)

# Model architecture
input_tensor = Input(shape=(img_width, img_height, 3))
x = Conv2D(32, (3, 3), activation='relu', padding='same')(input_tensor)  # Reduced number of filters
x = MaxPooling2D((2, 2))(x)
x = BatchNormalization()(x)
x = Dropout(0.3)(x)

x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2))(x)

x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)  # Reduced number of neurons
x = BatchNormalization()(x)
x = Dropout(0.3)(x)

output_tensor = Dense(1, activation='sigmoid')(x)

model = Model(inputs=input_tensor, outputs=output_tensor)

model.compile(optimizer=Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

# Model training with reduced epochs
epochs = 5

checkpoint_filepath = '/tmp/checkpoint'
model_checkpoint_callback = ModelCheckpoint(
    filepath=checkpoint_filepath,
    save_weights_only=True,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True
)

early_stopping = EarlyStopping(patience=3, min_delta=1e-3, restore_best_weights=True)

history = model.fit(
    train_data,
    epochs=epochs,
    validation_data=validation_data,
    callbacks=[model_checkpoint_callback, early_stopping],
    verbose=1
)

# Save the model
model.save("malaria-cnn-v1-fast-100images-5epochs.keras")

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

