import importlib
import sys
import datetime
import json

from nupic.data.inference_shifter import InferenceShifter
from nupic.frameworks.opf.model_factory import ModelFactory
from nupic.algorithms.anomaly_likelihood import AnomalyLikelihood
from nupic.frameworks.opf.common_models.cluster_params import getScalarMetricWithTimeOfDayAnomalyParams

class buildmodel:
	def __init__(self):
		#self.model_params = getScalarMetricWithTimeOfDayAnomalyParams(metricData=[0],tmImplementation="cpp")
		with open("model_params.json") as fp:
			self.model_params = json.load(fp)
		print self.model_params
		self.newmodel = ModelFactory.create(self.model_params)
		self.newmodel.enableLearning()
		self.newmodel.enableInference({"predictedField": "value"})
		self.DATE_FORMAT = "%d/%m/%Y %H:%M"
		self.anomalylikelihood = AnomalyLikelihood()
		
	def processdata(self,data):
		timestamp = datetime.datetime.strptime(data[0], self.DATE_FORMAT)
		ce = float(data[1])
		result = self.newmodel.run({"dttm": timestamp,"value": ce})
		#print result
		anomalyScore = result.inferences["anomalyScore"]
		anomaly = self.anomalylikelihood.anomalyProbability(ce, anomalyScore, timestamp)
		logLikelihood = self.anomalylikelihood.computeLogLikelihood(anomaly)
		logLikelihood = logLikelihood*100
		print logLikelihood
		'''if anomaly > 0.999:
			print "Detected high level anomaly at "+str(timestamp)
		elif anomaly>0.958:
			print "Detected medium level anomaly at "+str(timestamp)'''
		if logLikelihood > 20:
			print "Detected high level anomaly at "+str(timestamp)
		elif logLikelihood> 15:
			print "Detected medium level anomaly at "+str(timestamp)
		
	