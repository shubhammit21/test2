# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'line.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(408, 231)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_11.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setValidator(QtGui.QIntValidator())
        self.t1.setObjectName("t1")
        self.verticalLayout_10.addWidget(self.t1)
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setObjectName("t2")
        self.verticalLayout_10.addWidget(self.t2)
        self.t3 = QtWidgets.QLineEdit(Form)
        self.t3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.t3.setObjectName("t3")
        self.verticalLayout_10.addWidget(self.t3)
        self.t4 = QtWidgets.QLineEdit(Form)
        self.t4.setObjectName("t4")
        self.verticalLayout_10.addWidget(self.t4)
        self.t4.textChanged.connect(self.textchange)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Integ Validatorer "))
        self.label.setText(_translate("Form", "Input Mask"))
        self.label_4.setText(_translate("Form", "Password Field"))
        self.label_3.setText(_translate("Form", "Text Changed"))
        self.t2.setInputMask(_translate("Form", "+99 999 999 9999"))

    def textchange(self, text):
        if text.isalpha()==False:
            print ("non-alphabet character not allowed")
            self.t4.setText("")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
