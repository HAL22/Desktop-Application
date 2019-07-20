"""""

Respresents a data set for particular participant 

"""""

from PyQt5 import QtCore, QtGui, QtWidgets


class DataSet():

    def __init__(self,EDAdata,ECGdata,RSPdata,PPGdata,RadioButton):

        self.EDAdata=EDAdata
        self.ECGdata=ECGdata
        self.RSPdata=RSPdata
        self.PPGdata=PPGdata
        self.RadioButton=RadioButton

        self.Time = None

        self.Min = None

        self.Max = None

        self.NormEDA = []
        self.NormECG = []
        self.NormRSP = []
        self.NormPPG = []

        self.Min = self.getMin()

        self.Max = self.getMax()

        self.NormEDA = self.getNorm(self.EDAdata)
        self.NormECG = self.getNorm(self.ECGdata)
        self.NormPPG = self.getNorm(self.PPGdata)
        self.NormRSP = self.getNorm(self.RSPdata)


    def getMax(self):
        return max(max(self.EDAdata),max(self.ECGdata),max(self.PPGdata),max(self.RSPdata))

    def getMin(self):
        return min(min(self.EDAdata), min(self.ECGdata), min(self.PPGdata), min(self.RSPdata))


    def getNorm(self,data):
        normdata = []

        for x in data:
            normdata.append(((x-self.Min) / (self.Max-self.Min)))


        return normdata



    def getEDAdata(self):
        return self.EDAdata

    def setEDAdata(self,EDAdata):
        self.EDAdata=EDAdata


    def getECGdata(self):
        return self.ECGdata

    def setECGdata(self,ECGdata):
        self.ECGdata = ECGdata

    def getRSPdata(self):
        return self.RSPdata

    def setRSPdata(self,RSPdata):
        return self.RSPdata

    def getPPGdata(self):
        return self.PPGdata

    def setPPGdata(self,PPGdata):
        self.PPGdata=PPGdata

    def getRadioButton(self):
        return self.RadioButton

    def setRadioButton(self,RadioButton):
        self.RadioButton=RadioButton

