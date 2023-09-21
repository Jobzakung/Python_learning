import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10


# Load the CIFAR-10 dataset and split it into train and test sets
# data = tf.keras.datasets.cifar10.load_data()
# (train_images, train_labels), (test_images, test_labels) = data
cifar10_url = "http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()


# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Convert labels to one-hot encoding
train_labels = tf.keras.losses.to_categorical(train_labels, num_classes=10)
test_labels = tf.keras.losses.to_categorical(test_labels, num_classes=10)

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
