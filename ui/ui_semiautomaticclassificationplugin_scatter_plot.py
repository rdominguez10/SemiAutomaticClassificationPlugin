# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_semiautomaticclassificationplugin_scatter_plot.ui'
#
# Created: Sun Mar 22 18:00:01 2015
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ScatterPlot(object):
    def setupUi(self, ScatterPlot):
        ScatterPlot.setObjectName(_fromUtf8("ScatterPlot"))
        ScatterPlot.resize(575, 445)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScatterPlot.sizePolicy().hasHeightForWidth())
        ScatterPlot.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/semiautomaticclassificationplugin/semiautomaticclassificationplugin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ScatterPlot.setWindowIcon(icon)
        self.gridLayout_6 = QtGui.QGridLayout(ScatterPlot)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_25 = QtGui.QLabel(ScatterPlot)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(_fromUtf8("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #243a4e, stop:1 rgba(0, 0, 0, 0)); color : white"))
        self.label_25.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_25.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_4.addWidget(self.label_25, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 2, 1, 1)
        self.scatter_list_plot_tableWidget = QtGui.QTableWidget(ScatterPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scatter_list_plot_tableWidget.sizePolicy().hasHeightForWidth())
        self.scatter_list_plot_tableWidget.setSizePolicy(sizePolicy)
        self.scatter_list_plot_tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.scatter_list_plot_tableWidget.setObjectName(_fromUtf8("scatter_list_plot_tableWidget"))
        self.scatter_list_plot_tableWidget.setColumnCount(6)
        self.scatter_list_plot_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.scatter_list_plot_tableWidget.setHorizontalHeaderItem(5, item)
        self.scatter_list_plot_tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.scatter_list_plot_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.scatter_list_plot_tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.gridLayout_2.addWidget(self.scatter_list_plot_tableWidget, 0, 0, 1, 1)
        self.gridLayout_32 = QtGui.QGridLayout()
        self.gridLayout_32.setObjectName(_fromUtf8("gridLayout_32"))
        self.scatter_ROI_Button = QtGui.QPushButton(ScatterPlot)
        self.scatter_ROI_Button.setObjectName(_fromUtf8("scatter_ROI_Button"))
        self.gridLayout_32.addWidget(self.scatter_ROI_Button, 2, 0, 1, 1)
        self.gridLayout_40 = QtGui.QGridLayout()
        self.gridLayout_40.setObjectName(_fromUtf8("gridLayout_40"))
        self.label_48 = QtGui.QLabel(ScatterPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        self.label_48.setFrameShape(QtGui.QFrame.Panel)
        self.label_48.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.gridLayout_40.addWidget(self.label_48, 0, 0, 1, 1)
        self.bandY_spinBox = QtGui.QSpinBox(ScatterPlot)
        self.bandY_spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.bandY_spinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bandY_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bandY_spinBox.setMinimum(1)
        self.bandY_spinBox.setMaximum(2000)
        self.bandY_spinBox.setProperty("value", 2)
        self.bandY_spinBox.setObjectName(_fromUtf8("bandY_spinBox"))
        self.gridLayout_40.addWidget(self.bandY_spinBox, 0, 1, 1, 1)
        self.gridLayout_32.addLayout(self.gridLayout_40, 1, 0, 1, 1)
        self.gridLayout_38 = QtGui.QGridLayout()
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.label_46 = QtGui.QLabel(ScatterPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        self.label_46.setFrameShape(QtGui.QFrame.Panel)
        self.label_46.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.gridLayout_38.addWidget(self.label_46, 0, 0, 1, 1)
        self.bandX_spinBox = QtGui.QSpinBox(ScatterPlot)
        self.bandX_spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.bandX_spinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bandX_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bandX_spinBox.setMinimum(1)
        self.bandX_spinBox.setMaximum(2000)
        self.bandX_spinBox.setProperty("value", 1)
        self.bandX_spinBox.setObjectName(_fromUtf8("bandX_spinBox"))
        self.gridLayout_38.addWidget(self.bandX_spinBox, 0, 1, 1, 1)
        self.gridLayout_32.addLayout(self.gridLayout_38, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_32, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.Sig_Widget_2 = SigWidget2(ScatterPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sig_Widget_2.sizePolicy().hasHeightForWidth())
        self.Sig_Widget_2.setSizePolicy(sizePolicy)
        self.Sig_Widget_2.setObjectName(_fromUtf8("Sig_Widget_2"))
        self.gridLayout_3.addWidget(self.Sig_Widget_2, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.OK_welcome_buttonBox = QtGui.QDialogButtonBox(ScatterPlot)
        self.OK_welcome_buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.OK_welcome_buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.OK_welcome_buttonBox.setObjectName(_fromUtf8("OK_welcome_buttonBox"))
        self.gridLayout.addWidget(self.OK_welcome_buttonBox, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 3, 0, 1, 1)

        self.retranslateUi(ScatterPlot)
        QtCore.QObject.connect(self.OK_welcome_buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ScatterPlot.accept)
        QtCore.QObject.connect(self.OK_welcome_buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ScatterPlot.reject)
        QtCore.QMetaObject.connectSlotsByName(ScatterPlot)

    def retranslateUi(self, ScatterPlot):
        ScatterPlot.setWindowTitle(_translate("ScatterPlot", "SCP: Scatter Plot", None))
        self.label_25.setText(_translate("ScatterPlot", " ROI list", None))
        self.scatter_list_plot_tableWidget.setSortingEnabled(True)
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ScatterPlot", "S", None))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ScatterPlot", "MC ID", None))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ScatterPlot", "MC Info", None))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ScatterPlot", "C ID", None))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ScatterPlot", "C Info", None))
        item = self.scatter_list_plot_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ScatterPlot", "Color", None))
        self.scatter_ROI_Button.setToolTip(_translate("ScatterPlot", "<html><head/><body><p>Calculate scatter plot</p></body></html>", None))
        self.scatter_ROI_Button.setText(_translate("ScatterPlot", "Calculate scatter plot", None))
        self.label_48.setText(_translate("ScatterPlot", "Band Y", None))
        self.bandY_spinBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p align=\"justify\">Band Y</p></body></html>", None))
        self.label_46.setText(_translate("ScatterPlot", "Band X", None))
        self.bandX_spinBox.setToolTip(_translate("ScatterPlot", "<html><head/><body><p align=\"justify\">Band X</p></body></html>", None))

from sigwidget2 import SigWidget2
import resources_rc
