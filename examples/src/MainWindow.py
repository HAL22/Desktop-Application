# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/thethelafaltein/Desktop/University/Research/DesktopApplication.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np; np.random.seed(1)


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
        self.left_left_scrollarea_widget.setGeometry(QtCore.QRect(0, 0, 124, 544))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_left_scrollarea_widget.sizePolicy().hasHeightForWidth())
        self.left_left_scrollarea_widget.setSizePolicy(sizePolicy)
        self.left_left_scrollarea_widget.setObjectName("left_left_scrollarea_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_left_scrollarea_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.left_left_scrollarea_widget)
        self.label.setMaximumSize(QtCore.QSize(80, 40))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.datasetInfo = QtWidgets.QLabel(self.left_left_scrollarea_widget)
        self.datasetInfo.setObjectName("datasetInfo")
        self.verticalLayout_3.addWidget(self.datasetInfo, 0, QtCore.Qt.AlignBottom)
        self.left_left_scrollArea.setWidget(self.left_left_scrollarea_widget)
        self.left_main_horizontallayout.addWidget(self.left_left_scrollArea)
        self.left_right_scrollArea = QtWidgets.QScrollArea(self.left_widget)
        self.left_right_scrollArea.setWidgetResizable(True)
        self.left_right_scrollArea.setObjectName("left_right_scrollArea")
        self.left_right_scrollarea_widget = QtWidgets.QWidget()
        self.left_right_scrollarea_widget.setGeometry(QtCore.QRect(0, 0, 123, 544))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_right_scrollarea_widget.sizePolicy().hasHeightForWidth())
        self.left_right_scrollarea_widget.setSizePolicy(sizePolicy)
        self.left_right_scrollarea_widget.setObjectName("left_right_scrollarea_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.left_right_scrollarea_widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.Channels = QtWidgets.QLabel(self.left_right_scrollarea_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Channels.sizePolicy().hasHeightForWidth())
        self.Channels.setSizePolicy(sizePolicy)
        self.Channels.setMinimumSize(QtCore.QSize(0, 65))
        self.Channels.setMaximumSize(QtCore.QSize(83, 65))
        self.Channels.setSizeIncrement(QtCore.QSize(0, 0))
        self.Channels.setBaseSize(QtCore.QSize(0, 0))
        self.Channels.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Channels.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Channels.setLineWidth(2)
        self.Channels.setMidLineWidth(1)
        self.Channels.setScaledContents(False)
        self.Channels.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Channels.setWordWrap(False)
        self.Channels.setIndent(0)
        self.Channels.setObjectName("Channels")
        self.verticalLayout_5.addWidget(self.Channels)
        self.EDA = QtWidgets.QCheckBox(self.left_right_scrollarea_widget)
        self.EDA.setIconSize(QtCore.QSize(16, 16))
        self.EDA.setChecked(True)
        self.EDA.setTristate(False)
        self.EDA.setObjectName("EDA")

        self.EDA.stateChanged.connect(self.checkmarkers)
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
        self.ChannelsInfo = QtWidgets.QLabel(self.left_right_scrollarea_widget)
        self.ChannelsInfo.setObjectName("ChannelsInfo")
        self.verticalLayout_5.addWidget(self.ChannelsInfo, 0, QtCore.Qt.AlignBottom)
        self.left_right_scrollArea.setWidget(self.left_right_scrollarea_widget)
        self.left_main_horizontallayout.addWidget(self.left_right_scrollArea)
        self.horizontalLayout_5.addLayout(self.left_main_horizontallayout)
        self.centralhorizontallayout.addWidget(self.left_widget)
        self.right_widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.right_widget_2.setObjectName("right_widget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.right_widget_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.right_scrollArea = QtWidgets.QScrollArea(self.right_widget_2)
        self.right_scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.right_scrollArea.setWidgetResizable(True)
        self.right_scrollArea.setObjectName("right_scrollArea")
        self.right_scrollArea_widget = QtWidgets.QWidget()
        self.right_scrollArea_widget.setGeometry(QtCore.QRect(0, 0, 261, 546))
        self.right_scrollArea_widget.setObjectName("right_scrollArea_widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.right_scrollArea_widget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.right_scrollArea.setWidget(self.right_scrollArea_widget)
        self.horizontalLayout_7.addWidget(self.right_scrollArea)
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
        self.menuWindow.addAction(self.actionZoom)
        self.menuWindow.addAction(self.actionMinimize)
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


        self.x = np.sort(np.random.rand(15))
        self.y = np.sort(np.random.rand(15))
        self.y2 = np.sort(np.random.rand(15))

        self.fig = plt.figure()
        self.ax1 = plt.subplot(2, 2, 1)
        self.line1, = plt.plot(self.x, self.y)
        self.ax1.grid(True)

        self.ax2 = self.ax1.twinx()
        self.line2, = self.ax2.plot(self.x, self.y2, color='green')
        self.ax2.tick_params(axis='y', labelcolor='green')

        self.annots = []
        for ax in [self.ax1, self.ax2]:
            annot = self.ax1.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",
                                 bbox=dict(boxstyle="round", fc="w", alpha=0.4),
                                 arrowprops=dict(arrowstyle="->"))
            annot.set_visible(False)
            self.annots.append(annot)

        self.annot_dic = dict(zip([self.ax1, self.ax2], self.annots))
        self.line_dic = dict(zip([self.ax1, self.ax2], [self.line1, self.line2]))

        def update_annot(line, annot, ind):
            x, y = line.get_data()
            annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
            text = "x = {}\ny= {}".format(x[ind["ind"][0]], y[ind["ind"][0]])
            annot.set_text(text)

        def hover(event):

            if event.inaxes in [self.ax1, self.ax2]:
                for ax in [self.ax1, self.ax2]:
                    cont, ind = self.line_dic[ax].contains(event)
                    annot = self.annot_dic[ax]
                    if cont:
                        update_annot(self.line_dic[ax], annot, ind)
                        annot.set_visible(True)
                        self.fig.canvas.draw_idle()
                    else:
                        if annot.get_visible():
                            annot.set_visible(False)
                            self.fig.canvas.draw_idle()





        self.wid=FigureCanvas(self.fig)



        self.verticalLayout_7.addWidget(self.wid)

        self.fig.canvas.draw_idle()

        self.fig.canvas.mpl_connect("motion_notify_event", hover)

        self.retranslateUi(MainWindow)


        self.checkmarkers()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Data Set(s)</span></p></body></html>"))
        self.datasetInfo.setText(_translate("MainWindow", "datasetinfo"))
        self.Channels.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Channels</span></p></body></html>"))
        self.EDA.setText(_translate("MainWindow", "EDA"))
        self.ECG.setText(_translate("MainWindow", "ECG"))
        self.RSP.setText(_translate("MainWindow", "RSP"))
        self.PPG.setText(_translate("MainWindow", "PPG"))
        self.ChannelsInfo.setText(_translate("MainWindow", "ChannelInfo"))
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



    def checkmarkers(self):
        if(self.EDA.checkState()==0):
           self.datasetInfo.setText("Fucks")
        else:
            self.datasetInfo.setText("datasetInfo")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
