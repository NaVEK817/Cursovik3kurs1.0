# Form implementation generated from reading ui file 'search_apartment_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(505, 472)
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 501, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 250, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(10, 270, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(120, 270, 91, 16))
        self.label_3.setObjectName("label_3")
        self.look = QtWidgets.QPushButton(parent=Form)
        self.look.setGeometry(QtCore.QRect(410, 440, 75, 24))
        self.look.setObjectName("look")
        self.min_sq = QtWidgets.QLineEdit(parent=Form)
        self.min_sq.setGeometry(QtCore.QRect(10, 300, 81, 22))
        self.min_sq.setObjectName("min_sq")
        self.max_sq = QtWidgets.QLineEdit(parent=Form)
        self.max_sq.setGeometry(QtCore.QRect(120, 300, 81, 22))
        self.max_sq.setObjectName("max_sq")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(220, 250, 271, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(330, 270, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(220, 270, 81, 16))
        self.label_6.setObjectName("label_6")
        self.min_cost = QtWidgets.QLineEdit(parent=Form)
        self.min_cost.setGeometry(QtCore.QRect(220, 300, 81, 22))
        self.min_cost.setObjectName("min_cost")
        self.max_cost = QtWidgets.QLineEdit(parent=Form)
        self.max_cost.setGeometry(QtCore.QRect(330, 300, 81, 22))
        self.max_cost.setObjectName("max_cost")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(120, 360, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(10, 360, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(10, 340, 101, 16))
        self.label_9.setObjectName("label_9")
        self.renov = QtWidgets.QComboBox(parent=Form)
        self.renov.setGeometry(QtCore.QRect(10, 380, 81, 22))
        self.renov.setObjectName("renov")
        self.renov.addItem("")
        self.renov.addItem("")
        self.communication = QtWidgets.QComboBox(parent=Form)
        self.communication.setGeometry(QtCore.QRect(120, 380, 81, 22))
        self.communication.setObjectName("communication")
        self.communication.addItem("")
        self.communication.addItem("")
        self.label_10 = QtWidgets.QLabel(parent=Form)
        self.label_10.setGeometry(QtCore.QRect(230, 360, 81, 16))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=Form)
        self.label_11.setGeometry(QtCore.QRect(230, 340, 171, 16))
        self.label_11.setObjectName("label_11")
        self.proximaty = QtWidgets.QLineEdit(parent=Form)
        self.proximaty.setGeometry(QtCore.QRect(230, 380, 113, 22))
        self.proximaty.setObjectName("proximaty")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Помещения по фильтру"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Идентификатор"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Адрес"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Арендодатель"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Номер телефона"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Метро"))
        self.label.setText(_translate("Form", "Введите диапазон площади"))
        self.label_2.setText(_translate("Form", "Минимальная"))
        self.label_3.setText(_translate("Form", "Максимальная"))
        self.look.setText(_translate("Form", "Просмотр"))
        self.label_4.setText(_translate("Form", "Введите диапазон стоимости за квадратный метр"))
        self.label_5.setText(_translate("Form", "Максимальная"))
        self.label_6.setText(_translate("Form", "Минимальная"))
        self.label_7.setText(_translate("Form", "Коммуникаций"))
        self.label_8.setText(_translate("Form", "Ремонта"))
        self.label_9.setText(_translate("Form", "Наличие:"))
        self.renov.setItemText(0, _translate("Form", "1"))
        self.renov.setItemText(1, _translate("Form", "0"))
        self.communication.setItemText(0, _translate("Form", "1"))
        self.communication.setItemText(1, _translate("Form", "1"))
        self.label_11.setText(_translate("Form", "Введите удалённость от метро"))
