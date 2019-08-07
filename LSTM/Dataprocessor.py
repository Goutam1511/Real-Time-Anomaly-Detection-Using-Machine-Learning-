import pandas as pd
import numpy as np
from numpy import newaxis
import warnings
warnings.filterwarnings("ignore") # ignore messy numpy warnings
from sklearn import preprocessing

'''class Dataloader:
	def __init__(self,seq_len):
		df = pd.read_csv("Patternchange1.csv")
		j = 0
		df = pd.DataFrame(df['Pattern'])
		x = df.values #returns a numpy array
		min_max_scaler = preprocessing.MinMaxScaler()
		df = pd.DataFrame(min_max_scaler.fit_transform(x))
		series = df.copy()
		window_size = seq_len
		series_s = series.copy()
		for i in range(window_size):
			series = pd.concat([series, series_s.shift(-(i+1))], axis = 1)
		series.dropna(axis=0, inplace=True)
		nrow = round(0.25*series.shape[0])
		#print (nrow)
		self.train = series.iloc[:nrow, :]
		self.test = series.iloc[nrow:,:]
		train_X = self.train.iloc[:,:-1]
		train_y = self.train.iloc[:,-1]
		test_X = self.test.iloc[:,:-1]
		test_y = self.test.iloc[:,-1]
		train_X = train_X.values
		self.train_y = train_y.values
		self.test_X = test_X.values
		self.test_y = test_y.values
		self.train_X = train_X.reshape(train_X.shape[0],train_X.shape[1],1)
		#self.test_X = test_X.reshape(test_X.shape[0],test_X.shape[1],1)
		#print(self.train_X.shape)
		#print(self.train_y.shape)
		#print(self.test_X.shape)
		#print(self.test_y.shape)

	def get_train_data(self):
		return self.train_X,self.train_y
		
	def get_test_data(self):
		return self.test_X,self.test_y'''

class Dataloader:
	def __init__(self,window_size,filename,column):
		df = pd.read_csv(filename)
		df = pd.DataFrame(df[column])
		isplit = round(len(df)*0.25)
		self.data_train = df.get(column).values[:isplit]
		self.data_test = df.get(column).values[isplit:]
		self.len_train = len(self.data_train)
		self.len_test = len(self.data_test)
		self.window_size = window_size
		
	def normalise(self,window_data):
		window_data = window_data.reshape(-1,1)
		scaler = preprocessing.MinMaxScaler()
		return scaler.fit_transform(window_data)
	
	def get_train_data(self):
		data_x = []
		data_y = []
		for i in range(self.len_train-self.window_size):
			window = self.data_train[i:i+self.window_size+1]
			normalised_window = self.normalise(window)
			x = normalised_window[:-1]
			y = normalised_window[-1]
			data_x.append(x)
			data_y.append(y)
		data_x = np.array(data_x)
		data_y = np.array(data_y)
		return data_x.reshape(data_x.shape[0],data_x.shape[1],1), data_y
		
	def get_test_data(self):
		data_x = []
		data_y = []
		for i in range(self.len_test-self.window_size):
			window = self.data_test[i:i+self.window_size+1]
			normalised_window = self.normalise(window)
			x = normalised_window[:-1]
			y = normalised_window[-1]
			data_x.append(x)
			data_y.append(y[0])
		#data_x = np.array(data_x)
		#data_y = np.array(data_y)
		return data_x, data_y
			
			
