# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(400, 200)
        self.frame = QtWidgets.QFrame(parent=LogIn)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.usernameLineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.usernameLineEdit.setGeometry(QtCore.QRect(10, 40, 181, 22))
        self.usernameLineEdit.setMouseTracking(False)
        self.usernameLineEdit.setMaxLength(25)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.Login = QtWidgets.QLabel(parent=self.frame)
        self.Login.setGeometry(QtCore.QRect(10, 0, 49, 16))
        self.Login.setObjectName("Login")
        self.Password = QtWidgets.QLabel(parent=self.frame)
        self.Password.setGeometry(QtCore.QRect(10, 80, 49, 16))
        self.Password.setObjectName("Password")
        self.passwordLineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.passwordLineEdit.setGeometry(QtCore.QRect(10, 110, 181, 22))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(self.passwordLineEdit.EchoMode.Password)
        self.errorLabel = QtWidgets.QLabel(parent=self.frame)
        self.errorLabel.setGeometry(QtCore.QRect(200, 20, 220, 101))
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.registerButton = QtWidgets.QPushButton(parent=self.frame)
        self.registerButton.setGeometry(QtCore.QRect(220, 140, 75, 24))
        self.registerButton.setObjectName("registerButton")
        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)
    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Регистрация"))
        self.Login.setText(_translate("LogIn", "Логин"))
        self.Password.setText(_translate("LogIn", "Пароль"))
        self.registerButton.setText(_translate("LogIn", "LogIn"))