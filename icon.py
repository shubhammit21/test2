# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'icon.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(514, 396)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../../Downloads/devilmaycryion.jpg"))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-family:\'arial,sans-serif\'; font-size:medium; color:#222222; background-color:#ffffff;\"/><a name=\"fprsl\"/><a href=\"https://www.google.com/search?rlz=1C1CHBF_enIN856IN856&amp;q=http://devil-may-cry.com&amp;spell=1&amp;sa=X&amp;ved=0ahUKEwj4_fbomMHjAhVHWisKHRVDDzcQkeECCC4oAA\"><span style=\" font-family:\'arial,sans-serif\'; font-size:18px; font-weight:600; font-style:italic; text-decoration: underline; color:#660099; background-color:#ffffff;\">h</span></a><span style=\" font-family:\'arial,sans-serif\'; font-size:18px; font-weight:600; font-style:italic; text-decoration: underline; color:#660099; background-color:#ffffff;\">ttp</span><a href=\"https://www.google.com/search?rlz=1C1CHBF_enIN856IN856&amp;q=http://devil-may-cry.com&amp;spell=1&amp;sa=X&amp;ved=0ahUKEwj4_fbomMHjAhVHWisKHRVDDzcQkeECCC4oAA\"><span style=\" font-family:\'arial,sans-serif\'; font-size:18px; text-decoration: underline; color:#660099; background-color:#ffffff;\">://</span></a><a href=\"https://www.google.com/search?rlz=1C1CHBF_enIN856IN856&amp;q=http://devil-may-cry.com&amp;spell=1&amp;sa=X&amp;ved=0ahUKEwj4_fbomMHjAhVHWisKHRVDDzcQkeECCC4oAA\"><span style=\" font-family:\'arial,sans-serif\'; font-size:18px; font-weight:600; font-style:italic; text-decoration: underline; color:#660099; background-color:#ffffff;\">devil-may-cry.com</span></a></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
