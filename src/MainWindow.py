"""""

Desktop Application for visualising physiological data

@author Thethela Faltein

"""""

from PyQt5 import QtCore, QtGui, QtWidgets
from src.DataSet import DataSet
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import QMainWindow, QLabel, QCheckBox, QWidget
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
import xlrd




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 685)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.centralhorizontallayout = QtWidgets.QHBoxLayout()
        self.centralhorizontallayout.setObjectName("centralhorizontallayout")
        self.left_widget = QtWidgets.QWidget(self.centralwidget)
        self.left_widget.setObjectName("left_widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.left_widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.left_main_horizontallayout = QtWidgets.QHBoxLayout()
        self.left_main_horizontallayout.setObjectName("left_main_horizontallayout")
        self.left_left_scrollArea = QtWidgets.QScrollArea(self.left_widget)
        self.left_left_scrollArea.setMouseTracking(False)
        self.left_left_scrollArea.setTabletTracking(False)
        self.left_left_scrollArea.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.left_left_scrollArea.setAutoFillBackground(False)
        self.left_left_scrollArea.setWidgetResizable(True)
        self.left_left_scrollArea.setObjectName("left_left_scrollArea")
        self.left_left_scrollarea_widget = QtWidgets.QWidget()
        self.left_left_scrollarea_widget.setGeometry(QtCore.QRect(0, 0, 104, 544))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_left_scrollarea_widget.sizePolicy().hasHeightForWidth())
        self.left_left_scrollarea_widget.setSizePolicy(sizePolicy)
        self.left_left_scrollarea_widget.setObjectName("left_left_scrollarea_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_left_scrollarea_widget)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.DataSetLabel = QtWidgets.QLabel(self.left_left_scrollarea_widget)
        self.DataSetLabel.setMaximumSize(QtCore.QSize(16777215, 21))
        self.DataSetLabel.setObjectName("DataSetLabel")
        self.verticalLayout_3.addWidget(self.DataSetLabel)
        self.DataSet1 = QtWidgets.QRadioButton(self.left_left_scrollarea_widget)
        self.DataSet1.setObjectName("DataSet1")
        self.verticalLayout_3.addWidget(self.DataSet1)
        self.DataSet2 = QtWidgets.QRadioButton(self.left_left_scrollarea_widget)
        self.DataSet2.setObjectName("DataSet2")
        self.verticalLayout_3.addWidget(self.DataSet2)
        self.LineBreakerDataSet = QtWidgets.QLabel(self.left_left_scrollarea_widget)
        self.LineBreakerDataSet.setText("")
        self.LineBreakerDataSet.setObjectName("LineBreakerDataSet")
        self.verticalLayout_3.addWidget(self.LineBreakerDataSet, 0, QtCore.Qt.AlignBottom)
        self.left_left_scrollArea.setWidget(self.left_left_scrollarea_widget)
        self.left_main_horizontallayout.addWidget(self.left_left_scrollArea)
        self.scrollArea = QtWidgets.QScrollArea(self.left_widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 190, 544))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TransformLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.TransformLabel.setMaximumSize(QtCore.QSize(16777215, 21))
        self.TransformLabel.setObjectName("TransformLabel")
        self.verticalLayout.addWidget(self.TransformLabel)
        self.Line_Graphs_Overlayed = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Line_Graphs_Overlayed.setObjectName("Line_Graphs_Overlayed")
        self.verticalLayout.addWidget(self.Line_Graphs_Overlayed)
        self.Line_Graphs_Normalized =QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Line_Graphs_Normalized.setObjectName("Line_Graphs_Normalized")
        self.verticalLayout.addWidget(self.Line_Graphs_Normalized)
        self.LineBreakerTransform = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.LineBreakerTransform.setText("")
        self.LineBreakerTransform.setObjectName("LineBreakerTransform")
        self.verticalLayout.addWidget(self.LineBreakerTransform, 0, QtCore.Qt.AlignBottom)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.left_main_horizontallayout.addWidget(self.scrollArea)
        self.left_right_scrollArea = QtWidgets.QScrollArea(self.left_widget)
        self.left_right_scrollArea.setWidgetResizable(True)
        self.left_right_scrollArea.setObjectName("left_right_scrollArea")
        self.left_right_scrollarea_widget = QtWidgets.QWidget()
        self.left_right_scrollarea_widget.setGeometry(QtCore.QRect(0, 0, 99, 544))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_right_scrollarea_widget.sizePolicy().hasHeightForWidth())
        self.left_right_scrollarea_widget.setSizePolicy(sizePolicy)
        self.left_right_scrollarea_widget.setObjectName("left_right_scrollarea_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.left_right_scrollarea_widget)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ChannelLabel = QtWidgets.QLabel(self.left_right_scrollarea_widget)
        self.ChannelLabel.setMaximumSize(QtCore.QSize(16777215, 21))
        self.ChannelLabel.setObjectName("ChannelLabel")
        self.verticalLayout_5.addWidget(self.ChannelLabel)
        self.EDA = QtWidgets.QCheckBox(self.left_right_scrollarea_widget)
        self.EDA.setEnabled(True)
        self.EDA.setIconSize(QtCore.QSize(16, 16))
        self.EDA.setChecked(True)
        self.EDA.setTristate(False)
        self.EDA.setObjectName("EDA")
        self.verticalLayout_5.addWidget(self.EDA)
        self.ECG = QtWidgets.QCheckBox(self.left_right_scrollarea_widget)
        self.ECG.setChecked(True)
        self.ECG.setObjectName("ECG")
        self.verticalLayout_5.addWidget(self.ECG)
        self.RSP = QtWidgets.QCheckBox(self.left_right_scrollarea_widget)
        self.RSP.setChecked(True)
        self.RSP.setObjectName("RSP")
        self.verticalLayout_5.addWidget(self.RSP)
        self.PPG = QtWidgets.QCheckBox(self.left_right_scrollarea_widget)
        self.PPG.setChecked(True)
        self.PPG.setObjectName("PPG")
        self.verticalLayout_5.addWidget(self.PPG)
        self.LineBreakerChannel = QtWidgets.QLabel(self.left_right_scrollarea_widget)
        self.LineBreakerChannel.setText("")
        self.LineBreakerChannel.setObjectName("LineBreakerChannel")
        self.verticalLayout_5.addWidget(self.LineBreakerChannel, 0, QtCore.Qt.AlignBottom)
        self.left_right_scrollArea.setWidget(self.left_right_scrollarea_widget)
        self.left_main_horizontallayout.addWidget(self.left_right_scrollArea)
        self.horizontalLayout_5.addLayout(self.left_main_horizontallayout)
        self.centralhorizontallayout.addWidget(self.left_widget)
        self.right_widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.right_widget_2.setObjectName("right_widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.right_widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.right_scrollArea = QtWidgets.QScrollArea(self.right_widget_2)
        self.right_scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.right_scrollArea.setWidgetResizable(True)
        self.right_scrollArea.setObjectName("right_scrollArea")
        self.right_scrollArea_widget = QtWidgets.QWidget()
        self.right_scrollArea_widget.setGeometry(QtCore.QRect(0, 0, 193, 546))
        self.right_scrollArea_widget.setObjectName("right_scrollArea_widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.right_scrollArea_widget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.right_scrollArea.setWidget(self.right_scrollArea_widget)
        self.verticalLayout_2.addWidget(self.right_scrollArea)
        self.centralhorizontallayout.addWidget(self.right_widget_2)
        self.gridLayout_2.addLayout(self.centralhorizontallayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInsert = QtWidgets.QMenu(self.menubar)
        self.menuInsert.setObjectName("menuInsert")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setCheckable(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../PycharmProjects/DesktopApplication/res/images/icons/openproject.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Project.setIcon(icon)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../PycharmProjects/DesktopApplication/res/images/icons/newproject.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Project.setIcon(icon1)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../PycharmProjects/DesktopApplication/res/images/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setIcon(icon2)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionAdd_Data = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../PycharmProjects/DesktopApplication/res/images/icons/insertdataset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Data.setIcon(icon3)
        self.actionAdd_Data.setObjectName("actionAdd_Data")
        self.actionZoom = QtWidgets.QAction(MainWindow)
        self.actionZoom.setObjectName("actionZoom")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionExport_Graph = QtWidgets.QAction(MainWindow)
        self.actionExport_Graph.setObjectName("actionExport_Graph")
        self.actionExport_Data = QtWidgets.QAction(MainWindow)
        self.actionExport_Data.setObjectName("actionExport_Data")
        self.actionExit_Application = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../PycharmProjects/DesktopApplication/res/images/icons/exitapplication.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit_Application.setIcon(icon4)
        self.actionExit_Application.setObjectName("actionExit_Application")
        self.actionDownload_data = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../../PycharmProjects/DesktopApplication/res/images/icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownload_data.setIcon(icon5)
        self.actionDownload_data.setObjectName("actionDownload_data")
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuInsert.addAction(self.actionAdd_Data)
        self.menuWindow.addAction(self.actionExit_Application)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInsert.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.toolBar.addAction(self.actionNew_Project)
        self.toolBar.addAction(self.actionOpen_Project)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_Data)
        self.toolBar.addAction(self.actionDownload_data)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit_Application)

        self.retranslateUi(MainWindow)
        self.setUpVariables()
        self.InitWindow()

        self.Test()


        self.Events()

        self.fig.canvas.mpl_connect("motion_notify_event", self.hover)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DataSetLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Data Set(s)</span></p></body></html>"))
        self.DataSet1.setText(_translate("MainWindow", "DataSet1"))
        self.DataSet2.setText(_translate("MainWindow", "DataSet2"))
        self.TransformLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Transform</span></p></body></html>"))
        self.Line_Graphs_Overlayed.setText(_translate("MainWindow", "Line Graphs(overlayed)"))
        self.Line_Graphs_Normalized.setText(_translate("MainWindow", "Line Graphs(Normalized)"))
        self.ChannelLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Channels</span></p></body></html>"))
        self.EDA.setText(_translate("MainWindow", "EDA"))
        self.ECG.setText(_translate("MainWindow", "ECG"))
        self.RSP.setText(_translate("MainWindow", "RSP"))
        self.PPG.setText(_translate("MainWindow", "PPG"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuInsert.setTitle(_translate("MainWindow", "Insert"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionAdd_Data.setText(_translate("MainWindow", "Add Data Set(s)"))
        self.actionZoom.setText(_translate("MainWindow", "Zoom"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionExport_Graph.setText(_translate("MainWindow", "Export Graph"))
        self.actionExport_Data.setText(_translate("MainWindow", "Export Data"))
        self.actionExit_Application.setText(_translate("MainWindow", "Exit Application"))
        self.actionDownload_data.setText(_translate("MainWindow", "Download data"))





    def InitWindow(self):

        self.EDA.setChecked(False)
        self.ECG.setChecked(False)
        self.RSP.setChecked(False)
        self.PPG.setChecked(False)

        self.verticalLayout_7.addWidget(self.FirgureCanvas)
        self.verticalLayout_7.addWidget(self.Navtoolbar)

        self.EDA.setEnabled(False)
        self.ECG.setEnabled(False)
        self.PPG.setEnabled(False)
        self.RSP.setEnabled(False)

        self.Line_Graphs_Normalized.setEnabled(False)
        self.Line_Graphs_Overlayed.setEnabled(False)

    def setUpVariables(self):

        self.dataSetArray = []  ## array that will store the datasets

        self.CurrentDataSet = None ## Current dataset

        ## For the tooltip on the plot array
        self.ANNOTS = []
        self.LINE_DIC = []
        self.ANNOTS_DIC = []
        self.AXISET = []
        self.LINES = []
        self.Channellabels = []

        self.RadioButtonsArray= [] ## Will store the radio buttons used in the window

        self.numDataSet = 2 ## Number of data sets



        #### Initialising the plot area ####
        self.fig = plt.figure(figsize=(50, 50))
        self.FirgureCanvas = FigureCanvas(self.fig)
        ## Intialise Navigation toolbar
        self.NavtoolWidget = QWidget()
        self.Navtoolbar = NavigationToolbar(self.FirgureCanvas, self.NavtoolWidget)

        self.HOVER = False ## Activate tooltip

        self.ax1EDA = None
        self.ax2ECG = None
        self.ax3PPG = None
        self.ax4RSP = None

        self.subPlot = plt.subplot(1, 1, 1)


    def hover(self,event):

        if(self.HOVER==True):

            if event.inaxes in self.AXISET:
                for ax in self.AXISET:
                    cont, ind = self.LINE_DIC[ax].contains(event)
                    annot = self.ANNOTS_DIC[ax]
                    if cont:
                        self.update_annot(self.LINE_DIC[ax], annot, ind,self.getChannelDescription(ax))
                        annot.set_visible(True)
                        self.fig.canvas.draw_idle()
                    else:
                        if annot.get_visible():
                            annot.set_visible(False)
                            self.fig.canvas.draw_idle()


    def refresh(self):

        self.fig.canvas.draw_idle()

    def getChannelDescription(self,axis):

        if axis == self.ax1EDA:
            return "EDA"

        if axis == self.ax2ECG:
            return "ECG"

        if axis == self.ax3PPG:
            return "PPG"

        if axis == self.ax4RSP:
            return "RSP"

    def renderLineGraphs(self,dataSet):

        self.HOVER = False
        plt.clf()

        self.subPlot = plt.subplot(1, 1, 1)




        if dataSet != None:

            plt.title('Physiological data', fontsize=10)
            plt.xlabel('Time in microsecond', fontsize=10)
            plt.ylabel('Magnitude', fontsize=10)


            self.InitLinePlotData()

            if self.Line_Graphs_Overlayed.isChecked()==True:

                self.HOVER=True


                if self.EDA.isChecked() == True:
                    self.ax1EDA = self.subPlot.twinx()

                    self.LineEDA, = self.ax1EDA.plot(np.array(dataSet.getTime()), np.array(dataSet.getNormEDA()),
                                                     color='blue')

                    self.ax1EDA.set_ylim(min(dataSet.getNormEDA()), max(dataSet.getNormEDA()))

                    self.LineEDA.set_label('EDA')
                    self.LINES.append(self.LineEDA)
                    self.AXISET.append(self.ax1EDA)
                    text = "EDA"
                    self.Channellabels.append(text)


                if self.ECG.isChecked() == True:
                    self.ax2ECG = self.subPlot.twinx()# ECG
                    self.LineECG, = self.ax2ECG.plot(np.array(dataSet.getTime()), np.array(dataSet.getNormECG()),
                                                     color="red")

                    self.ax2ECG.set_ylim(min(dataSet.getNormECG()), max(dataSet.getNormECG()))

                    self.LineECG.set_label('ECG')
                   # self.ax2ECG.tick_params(axis='y', labelcolor='red')
                    self.LINES.append(self.LineECG)
                    self.AXISET.append(self.ax2ECG)
                    text = "ECG"
                    self.Channellabels.append(text)

                if self.PPG.isChecked() == True:

                    self.ax3PPG = self.subPlot.twinx().twiny() # PPG

                    self.LinePPG, = self.ax3PPG.plot(np.array(dataSet.getTime()), np.array(dataSet.getNormPPG()),
                                                     color="purple")

                    self.ax3PPG.set_ylim(min(dataSet.getNormPPG()), max(dataSet.getNormPPG()))

                    self.LinePPG.set_label('PPG')
                    #self.ax3PPG.tick_params(axis='y', labelcolor='purple')
                    self.LINES.append(self.LinePPG)
                    self.AXISET.append(self.ax3PPG)
                    text = "PPG"
                    self.Channellabels.append(text)


                if self.RSP.isChecked() == True:
                    self.ax4RSP = self.subPlot.twinx() # RSP

                    self.LineRSP, = self.ax4RSP.plot(np.array(dataSet.getTime()), np.array(dataSet.getNormRSP()),
                                                     color="orange")

                    self.ax4RSP.set_ylim(min(dataSet.getNormRSP()), max(dataSet.getNormRSP()))

                    self.LineRSP.set_label('RSP')
                   # self.ax4RSP.tick_params(axis='y', labelcolor='orange')
                    self.LINES.append(self.LineRSP)
                    self.AXISET.append(self.ax4RSP)
                    text = "RSP"
                    self.Channellabels.append(text)

                if self.LINES != [] and self.Channellabels != []:
                    plt.legend(self.LINES, self.Channellabels)

                for ax in self.AXISET:
                    annot = self.subPlot.annotate("", xy=(0, 0), xytext=(0, 0), textcoords="offset points",
                                                  bbox=dict(boxstyle="round", fc="w", alpha=0.4),
                                                  arrowprops=dict(arrowstyle="->"))
                    annot.set_visible(False)

                    self.ANNOTS.append(annot)

                self.ANNOTS_DIC = dict(zip(self.AXISET, self.ANNOTS))

                self.LINE_DIC = dict(zip(self.AXISET, self.LINES))

                ##plt.yticks(np.arange(dataSet.getMin(),dataSet.getMax(),0.1))

                #output = output_start + ((output_end - output_start) / (input_end - input_start)) * (input - input_start)


                self.subPlot.set_ylim(-1,dataSet.getNormMax()+1)


                self.refresh()


            elif self.Line_Graphs_Normalized.isChecked() == True:

                plt.title('Channel(s) vs Time', fontsize=10)
                plt.xlabel('Time', fontsize=10)
                plt.ylabel('Volts', fontsize=10)

                self.HOVER=True

                if self.EDA.isChecked() == True:
                    self.ax1EDA = self.subPlot  # EDA
                    self.LineEDA, = self.ax1EDA.plot(np.array(dataSet.getTime()), np.array(dataSet.getNormEDA()),
                                                     color='blue')
                    self.LineEDA.set_label('EDA')
                    self.LINES.append(self.LineEDA)
                    self.AXISET.append(self.ax1EDA)
                    text = "EDA"
                    self.Channellabels.append(text)

                if self.ECG.isChecked() == True:
                    self.ax2ECG = self.subPlot  # ECG
                    self.LineECG, = self.ax2ECG.plot(np.array(dataSet.getTime()), np.array(dataSet.getNormECG()),
                                                     color="red")
                    self.ax2ECG.tick_params(axis='y', labelcolor='red')
                    self.LineECG.set_label('ECG')
                    self.LINES.append(self.LineECG)
                    self.AXISET.append(self.ax2ECG)
                    text = "ECG"
                    self.Channellabels.append(text)

                if self.PPG.isChecked() == True:
                    self.ax3PPG = self.subPlot  # PPG
                    self.LinePPG, = self.ax3PPG.plot(np.array(dataSet.getTime()), np.array(dataSet.getNormPPG()),
                                                     color="purple")
                    self.ax3PPG.tick_params(axis='y', labelcolor='purple')
                    self.LinePPG.set_label('PPG')
                    self.LINES.append(self.LinePPG)
                    self.AXISET.append(self.ax3PPG)
                    text = "PPG"
                    self.Channellabels.append(text)

                if self.RSP.isChecked() == True:
                    self.ax4RSP = self.subPlot  # RSP
                    self.LineRSP, = self.ax4RSP.plot(np.array(dataSet.getTime()), np.array(dataSet.getNormRSP()),
                                                     color="orange")
                    self.ax4RSP.tick_params(axis='y', labelcolor='orange')
                    self.LineRSP.set_label('RSP')
                    self.LINES.append(self.LineRSP)
                    self.AXISET.append(self.ax4RSP)
                    text = "RSP"
                    self.Channellabels.append(text)

                if self.LINES != [] and self.Channellabels != []:
                    plt.legend(self.LINES, self.Channellabels)

                for ax in self.AXISET:
                    annot = self.subPlot.annotate("", xy=(0, 0), xytext=(0, 0), textcoords="offset points",
                                                  bbox=dict(boxstyle="round", fc="w", alpha=0.4),
                                                  arrowprops=dict(arrowstyle="->"))
                    annot.set_visible(False)

                    self.ANNOTS.append(annot)

                self.ANNOTS_DIC = dict(zip(self.AXISET, self.ANNOTS))

                self.LINE_DIC = dict(zip(self.AXISET, self.LINES))

                self.refresh()


        else:
            self.EDA.setEnabled(False)
            self.ECG.setEnabled(False)
            self.PPG.setEnabled(False)
            self.RSP.setEnabled(False)


    def update_annot(self,line, annot, ind,label):
        x, y = line.get_data()

        if(label=="EDA"):
            yvalue  =  self.mapData(-1,2,min(self.CurrentDataSet.getNormEDA()),max(self.CurrentDataSet.getNormEDA()),y[ind["ind"][0]])

        if (label == "ECG"):
            yvalue = self.mapData(-1, 2, min(self.CurrentDataSet.getNormECG()), max(self.CurrentDataSet.getNormECG()),
                                  y[ind["ind"][0]])

        annot.xy = (x[ind["ind"][0]],yvalue )
        text =label+"\n"+"x = {}\ny= {}".format(x[ind["ind"][0]], y[ind["ind"][0]])
        annot.set_text(text)



    def Test(self):

        self.TIME = np.sort(np.random.rand(100)) ## constant  for all datasets


        ###Example###

        eda1 = np.sort(np.random.rand(100))
        eda2 = np.sort(np.random.rand(100))
        ppg1 = np.sort(np.random.rand(100))
        ppg2 = np.sort(np.random.rand(100))
        ecg1 = np.sort(np.random.rand(100))
        ecg2 = np.sort(np.random.rand(100))
        rsp1 = np.sort(np.random.rand(100))
        rsp2 = np.sort(np.random.rand(100))

        dataset1 = DataSet(self.TIME,eda1, ecg1, rsp1, ppg1, self.DataSet1)

        dataset2 = DataSet(self.TIME,eda2, ecg2, rsp2, ppg2, self.DataSet2)

        self.dataSetArray = [dataset1, dataset2]




    def Events(self):

        self.PPG.stateChanged.connect(lambda: self.renderLineGraphs(self.CurrentDataSet))
        self.ECG.stateChanged.connect(lambda: self.renderLineGraphs(self.CurrentDataSet))
        self.RSP.stateChanged.connect(lambda: self.renderLineGraphs(self.CurrentDataSet))
        self.EDA.stateChanged.connect(lambda: self.renderLineGraphs(self.CurrentDataSet))

        self.DataSet1.toggled.connect(lambda: self.dataSetAction(self.dataSetArray[0]))
        self.DataSet2.toggled.connect(lambda: self.dataSetAction(self.dataSetArray[1]))

        self.Line_Graphs_Normalized.toggled.connect(lambda: self.renderLineGraphs(self.CurrentDataSet))
        self.Line_Graphs_Overlayed.toggled.connect(lambda: self.renderLineGraphs(self.CurrentDataSet))

        self.actionAdd_Data.triggered.connect(self.file_open)


    def dataSetAction(self,dataSet):

        self.CurrentDataSet = dataSet

        self.Line_Graphs_Normalized.setEnabled(True)
        self.Line_Graphs_Overlayed.setEnabled(True)


    def InitLinePlotData(self):

        self.EDA.setEnabled(True)
        self.ECG.setEnabled(True)
        self.PPG.setEnabled(True)
        self.RSP.setEnabled(True)


        self.ANNOTS.clear()
        self.LINE_DIC.clear()
        self.ANNOTS_DIC.clear()
        self.AXISET.clear()
        self.LINES.clear()
        self.Channellabels = []



    def setMainDataSet(self,dataSet):

        self.INUSEDATASET=dataSet

        self.RenderPlots(dataSet)


    def file_open(self):

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Open File")

        self.read_data(filename)

    def read_data(self, filename):

        eda = []
        ecg = []
        rsp = []
        ppg = []

        time = []

        wb = xlrd.open_workbook(filename)
        sheet = wb.sheet_by_index(0)

        for i in range(sheet.ncols):
            for j in range(sheet.nrows):

                if i == 0:
                    time.append(sheet.cell_value(j, i))

                if i == 1:
                    ppg.append(sheet.cell_value(j, i))

                if i == 2:
                    rsp.append(sheet.cell_value(j, i))

                if i == 3:
                    eda.append(sheet.cell_value(j, i))

                if i == 4:
                    ecg.append(sheet.cell_value(j, i))

        self.createButton(eda, ecg, rsp, ppg, time)

    def createButton(self, eda, ecg, rsp, ppg, time):

        _translate = QtCore.QCoreApplication.translate
        name = "DataSet" + str(self.numDataSet + 1)
        self.numDataSet = self.numDataSet + 1;

        radiobutton = QtWidgets.QRadioButton(self.left_left_scrollarea_widget)
        radiobutton.setObjectName(name)
        radiobutton.setText(_translate("MainWindow", name))
        self.verticalLayout_3.addWidget(radiobutton)

        self.verticalLayout_3.addWidget(self.LineBreakerDataSet, 0, QtCore.Qt.AlignBottom)

        dataset = DataSet(time, eda, ecg, rsp, ppg, radiobutton)
        radiobutton.toggled.connect(lambda: self.dataSetAction(dataset))

        self.RadioButtonsArray.append(radiobutton)
        self.dataSetArray.append(dataset)

    def mapData(self,output_start,output_end,input_start,input_end,input):

        output = output_start + ((output_end - output_start) / (input_end - input_start)) * (input - input_start)

        return output




# output = output_start + ((output_end - output_start) / (input_end - input_start)) * (input - input_start)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
