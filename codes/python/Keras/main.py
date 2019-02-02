'''
Created on Oct 30, 2018

@author: amin abyaneh
'''

# Choose backend
import os
from matplotlib.pyplot import title
os.environ['KERAS_BACKEND'] = 'tensorflow'

# Main Libraries
import numpy as np
import scipy as sp
import keras as dp

# Keras components
from keras.models   import Sequential
from keras.layers   import Dense, Dropout, Activation, Flatten
from keras.layers   import Convolution2D, MaxPooling2D
from keras.utils    import np_utils
from keras.datasets import mnist

# Other libraries:
from matplotlib import pyplot as plt

def visualize_samples(x_train):
    fig = plt.figure()
    fig.add_axes()
    ax = fig.add_subplot(221)
    ax.imshow(x_train[0])
    ax.set(title = 'train_x[0]')
    ax = fig.add_subplot(222)
    ax.imshow(x_train[1])
    ax.set(title = 'train_x[1]')
    ax = fig.add_subplot(223)
    ax.imshow(x_train[2000])
    ax.set(title = 'train_x[2000]')
    ax = fig.add_subplot(224)
    ax.imshow(x_train[10000])
    ax.set(title = 'train_x[10000]')
    plt.show()

# Main
if __name__ == '__main__':

    # Keras version check
    print('Initializing...')
    print('Keras version: ' + dp.__version__)
    
    # Loading data
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    print('X train shape:', x_train.shape)
    print('Y train shape:', y_train.shape)
    
    # Conforming data by visualization
    visualize_samples(x_train)
    
    # Reshaping input data
    x_train = x_train.reshape(x_train.shape[0], 1, 28, 28)
    x_test = x_test.reshape(x_test.shape[0], 1, 28, 28)
    print('X train after reshape:', x_train.shape)
    print('X test  after reshape:', x_test.shape)
    
    # Convert to float32
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')


    # Convert 1-dimensional class arrays to 10-dimensional class matrices
    y_train = np_utils.to_categorical(y_train, 10)
    y_test = np_utils.to_categorical(y_test, 10)
    print('Y train after reshape:', y_train.shape)
    print('Y test  after reshape:', y_test.shape)
    
    # Creating model
    model = Sequential()
    model.add(Convolution2D(32, (3, 3), activation = 'relu',
                             input_shape = (1,28,28), 
                             data_format = 'channels_first'))
    
    model.add(Convolution2D(32, (3, 3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2,2)))
    model.add(Dropout(0.25))
    
    model.add(Flatten())
    model.add(Dense(128, activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation = 'softmax'))
    
    # Adding optimizer function
    model.compile(loss = 'categorical_crossentropy',
                  optimizer = 'adam',
                  metrics=['accuracy'])
    
    start_training = input('Do you want training to be started?[y/n]')
    if (start_training == 'y'):
        model.fit(x_train, y_train, 
                  batch_size = 32, epochs = 10, verbose = 1)
    else:
        exit(0)
    
    # Evaluate prediction
    print('Evaluation result is: ', model.evaluate(x_test, y_test, verbose = 1))

    
