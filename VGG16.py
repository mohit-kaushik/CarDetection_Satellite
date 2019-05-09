import tensorflow as tf
from keras.layers import Dense,Flatten,Conv2D,Activation
from keras.models import Sequential
from keras.layers import MaxPool2D

def VGG16():
    model = Sequential()
    model.add(Conv2D(input_shape=(61,61,4),filters=64,kernel_size=(3,3),padding="same", activation="relu"))
    model.add(Conv2D(filters=64,kernel_size=(3,3),padding="same", activation="relu"))
    model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
    
    return model
