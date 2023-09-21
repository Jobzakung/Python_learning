import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical

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

# Now you can use train_images, train_labels, test_images, and test_labels for your machine learning tasks.
train_images, test_images = train_images / 255.0, test_images / 255.0

# Convert labels to one-hot encoding
train_labels = to_categorical(train_labels, num_classes=10)
test_labels = to_categorical(test_labels, num_classes=10)

# Define a CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Define callbacks for early stopping and model checkpointing
callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
    tf.keras.callbacks.ModelCheckpoint("cifar10_model.h5", save_best_only=True),
]

# Train the model
history = model.fit(train_images, train_labels, epochs=50, batch_size=64, 
                    validation_data=(test_images, test_labels), callbacks=callbacks)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(test_images, test_labels)

print(f'Test accuracy: {test_accuracy * 100:.2f}%')
