import numpy as np
import matplotlib.pyplot as plt
import pathlib
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dense, Dropout, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import random
import PIL

# Use the data path from the previous code
path = "/content/dataset/cell_images"

data_dir = pathlib.Path(path).with_suffix('')
image_count = len(list(data_dir.glob('*/*.png')))
print(image_count)

uninfected = list(data_dir.glob("Uninfected/*"))
parasitized = list(data_dir.glob("Parasitized/*"))
print("Number of uninfected cells", len(uninfected))
print("Number of parasitized cells", len(parasitized))

# Display sample images
PIL.Image.open(uninfected[1])
PIL.Image.open(parasitized[1])

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
input_tensor = Input(shape=(img_width, img_height, 3), dtype=np.float32, name="malaria_cells")
x = Conv2D(64, (3, 3), activation='relu', padding='same')(input_tensor)
x = MaxPooling2D((2, 2))(x)
x = BatchNormalization()(x)
x = Dropout(0.3)(x)

x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2))(x)

x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = BatchNormalization()(x)
x = Dropout(0.3)(x)
x = Dense(256, activation='relu')(x)
x = BatchNormalization()(x)
output_tensor = Dense(1, activation='sigmoid')(x)

model = Model(inputs=input_tensor, outputs=output_tensor)

model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

# Model training
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
    training_data,
    epochs=epochs,
    validation_data=validation_data,
    callbacks=[model_checkpoint_callback, early_stopping],
    verbose=1
)

# Save the model
model.save("malaria_cnn_model.h5")

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

parasitized_path = random.choice(parasitized)
uninfected_path = random.choice(uninfected)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
evaluate_random_image(parasitized_path, ax1)
evaluate_random_image(uninfected_path, ax2)
plt.tight_layout()
plt.show()
#the evaluate method is called on the trained model using the validation data. 
# The validation_data is a generator created using ImageDataGenerator to flow images from the validation directory. 
# This method calculates the loss and metrics (in this case, accuracy) on the provided validation dataset.
#Here's what each component does:
#model.evaluate(validation_data): This method computes the loss and metrics of the model on the validation dataset.It returns a list containing the loss and accuracy 
