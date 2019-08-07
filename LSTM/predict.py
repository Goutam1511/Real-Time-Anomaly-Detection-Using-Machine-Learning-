from Dataprocessor import Dataloader
from keras.models import load_model
import os
import numpy as np
from matplotlib import pyplot
import lstm
from sklearn.metrics import mean_squared_error
from math import sqrt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #Hide messy TensorFlow warnings

model = load_model("lstm.h5")

seq_len = 400
data = Dataloader(seq_len,'merged-dataset-with-noise-and-seasonal(datetime).csv','Value')
x_train, y_train = data.get_train_data()
x_test,y_test = data.get_test_data()
#print (x_train.shape)
errordata = []

print ('\n[Model] Predicting point by point')

predicted_data = lstm.predict_point_by_point(model,x_test,y_test,x_train,y_train)

x = []
y = []
errordata=[]
for i in range(len(predicted_data)):
	error = abs(y_test[i]-predicted_data[i])
	errordata.append(error)
	if (error > 0.5):
	    x.append(i)
	    y.append(y_test[i])

mse = mean_squared_error(predicted_data, y_test)
rmse = sqrt(mse)
print('RMSE: %f' % rmse)

#pyplot.subplot(211)
pyplot.plot(y_test,label = 'Actual')
pyplot.plot(predicted_data,label = 'Predicted', color='orange')
pyplot.scatter(x, y, label = "Anomalies", color = 'red')
#pyplot.legend()
#pyplot.subplot(212)
#pyplot.plot(errordata, label = 'Error', color= 'green')
#pyplot.legend(['Actual','Predicted','Error'])
pyplot.show()

'''for i in range(len(predicted)):
	if (predicted[i]-y_test[i])>0.24:
		print ("Found anomaly at ",i+len(y_train))'''
