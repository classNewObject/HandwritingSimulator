# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(514, 304)
        icon = QIcon()
        icon.addFile(u":/icon/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(9, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.widget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.chooseDirLineEdit = QLineEdit(self.groupBox_2)
        self.chooseDirLineEdit.setObjectName(u"chooseDirLineEdit")
        self.chooseDirLineEdit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.chooseDirLineEdit)

        self.chooseDirButton = QPushButton(self.groupBox_2)
        self.chooseDirButton.setObjectName(u"chooseDirButton")

        self.horizontalLayout.addWidget(self.chooseDirButton)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.widget_3)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.chooseFileLineEdit = QLineEdit(self.groupBox)
        self.chooseFileLineEdit.setObjectName(u"chooseFileLineEdit")
        self.chooseFileLineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.chooseFileLineEdit)

        self.chooseFileButton = QPushButton(self.groupBox)
        self.chooseFileButton.setObjectName(u"chooseFileButton")

        self.horizontalLayout_2.addWidget(self.chooseFileButton)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.widget_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 2, 5, 1, 1)

        self.radioButton = QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSlider = QSlider(self.groupBox_3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setEnabled(True)
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalSlider.setMouseTracking(False)
        self.horizontalSlider.setAcceptDrops(False)
        self.horizontalSlider.setMaximum(99)
        self.horizontalSlider.setValue(10)
        self.horizontalSlider.setSliderPosition(10)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(0)

        self.horizontalLayout_4.addWidget(self.horizontalSlider)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(15, 0))

        self.horizontalLayout_4.addWidget(self.label_6)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 2, 1, 4)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.groupBox_3)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 4)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.saveCheckBox = QCheckBox(self.groupBox_3)
        self.saveCheckBox.setObjectName(u"saveCheckBox")
        self.saveCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.saveCheckBox, 2, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 2, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.gridLayout_2.addWidget(self.widget_3, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.titleWidget = QWidget(self.widget)
        self.titleWidget.setObjectName(u"titleWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleWidget.sizePolicy().hasHeightForWidth())
        self.titleWidget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_3 = QHBoxLayout(self.titleWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_7 = QLabel(self.titleWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(23, 23))
        self.label_7.setStyleSheet(u"border-image: url(:/icon/icons/icon.png);")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.titleWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.closeButton = QPushButton(self.titleWidget)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.gridLayout_2.addWidget(self.titleWidget, 0, 0, 1, 3)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa\u8def\u5f84", None))
        self.chooseDirButton.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u9884\u8bbe", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8f7d\u5165\u9884\u8bbe", None))
        self.chooseFileButton.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u5176\u4ed6", None))
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u591a\u6838\u52a0\u901f\u5904\u7406", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6a21\u7cca\u5ea6", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e3b\u9898", None))
        self.saveCheckBox.setText(QCoreApplication.translate("Form", u"\u9000\u51fa\u7a0b\u5e8f\u65f6\u63d0\u793a\u201c\u662f\u5426\u4fdd\u5b58\u4e3a\u9884\u8bbe\u201d", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.closeButton.setText("")
    # retranslateUi

