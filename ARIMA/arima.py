from pandas import read_csv
from matplotlib import pyplot
import numpy as np

series = read_csv('final - Copy.csv', header=0, index_col=0)
series.plot()
pyplot.show()
rolmean=series.rolling(window=100).mean()
rolstd=series.rolling(window=100).std()
rolmean.plot()
pyplot.show()
rolstd.plot()
pyplot.show()
print(series.head())
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plot_acf(series)
plot_pacf(series, lags=500)
pyplot.show()
from statsmodels.tsa.arima_model import ARIMA
X = series.values
size = int(len(X) * 0.33)
train, test = X[0:size], X[size:len(X)]
history = [x for x in X]
print(len(history))
predictions = []
u_clvl = []
l_clvl = []
std_err = []
anomaly = []
for t in range(len(test)):
	print("Forecasting: ",(t+1)*100/len(test), "% complete...")
	#final - 0,1,1
	model = ARIMA(history, order=(0,1,1))
	model_fit = model.fit(disp=0)
	output, stderr, conf = model_fit.forecast()
	u_clvl.append(conf[0][1])
	l_clvl.append(conf[0][0])
	std_err.append(stderr)
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	#print('predicted=%f, expected=%f' % (yhat, obs))
#print(test)
#print(predictions)
for i in range(len(test)):
    if test[i] > (u_clvl[i] + 2*std_err[i]) or test[i] < (l_clvl[i] - 2*std_err[i]):
        anomaly.append(test[i])
    else:
        anomaly.append(np.NaN)
#print(anomaly)
# plot
pyplot.plot(test)
#pyplot.plot(u_clvl, linestyle='--', color='green')
#pyplot.plot(l_clvl, linestyle='--', color='green')
pyplot.plot(anomaly, marker='.', linestyle='', color='red')
pyplot.plot(predictions, color='orange')
pyplot.show()
