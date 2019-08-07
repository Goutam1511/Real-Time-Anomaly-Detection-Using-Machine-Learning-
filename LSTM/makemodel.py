from Dataprocessor import Dataloader
import lstm
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error as mse

import warnings
warnings.filterwarnings("ignore") # ignore messy numpy warnings

seq_len = 400
data = Dataloader(seq_len,'merged-dataset-with-noise-and-seasonal(datetime).csv','Value')
x_train,y_train = data.get_train_data()

#print (x_train)
#print ("\n \n \n")
#print (y_train)
#print ("\n \n \n")
#print (y_train.shape)

epochs  = 15

model = lstm.build_model([1, 50, 100, 1])

model.fit(
    x_train,
    y_train,
    batch_size=32,
    nb_epoch=epochs,
    validation_split=0.05)
	
#print (model.get_weights())
	
model.save("lstm.h5")
	
print ("\n[Model] Model Trained and saved")
