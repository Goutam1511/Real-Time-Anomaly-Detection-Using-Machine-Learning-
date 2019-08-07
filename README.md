# Real-Time-Anomaly-Detection-Using-Machine-Learning

# <1.1>  Introduction

Every industry with networking integrated into their infrastructure requires an autonomous system to monitor its respective network performance statistics and apprehend any situation as they arrive. This requirement hugely benefits from the advent of machine learning methodologies which help computers to closely emulate human analytical skills by autonomously gauging the performance and general traits of any network’s dataflow and pointing out potential information that can help in improving the said network’s statistics. Hence, the monitoring system should closely inspect such metrics (like network throughput, nature of incoming and outgoing packets of data, network and transmission control layer statistics, etc.) in real time and analyse them as desired. This project is aimed at proposing such a solution, i.e. a model, that will be able to understand legitimate trends, as and when they appear, of any given time series based statistical data of network metrics and detect anomalous behaviour out of the same in real time.

# <1.2> Objectives

The two major phases of the project are described briefly as below.

# <1.2.1> Developing a customised time series dataset

•	Since procuring actual time series data of data traffic generated on industrial networks is not practically feasible for this project, we need the next best alternative to base our operations on.

•	To evaluate each of the three proposed models in a uniform manner, create identical testing environments and converge onto common grounds of comparable forecasting and anomaly detection results, we will synthesize our own dataset with manually injected trends, noise, seasonality and anomalies.

•	This dataset will be a customised univariate time series of packet flow which will mirror real life network trends as much practically as possible.

# <1.2.2> Investigating potential forecasting models

•	The primary goal of this project is to design an algorithmic statistical evaluation solution which will be able to detect anomalies in a time series dataset of network packet capture on a real time basis. 

•	This project will be aimed to investigate three potential machine learning models, i.e., the Auto-Regressive Integrated Moving Average (ARIMA) model, followed by Long Short Term Memory (LSTM) model and ultimately the Hierarchical Temporal Memory (HTM) model. 
