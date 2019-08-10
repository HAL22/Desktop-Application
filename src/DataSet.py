"""""

Respresents a data set for particular participant 

"""""

from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np


class DataSet():

    def __init__(self,Time,EDAdata,ECGdata,RSPdata,PPGdata,RadioButton):

        self.EDAdata=EDAdata
        self.ECGdata=ECGdata
        self.RSPdata=RSPdata
        self.PPGdata=PPGdata
        self.RadioButton=RadioButton
        self.Time = Time

        self.Min = None
        self.Max = None

        self.TotalArray = np.concatenate(((self.EDAdata),self.RSPdata,self.PPGdata,(self.ECGdata)))

        self.MEAN = np.mean(self.TotalArray)

        self.NormEDA = []
        self.NormECG = []
        self.NormRSP = []
        self.NormPPG = []

        self.Min = self.getMin()

        self.Max = self.getMax()

        self.NormEDA = self.getNorm((self.EDAdata))
        self.NormECG = self.getNorm((self.ECGdata))
        self.NormPPG = self.getNorm(self.PPGdata)
        self.NormRSP = self.getNorm(self.RSPdata)

        self.TotalNormArray = np.concatenate((self.NormEDA,self.NormECG,self.NormPPG,self.NormRSP))

        ##TRIGGERS####

        self.Triggers = []

        ##Testing ###
        self.Triggers = [100.00,100.05,100.10,100.25,100.34]


        ##Annotation##

        self.UserAnnotations = []






    def getMax(self):
        return max(self.TotalArray)

    def getMin(self):
        return min(self.TotalArray)

    def getNormMax(self):
        return max(self.TotalNormArray)

    def getNormMin(self):
        return min(self.TotalNormArray)


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

    def getNormRSP(self):
        return self.NormRSP

    def setNormRSP(self,rsp):
        self.NormRSP=rsp



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

    def getTriggers(self):
        return self.Triggers

    def setTriggers(self,triggers):
        self.Triggers=triggers

    def getUserAnnotation(self):
        return self.UserAnnotations

    def setUserAnnotation(self,userannotation):

        self.UserAnnotations = userannotation




