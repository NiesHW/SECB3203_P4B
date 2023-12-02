import os
import time
import shutil
import pathlib
import itertools
from PIL import Image


import cv2
img = cv2.imread('D:/DEGREE/YEAR3SEM1/PROG BIOINFORMATICS/Project/Coding/colon_image_sets/')
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_style('darkgrid')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# import Deep learning Libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam, Adamax
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation, Dropout, BatchNormalization
from tensorflow.keras import regularizers

# Ignore Warnings
import warnings
warnings.filterwarnings("ignore")

print ('modules loaded')

data_dir = 'D:/DEGREE/YEAR3SEM1/PROG BIOINFORMATICS/Project/Coding/colon_image_sets/'

filepaths = []
labels = []

folds = os.listdir(data_dir)
for fold in folds:
    foldpath = os.path.join(data_dir, fold)
    filelist = os.listdir(foldpath)
    for file in filelist:
        fpath = os.path.join(foldpath, file)
        
        filepaths.append(fpath)
        labels.append(fold)

# Concatenate data paths with labels into one dataframe
Fseries = pd.Series(filepaths, name= 'filepaths')
Lseries = pd.Series(labels, name='labels')

df = pd.concat([Fseries, Lseries], axis= 1)
print(df)

image_files = [file for file in os.listdir(data_dir) if file.endswith(('.png', '.jpg', '.jpeg'))]

# Create a list to store paths of missing or problematic files
missing_files = []
# Check each image file
for image_file in image_files:
    image_path = os.path.join(data_dir, image_file)
    # Try to read the image using OpenCV
    try:
        img = cv2.imread('D:/DEGREE/YEAR3SEM1/PROG BIOINFORMATICS/Project/Coding/colon_image_sets/')
        if img is None:
            missing_files.append(image_path)
    except Exception as e:
        print(f"Error reading {image_path}: {str(e)}")
        missing_files.append(image_path)
# Print or handle missing files
if len(missing_files) > 0:
    print("Missing or problematic files:")
    for missing_file in missing_files:
        print(missing_file)
else:
    print("No missing or problematic files found.")

# train dataframe
train_df, dummy_df = train_test_split(df,  train_size= 0.8, shuffle= True, random_state= 123)

# valid and test dataframe
valid_df, test_df = train_test_split(dummy_df,  train_size= 0.6, shuffle= True, random_state= 123)

images_directory = 'D:/DEGREE/YEAR3SEM1/PROG BIOINFORMATICS/Project/Coding/colon_image_sets/colon_aca/'
image_files = [f for f in os.listdir(images_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Number of bins for data binning
num_bins = 10

# Loop through each image
for image_file in image_files:
    # Construct the full path to the image
    image_path = os.path.join(images_directory, image_file)

    # Read the colored image
    img = cv2.imread(image_path)

    # Split the image into individual color channels
    b, g, r = cv2.split(img)

    # Perform data binning for each color channel
    binned_b = np.digitize(b, bins=np.linspace(0, 255, num_bins + 1))
    binned_g = np.digitize(g, bins=np.linspace(0, 255, num_bins + 1))
    binned_r = np.digitize(r, bins=np.linspace(0, 255, num_bins + 1))

    # Normalize the binned values to the range [0, 255]
    binned_b = (255 * (binned_b / num_bins)).astype(np.uint8)
    binned_g = (255 * (binned_g / num_bins)).astype(np.uint8)
    binned_r = (255 * (binned_r / num_bins)).astype(np.uint8)

    # Merge the binned color channels back into an image
    binned_img = cv2.merge([binned_b, binned_g, binned_r])

    # Display original and binned images
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Colored Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(binned_img, cmap='viridis', interpolation='none')
    plt.title('Binned Colored Image')
    plt.axis('off')

    plt.show()

    # Save the binned image 
    output_path = os.path.join(images_directory, f'binned_{image_file}')
    cv2.imwrite(output_path, cv2.cvtColor(binned_img, cv2.COLOR_BGR2RGB))