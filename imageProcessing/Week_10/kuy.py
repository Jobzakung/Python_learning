import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, BatchNormalization, ReLU, Add, AveragePooling2D, Flatten, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.preprocessing.image import ImageDataGenerator



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

# # Load the dataset
train_images, train_labels, test_images, test_labels = load_cifar10_dataset(cifar10_folder)
# Now you can use train_images, train_labels, test_images, and test_labels for your machine learning tasks.
train_images, test_images = train_images / 255.0, test_images / 255.0

# Convert labels to one-hot encoding
train_labels = to_categorical(train_labels, 10)
test_labels = to_categorical(test_labels, 10)

def residual_block(x, filters, kernel_size=3, stride=1):
    y = Conv2D(filters, kernel_size=kernel_size, strides=stride, padding='same')(x)
    y = BatchNormalization()(y)
    y = ReLU()(y)
    y = Conv2D(filters, kernel_size=kernel_size, padding='same')(y)
    y = BatchNormalization()(y)
    
    if stride > 1:
        x = Conv2D(filters, kernel_size=1, strides=stride, padding='same')(x)
    
    out = Add()([x, y])
    out = ReLU()(out)
    return out

def resnet(num_blocks=3):
    input_layer = Input(shape=(32, 32, 3))
    x = Conv2D(64, 3, strides=1, padding='same')(input_layer)  # Changed kernel size to 3x3
    x = BatchNormalization()(x)
    x = ReLU()(x)
    x = AveragePooling2D(3, strides=2, padding='same')(x)
    
    for _ in range(num_blocks):
        x = residual_block(x, 64)
    
    x = AveragePooling2D(8)(x)
    x = Flatten()(x)
    x = Dense(10, activation='softmax')(x)
    
    return Model(inputs=input_layer, outputs=x)
     
# You can increase num_blocks for a deeper network
model = resnet(num_blocks=3)

# Compile the model
model.compile(optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=0.001), 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Define callbacks (optional but useful)
checkpoint = ModelCheckpoint("resnet_cifar10.h5", monitor='val_accuracy', save_best_only=True, mode='max', verbose=1)
early_stopping = EarlyStopping(monitor='val_accuracy', patience=10, verbose=1, restore_best_weights=True)

datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)
# Train the model
history = model.fit(datagen.flow(train_images, train_labels, 
                    epochs=50, 
                    batch_size=128, 
                    validation_split=0.2, 
                    verbose = 1,
                    callbacks=[checkpoint, early_stopping]))

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(test_images, test_labels, verbose=0)
print(f"Test accuracy: {test_accuracy * 100:.2f}%")