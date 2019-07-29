import tensorflow as tf

from keras.layers import Dense,Flatten,Conv2D,Activation,BatchNormalization
from keras.models import Sequential

def CNNModel():
    model = Sequential()
    model.add(Conv2D(input_shape=(61,61,4),filters=64,kernel_size=(5,5),padding="same"))
    model.add(BatchNormalization())
    model.add(Activation("relu"))
    return model
