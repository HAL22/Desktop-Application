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







