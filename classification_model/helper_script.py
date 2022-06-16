# A helper function that converts images to RGB 

import os
import imghdr
from PIL import Image

def convert_images_rgb(PATH):
    """
    Converts images to RGB in the sub-directories of the given directory.
    
    Args:
        path: String value to the image directory(folder)
        
    Returns:
        None
    """
    # loop through the main directory (images folder)
    for dir_name in os.listdir(PATH):
        # Join subfolder and the main path
        dir_path = PATH + "\\" + dir_name
        # Loop through the subfolder  (test or train)
        for folder_name in os.listdir(dir_path):
            print(f"\nScanning folder: {dir_name}\{folder_name}\n")
            image_folder_path = dir_path + "\\" + folder_name
            images = os.listdir(image_folder_path)
            # Loop through the individual images
            for image in images:
                img_dir = image_folder_path + "\\"+ image
                im = Image.open(img_dir)
                rgb_im = im.convert("RGB")
                rgb_im.save(img_dir)
                print(f"File Name: {image} Type: {imghdr.what(img_dir)}")



# Helper function to create tensorboard callbacks
import tensorflow as tf
import datetime

def create_tensorboard_callback(dir_name, experiment_name):
    #os.makedirs(dir_name, exist_ok=True)
    log_dir = dir_name + "/" + experiment_name + "/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir = log_dir)
    print(f"Saving TensorBoard log files to: {log_dir}")
    return tensorboard_callback



import matplotlib.pyplot as plt
def plot_loss_curves(history):
    """
    Returns seperate loss curves for training and validaion metrics.

    Args:
        history: TensorFlow history object

    Returns:
        Plots of training/validation loss and accuracy metrics
    """
    
    loss = history.history["loss"]
    val_loss = history.history["val_loss"]

    accuracy = history.history["accuracy"]
    val_accuracy = history.history["val_accuracy"]

    epochs = range(len(history.history["loss"])) # how many epochs we run for

    # Plot loss
    plt.plot(epochs, loss, label = "training_loss")
    plt.plot(epochs, val_loss, label = "val_loss")
    plt.title("loss")
    plt.xlabel("epochs")
    plt.legend()

    # Plot accuracy
    plt.figure()
    plt.plot(epochs, accuracy, label = "training_accuracy")
    plt.plot(epochs, val_accuracy, label = "val_accuracy")
    plt.title("accuracy")
    plt.xlabel("epochs")
    plt.legend()



# Function to compare training histories
def compare_history(original_history, new_history, initial_epochs=5):
    """
    Compares two TensorFlow model History objects.
    
    Args:
      original_history: History object from original model (before new_history)
      new_history: History object from continued model training (after original_history)
      initial_epochs: Number of epochs in original_history (new_history plot starts from here) 
    """
    # Get original history measurements
    acc = original_history.history["accuracy"]
    loss = original_history.history["loss"]

    val_acc = original_history.history["val_accuracy"]
    val_loss = original_history.history["val_loss"]

    # Combine original history metrics with new_history metrics
    total_acc = acc + new_history.history["accuracy"]
    total_loss = loss + new_history.history["loss"]

    total_val_acc = val_acc + new_history.history["val_accuracy"]
    total_val_loss = val_loss + new_history.history["val_loss"]

    # Make plot for accuracy
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    plt.plot(total_acc, label="Training Accuracy")
    plt.plot(total_val_acc, label="Val Accuracy")
    plt.plot([initial_epochs-1, initial_epochs-1], plt.ylim(), label="Start Fine Tuning")
    plt.legend(loc="lower right")
    plt.title("Training and Validation Accuracy")

    # Make plot for loss
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 2)
    plt.plot(total_loss, label="Training Loss")
    plt.plot(total_val_loss, label="Val Loss")
    plt.plot([initial_epochs-1, initial_epochs-1], plt.ylim(), label="Start Fine Tuning")
    plt.legend(loc="upper right")
    plt.title("Training and Validation Loss")