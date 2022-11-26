# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'handwriting.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 692)
        icon = QIcon()
        icon.addFile(u":/icon/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget#configWidget {\n"
"	border:1px solid rgb(122, 122, 122);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(8, 0, 6, 5)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.titleWidget = QWidget(self.widget)
        self.titleWidget.setObjectName(u"titleWidget")
        self.horizontalLayout_9 = QHBoxLayout(self.titleWidget)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.titleWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(23, 23))
        self.label_3.setStyleSheet(u"border-image: url(:/icon/icons/icon.png);")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.horizontalSpacer_8 = QSpacerItem(13, 13, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.label_4 = QLabel(self.titleWidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_4)

        self.horizontalSpacer_11 = QSpacerItem(18, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.helpPushButton = QPushButton(self.titleWidget)
        self.helpPushButton.setObjectName(u"helpPushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.helpPushButton.sizePolicy().hasHeightForWidth())
        self.helpPushButton.setSizePolicy(sizePolicy1)
        self.helpPushButton.setMinimumSize(QSize(47, 28))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(9)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.helpPushButton.setFont(font1)

        self.horizontalLayout_9.addWidget(self.helpPushButton)

        self.horizontalSpacer_9 = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.setPushButton = QPushButton(self.titleWidget)
        self.setPushButton.setObjectName(u"setPushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.setPushButton.sizePolicy().hasHeightForWidth())
        self.setPushButton.setSizePolicy(sizePolicy2)
        self.setPushButton.setMinimumSize(QSize(0, 28))
        self.setPushButton.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.setPushButton)

        self.horizontalSpacer_10 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.minPushButton = QPushButton(self.titleWidget)
        self.minPushButton.setObjectName(u"minPushButton")
        sizePolicy1.setHeightForWidth(self.minPushButton.sizePolicy().hasHeightForWidth())
        self.minPushButton.setSizePolicy(sizePolicy1)
        self.minPushButton.setMinimumSize(QSize(47, 28))
        self.minPushButton.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.minPushButton)

        self.maxPushButton = QPushButton(self.titleWidget)
        self.maxPushButton.setObjectName(u"maxPushButton")
        sizePolicy1.setHeightForWidth(self.maxPushButton.sizePolicy().hasHeightForWidth())
        self.maxPushButton.setSizePolicy(sizePolicy1)
        self.maxPushButton.setMinimumSize(QSize(47, 28))
        self.maxPushButton.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.maxPushButton)

        self.closePushButton = QPushButton(self.titleWidget)
        self.closePushButton.setObjectName(u"closePushButton")
        sizePolicy1.setHeightForWidth(self.closePushButton.sizePolicy().hasHeightForWidth())
        self.closePushButton.setSizePolicy(sizePolicy1)
        self.closePushButton.setMinimumSize(QSize(47, 28))
        self.closePushButton.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.closePushButton)


        self.verticalLayout_8.addWidget(self.titleWidget)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_8)

        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_8)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plainTextEdit = QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumBlockCount(0)

        self.verticalLayout_2.addWidget(self.plainTextEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fileLineEdit = QLineEdit(self.widget)
        self.fileLineEdit.setObjectName(u"fileLineEdit")
        self.fileLineEdit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.fileLineEdit)

        self.filePushButton = QPushButton(self.widget)
        self.filePushButton.setObjectName(u"filePushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.filePushButton.sizePolicy().hasHeightForWidth())
        self.filePushButton.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(10)
        self.filePushButton.setFont(font2)

        self.horizontalLayout.addWidget(self.filePushButton)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bgLineEdit = QLineEdit(self.widget)
        self.bgLineEdit.setObjectName(u"bgLineEdit")

        self.horizontalLayout_2.addWidget(self.bgLineEdit)

        self.bgPushButton = QPushButton(self.widget)
        self.bgPushButton.setObjectName(u"bgPushButton")
        sizePolicy3.setHeightForWidth(self.bgPushButton.sizePolicy().hasHeightForWidth())
        self.bgPushButton.setSizePolicy(sizePolicy3)
        self.bgPushButton.setFont(font2)

        self.horizontalLayout_2.addWidget(self.bgPushButton)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fontLineEdit = QLineEdit(self.widget)
        self.fontLineEdit.setObjectName(u"fontLineEdit")

        self.horizontalLayout_3.addWidget(self.fontLineEdit)

        self.fontPushButton = QPushButton(self.widget)
        self.fontPushButton.setObjectName(u"fontPushButton")
        sizePolicy3.setHeightForWidth(self.fontPushButton.sizePolicy().hasHeightForWidth())
        self.fontPushButton.setSizePolicy(sizePolicy3)
        self.fontPushButton.setFont(font2)

        self.horizontalLayout_3.addWidget(self.fontPushButton)

        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.configWidget = QWidget(self.widget)
        self.configWidget.setObjectName(u"configWidget")
        self.configWidget.setFocusPolicy(Qt.NoFocus)
        self.configWidget.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.configWidget)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.configWidget)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_14 = QLabel(self.configWidget)
        self.label_14.setObjectName(u"label_14")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_14.setFont(font4)

        self.gridLayout.addWidget(self.label_14, 8, 1, 1, 1)

        self.label_10 = QLabel(self.configWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 1)

        self.verDoubleSpinBox = QDoubleSpinBox(self.configWidget)
        self.verDoubleSpinBox.setObjectName(u"verDoubleSpinBox")
        font5 = QFont()
        font5.setPointSize(11)
        self.verDoubleSpinBox.setFont(font5)
        self.verDoubleSpinBox.setMaximum(99.000000000000000)
        self.verDoubleSpinBox.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.verDoubleSpinBox, 6, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.label_8 = QLabel(self.configWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)

        self.colorPushButton = QPushButton(self.configWidget)
        self.colorPushButton.setObjectName(u"colorPushButton")

        self.gridLayout.addWidget(self.colorPushButton, 0, 3, 1, 1)

        self.label_16 = QLabel(self.configWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font4)

        self.gridLayout.addWidget(self.label_16, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 2, 1, 1)

        self.horDoubleSpinBox = QDoubleSpinBox(self.configWidget)
        self.horDoubleSpinBox.setObjectName(u"horDoubleSpinBox")
        self.horDoubleSpinBox.setFont(font5)
        self.horDoubleSpinBox.setMinimum(0.000000000000000)
        self.horDoubleSpinBox.setMaximum(99.000000000000000)
        self.horDoubleSpinBox.setSingleStep(0.100000000000000)
        self.horDoubleSpinBox.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.horDoubleSpinBox, 5, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 4, 1, 1)

        self.label_15 = QLabel(self.configWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)

        self.gridLayout.addWidget(self.label_15, 9, 1, 1, 1)

        self.rHorDoubleSpinBox = QDoubleSpinBox(self.configWidget)
        self.rHorDoubleSpinBox.setObjectName(u"rHorDoubleSpinBox")
        self.rHorDoubleSpinBox.setFont(font5)
        self.rHorDoubleSpinBox.setMaximum(99.000000000000000)
        self.rHorDoubleSpinBox.setSingleStep(0.100000000000000)
        self.rHorDoubleSpinBox.setValue(4.000000000000000)

        self.gridLayout.addWidget(self.rHorDoubleSpinBox, 7, 3, 1, 1)

        self.sizeDoubleSpinBox = QDoubleSpinBox(self.configWidget)
        self.sizeDoubleSpinBox.setObjectName(u"sizeDoubleSpinBox")
        self.sizeDoubleSpinBox.setFont(font5)
        self.sizeDoubleSpinBox.setMinimum(0.000000000000000)
        self.sizeDoubleSpinBox.setMaximum(99.000000000000000)
        self.sizeDoubleSpinBox.setSingleStep(0.100000000000000)
        self.sizeDoubleSpinBox.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.sizeDoubleSpinBox, 4, 3, 1, 1)

        self.label_17 = QLabel(self.configWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font4)

        self.gridLayout.addWidget(self.label_17, 2, 1, 1, 1)

        self.label_9 = QLabel(self.configWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_4, 10, 1, 1, 1)

        self.rRotatedoubleSpinBox = QDoubleSpinBox(self.configWidget)
        self.rRotatedoubleSpinBox.setObjectName(u"rRotatedoubleSpinBox")
        self.rRotatedoubleSpinBox.setFont(font5)
        self.rRotatedoubleSpinBox.setMaximum(99.000000000000000)
        self.rRotatedoubleSpinBox.setSingleStep(0.010000000000000)
        self.rRotatedoubleSpinBox.setValue(0.050000000000000)

        self.gridLayout.addWidget(self.rRotatedoubleSpinBox, 9, 3, 1, 1)

        self.rVerDoubleSpinBox = QDoubleSpinBox(self.configWidget)
        self.rVerDoubleSpinBox.setObjectName(u"rVerDoubleSpinBox")
        self.rVerDoubleSpinBox.setFont(font5)
        self.rVerDoubleSpinBox.setMaximum(99.000000000000000)
        self.rVerDoubleSpinBox.setSingleStep(0.100000000000000)
        self.rVerDoubleSpinBox.setValue(4.000000000000000)

        self.gridLayout.addWidget(self.rVerDoubleSpinBox, 8, 3, 1, 1)

        self.label_7 = QLabel(self.configWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)

        self.horizontalSpinBox = QSpinBox(self.configWidget)
        self.horizontalSpinBox.setObjectName(u"horizontalSpinBox")
        self.horizontalSpinBox.setFont(font5)
        self.horizontalSpinBox.setMaximum(999)

        self.gridLayout.addWidget(self.horizontalSpinBox, 2, 3, 1, 1)

        self.verticalSpinBox = QSpinBox(self.configWidget)
        self.verticalSpinBox.setObjectName(u"verticalSpinBox")
        self.verticalSpinBox.setFont(font5)
        self.verticalSpinBox.setMaximum(999)

        self.gridLayout.addWidget(self.verticalSpinBox, 3, 3, 1, 1)

        self.label_12 = QLabel(self.configWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.gridLayout.addWidget(self.label_12, 7, 1, 1, 1)

        self.label_5 = QLabel(self.configWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.sizeSpinBox = QSpinBox(self.configWidget)
        self.sizeSpinBox.setObjectName(u"sizeSpinBox")
        self.sizeSpinBox.setFont(font5)
        self.sizeSpinBox.setMinimum(1)
        self.sizeSpinBox.setMaximum(999)
        self.sizeSpinBox.setValue(100)

        self.gridLayout.addWidget(self.sizeSpinBox, 1, 3, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.line = QFrame(self.configWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.configWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.optimizeCheckBox = QCheckBox(self.configWidget)
        self.optimizeCheckBox.setObjectName(u"optimizeCheckBox")
        sizePolicy2.setHeightForWidth(self.optimizeCheckBox.sizePolicy().hasHeightForWidth())
        self.optimizeCheckBox.setSizePolicy(sizePolicy2)
        self.optimizeCheckBox.setChecked(True)

        self.horizontalLayout_5.addWidget(self.optimizeCheckBox)

        self.vagueCheckBox = QCheckBox(self.configWidget)
        self.vagueCheckBox.setObjectName(u"vagueCheckBox")
        sizePolicy2.setHeightForWidth(self.vagueCheckBox.sizePolicy().hasHeightForWidth())
        self.vagueCheckBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.vagueCheckBox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.widget_2 = QWidget(self.configWidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.widget_2.setMinimumSize(QSize(121, 111))
        self.widget_2.setStyleSheet(u"")
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 40, 41, 31))
        font6 = QFont()
        font6.setPointSize(15)
        self.label_11.setFont(font6)
        self.leftLineEdit = QLineEdit(self.widget_2)
        self.leftLineEdit.setObjectName(u"leftLineEdit")
        self.leftLineEdit.setGeometry(QRect(0, 30, 31, 51))
        self.upLineEdit = QLineEdit(self.widget_2)
        self.upLineEdit.setObjectName(u"upLineEdit")
        self.upLineEdit.setGeometry(QRect(30, 0, 61, 31))
        self.downLineEdit = QLineEdit(self.widget_2)
        self.downLineEdit.setObjectName(u"downLineEdit")
        self.downLineEdit.setGeometry(QRect(30, 80, 61, 31))
        self.rightLineEdit = QLineEdit(self.widget_2)
        self.rightLineEdit.setObjectName(u"rightLineEdit")
        self.rightLineEdit.setGeometry(QRect(90, 30, 31, 51))

        self.horizontalLayout_4.addWidget(self.widget_2)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(2, 1)

        self.verticalLayout_6.addWidget(self.configWidget)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.previewPushButton = QPushButton(self.widget)
        self.previewPushButton.setObjectName(u"previewPushButton")
        sizePolicy2.setHeightForWidth(self.previewPushButton.sizePolicy().hasHeightForWidth())
        self.previewPushButton.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setPointSize(13)
        self.previewPushButton.setFont(font7)

        self.horizontalLayout_6.addWidget(self.previewPushButton)

        self.outputPushButton = QPushButton(self.widget)
        self.outputPushButton.setObjectName(u"outputPushButton")
        sizePolicy2.setHeightForWidth(self.outputPushButton.sizePolicy().hasHeightForWidth())
        self.outputPushButton.setSizePolicy(sizePolicy2)
        self.outputPushButton.setFont(font7)

        self.horizontalLayout_6.addWidget(self.outputPushButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)

        self.previewLabel = QLabel(self.widget)
        self.previewLabel.setObjectName(u"previewLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.previewLabel.sizePolicy().hasHeightForWidth())
        self.previewLabel.setSizePolicy(sizePolicy5)
        self.previewLabel.setMinimumSize(QSize(0, 0))
        self.previewLabel.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.previewLabel.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.previewLabel)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_8)


        self.verticalLayout_9.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u624b\u5199\u6a21\u62df\u5668", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u624b\u5199\u6a21\u62df\u5668", None))
        self.helpPushButton.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9(&H)", None))
        self.setPushButton.setText("")
        self.minPushButton.setText("")
        self.maxPushButton.setText("")
        self.closePushButton.setText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5728\u6b64\u6587\u672c\u6846\u4e2d\u8f93\u5165\u6587\u5b57\u6216\u70b9\u51fb\u9009\u62e9\u6587\u4ef6\u63d0\u53d6\u6587\u4ef6\u5185\u5bb9", None))
        self.fileLineEdit.setPlaceholderText("")
        self.filePushButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.bgPushButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u80cc\u666f", None))
        self.fontPushButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5b57\u4f53", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u4f53", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u7eb5\u5411\u504f\u79fb\u6270\u52a8", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u884c\u95f4\u8ddd\u6270\u52a8", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f\u6270\u52a8", None))
        self.colorPushButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u989c\u8272", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u884c\u95f4\u8ddd", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c\u504f\u79fb\u6270\u52a8", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u95f4\u8ddd", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u95f4\u8ddd\u6270\u52a8", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u989c\u8272", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6a2a\u5411\u504f\u79fb\u6270\u52a8", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u80cc\u666f", None))
        self.optimizeCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u7f8e\u5316*", None))
        self.vagueCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u7cca*", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u8fb9\u8ddd", None))
        self.leftLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.upLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.downLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.rightLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.previewPushButton.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.outputPushButton.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.previewLabel.setText("")
    # retranslateUi

