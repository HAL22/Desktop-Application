"""""

Respresents a data set for particular participant 

"""""

from PyQt5 import QtCore, QtGui, QtWidgets


class DataSet():

    def __init__(self,Time,EDAdata,ECGdata,RSPdata,PPGdata,RadioButton):

        self.EDAdata=self.convert_EDA(EDAdata)
        self.ECGdata= self.convert_ECG(ECGdata)
        self.RSPdata=RSPdata
        self.PPGdata=PPGdata
        self.RadioButton=RadioButton

        self.Time = Time

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

    def getTime(self):
        return self.Time


    def setTime(self,time):

        self.Time=time


    def getNormEDA(self):
        return self.NormEDA

    def setNormEDA(self,normeda):
        self.NormEDA=normeda

    def getNormECG(self):
        return self.NormECG

    def setNormECG(self,ecg):
        self.NormECG = ecg

    def getNormPPG(self):
        return self.NormPPG

    def setNormPPG(self,normppg):
        self.NormPPG=normppg




    def convert_EDA(self,con_eda):

        eda = []

        for x in con_eda:
            eda.append((x/1000000))

        return eda

    def convert_ECG(self,con_ecg):

        ecg = []

        for x in con_ecg:
            ecg.append((x/1000))

        return ecg



