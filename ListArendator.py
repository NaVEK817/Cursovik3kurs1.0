# Form implementation generated from reading ui file 'list_arendator_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cписок арендаторов"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id_tenant"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "surname"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "midle_name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "pasp_ser"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "pasp_numb"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "franchise_tenat_id"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "menedger_tenat_id"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "INN"))
