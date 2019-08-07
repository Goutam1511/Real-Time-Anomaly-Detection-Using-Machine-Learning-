import os
import math
import numpy as np
from numpy import newaxis
from keras.layers import Dense, Activation, Dropout, LSTM
from keras.models import Sequential, load_model
from keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.metrics import mean_squared_error as mse
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #Hide messy TensorFlow warnings


def build_model(layers):
	model = Sequential()
	model.add(LSTM(input_dim = 1, output_dim= 50))
	#model.add(Dropout(0.5))
	#model.add(LSTM(256,return_sequences = False))
	model.add(Dropout(0.5))
	model.add(Dense(1))
	#model.add(Activation("linear"))
	model.compile(loss="mse", optimizer="adam")
	#model.summary()
	return model
	
def predict_point_by_point(model,x_test,y_test,x_train,y_train):
	predicted_data = []
#Predict each timestep given the last sequence of true data, in effect only predicting 1 step ahead each time
	for i in range(len(x_test)):
		data = x_test[i].reshape(1,x_test[i].shape[0],1)
		x_train = np.append(x_train,data,axis=0)
		x_train = np.delete(x_train,0,0)
		y_train = np.append(y_train,y_test[i])
		y_train = np.delete(y_train,0,0)
		predicted = model.predict(data)[0][0]
		#predicted = np.reshape(predicted,predicted.size)
		predicted_data.append(predicted)
		print (i)
	return predicted_data
	
