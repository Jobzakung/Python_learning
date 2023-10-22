import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pickle
import sys

# Load CIFAR-10 dataset
def load_cifar10_dataset(folder_path):
    train_data = []
    train_labels = []

    for i in range(1, 6):
        with open(f"{folder_path}/data_batch_{i}", 'rb') as f:
            data = pickle.load(f, encoding='bytes')
            train_data.append(data[b'data'])
            train_labels.extend(data[b'labels'])

    with open(f"{folder_path}/test_batch", 'rb') as f:
        test_data = pickle.load(f, encoding='bytes')
        test_images = test_data[b'data']
        test_labels = test_data[b'labels']

    train_images = np.vstack(train_data).reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)
    
    return train_images, np.array(train_labels), test_images.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1), np.array(test_labels)

# Specify the folder path where your CIFAR-10 dataset is located
cifar10_folder = "./imageProcessing/Week_10/cifar-10-batches-py"

# Load the dataset
train_images, train_labels, test_images, test_labels = load_cifar10_dataset(cifar10_folder)

# Define class labels
label = ["airplane", "automobile", "bird", "cat", "deer",
         "dog", "frog", "horse", "ship", "truck"]

# Load the pre-trained model
mymodel = tf.keras.models.load_model("imageProcessing/Week_10/resnet_cifar10.h5")
mymodel.summary()

# Normalize test images
t = test_images / 255.0

# Create a flag to indicate if the program should exit
exit_program = False

# Event handling function for key press
def on_key(event):
    global exit_program
    if event.key == 'q':
        exit_program = True

# Connect the key press event handler
plt.connect('key_press_event', on_key)

# Iterate through all test images
for idx in range(len(test_images)):
    if exit_program:
        break  # Exit the loop if 'q' is pressed
    
    img = t[idx].reshape(1, 32, 32, 3)
    result = mymodel.predict(img)
    predicted_class_idx = np.argmax(result[0])
    
    # Get the predicted label
    predicted_label = label[predicted_class_idx]

    # Display the image and the predicted label
    plt.figure(figsize=(6, 6))  # Adjusted figure size for better visualization
    current_image = test_images[idx]  # Assign the image to a variable for readability
    plt.imshow(current_image)
    plt.xlabel(f"Predicted: {predicted_label}", fontsize=8)
    plt.xticks([])
    plt.yticks([])
    plt.show()

# Close the program gracefully
plt.disconnect('key_press_event', on_key)  # Disconnect the event handler
plt.close()  # Close the last figure
sys.exit(0)  # Exit the program
