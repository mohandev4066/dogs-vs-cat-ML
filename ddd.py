import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
import pickle

from keras.layers import Conv2D,MaxPooling2D

pickle_in=open(r"X.pickle","rb")
X=pickle.load(pickle_in)

pickle_in=open(r"y.pickle","rb")
y=pickle.load(pickle_in)

print(X)



X=X/255.0

print(X)

