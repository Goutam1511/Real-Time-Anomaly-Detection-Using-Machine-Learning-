from htm import buildmodel
import csv

newmodel = buildmodel()
inputFile = open("anomalies.csv", "r")
csvReader = csv.reader(inputFile)
csvReader.next()
csvReader.next()

for row in csvReader:
	newmodel.processdata(row)

