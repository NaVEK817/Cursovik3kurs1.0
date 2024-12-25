import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QWidget, QLineEdit, QLabel, QTextEdit, QHBoxLayout, QVBoxLayout, QScrollArea, QSizePolicy, QGridLayout, QDialog
from PyQt5.QtCore import Qt, QSize
from logIn import Ui_LogIn
from AdminMenu import Ui_Form as Ui_AdminMenu
from Menedger import Ui_Form as Ui_Menedger
import pymysql
import pandas as pd

class Functions():
    def set_connection(self, mydb): # Метод для установки соединения
        self.mydb = mydb
    def set_username(self, username):  # Метод для установки соединения
        self.username = username
    def mydisconnect(self):
        if self.mydb: # Проверяем, установлено ли соединение
            self.mydb.close()
        else:
            pass
        self.hide()
        self.registrationwindow.show()
    def close_window(self):
        self.close()

class RegistrationWindow(QMainWindow, Ui_LogIn, Functions):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registerButton.clicked.connect(self.register)
    def open_adminwindow(self, mydb, username): # Передаем соединение
        self.hide()
        self.adminwindow.show()
        self.adminwindow.set_connection(mydb) # передаём подключение в AdminWindow
        self.adminwindow.set_username(username)
    def open_menedger(self, mydb, username):
        self.close()
        self.menedgerwindow.show()
        self.menedgerwindow.set_connection(mydb)  # передаём подключение в
        self.adminwindow.set_username(username)
    def register(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        if not username or not password:
            self.errorLabel.setText("Заполните все поля!")
            return
        try:
            mydb = pymysql.connect(
                host='localhost',
                port=3306,
                user=username,
                password=password,
                database='Kursovik'
            )
            if username == "root":
                self.open_adminwindow(mydb, username)
            if username == "menedger":
                self.open_menedger(mydb, username)
        except pymysql.err.OperationalError as e:
            self.errorLabel.setText(f"Ошибка в подключении: {e}")
        except Exception as e:
            self.errorLabel.setText(f"Произошла неизвестная ошибка: {e}")
        finally:
            self.usernameLineEdit.clear()
            self.passwordLineEdit.clear()
            self.errorLabel.setText("")

class AdminWindow(QMainWindow, Ui_AdminMenu, Functions):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mydb = None # Добавляем атрибут для хранения соединения
        self.free_req.clicked.connect(self.querry)
        self.menu_menedger.clicked.connect(self.menmenu)
        self.menu_acc.clicked.connect(self.accmenu)
        self.disconnect.clicked.connect(self.mydisconnect)
        self.list_workers.clicked.connect(self.list_workers_f)

    def list_workers_f(self):
        self.workers = Workers()
        self.workers.mydb = self.mydb
        self.workers.show()
    def querry(self):
        self.requestwindow = RequestWindow()
        self.requestwindow.mydb = self.mydb
        self.requestwindow.show()
    def menmenu(self):
        self.hide()
        self.menedgerwindow.show()
    def accmenu(self):
        pass

class RequestWindow(QWidget, Functions):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Запрос")
        self.setMinimumSize(QSize(800, 600))

        # Текстовое поле для запроса (с прокруткой)
        self.request_scroll = QScrollArea()
        self.request_field = QLineEdit()
        self.request_field.setPlaceholderText("Введите ваш запрос...")
        self.request_scroll.setWidget(self.request_field)
        self.request_scroll.setWidgetResizable(True)
        self.request_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Fixed высота

        # Поле для вывода статуса
        self.status_label = QLabel("")
        self.status_label.setWordWrap(True)
        self.status_label.setAlignment(Qt.AlignCenter)

        # Поле для вывода результата (многострочное текстовое поле с прокруткой)
        self.result_scroll = QScrollArea()
        self.result_field = QTextEdit()
        self.result_field.setReadOnly(True)
        self.result_scroll.setWidget(self.result_field)
        self.result_scroll.setWidgetResizable(True)
        self.result_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Кнопки "Отправить" и "Назад"
        self.send_button = QPushButton("Отправить")
        self.send_button.clicked.connect(self.send_request)
        self.back_button = QPushButton("Назад")
        self.back_button.clicked.connect(self.close_window)

        # Расположение элементов в окне. QVBoxLayout для вертикального расположения
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.request_scroll)  # Поле ввода сверху
        main_layout.addWidget(self.result_scroll)  # Поле вывода снизу
        main_layout.addWidget(self.status_label)
        main_layout.addLayout(self.create_button_layout())
        self.setLayout(main_layout)

    def create_button_layout(self):
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.send_button)
        button_layout.addWidget(self.back_button)
        return button_layout

    def send_request(self):
        self.result_field.clear()
        request = self.request_field.text()
        if request:
            try:
                df = pd.read_sql(request, con=self.mydb).to_string()
                self.result_field.setText(df)
                self.status_label.setText("Запрос отправлен")
            except Exception as e:
                self.status_label.setText(f"Ошибка при отправке запроса: {e}")
        else:
            self.status_label.setText("Поле запроса пустое")

class MenedgerWindow(QMainWindow, Ui_Menedger, Functions):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mydb = None # Добавляем атрибут для хранения соединения
        self.allert_arendator.clicked.connect(self.allert_arendator_f)
        self.look_metro.clicked.connect(self.look_metro_f)
        self.pushButton.clicked.connect(self.list_arendodatel_f)
        self.disconnect.clicked.connect(self.mydisconnect)
        self.delete_arendator.clicked.connect(self.delete_arendator_f)
        self.append_arendator.clicked.connect(self.append_arendator_f)
        self.update_arendator.clicked.connect(self.update_arendator_f)
        self.list_apartment.clicked.connect(self.list_apartment_f)
        self.list_arendator.clicked.connect(self.list_arendator_f)
        self.append_pact.clicked.connect(self.append_pact_f)
        self.pushButton_2.clicked.connect(self.list_dog)
    def list_dog(self):
        pass
    def allert_arendator_f(self):
        pass
    def look_metro_f(self):
        pass
    def delete_arendator_f(self):
        pass
    def update_arendator_f(self):
        pass
    def append_arendator_f(self):
        pass
    def list_apartment_f(self):
        pass
    def list_arendodatel_f(self):
        pass
    def append_pact_f(self):
        pass
    def list_arendator_f(self):
        pass

class AddWorkerDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить сотрудника")

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")

        layout = QGridLayout()

        # Поля ввода
        self.fields = {
            "Фамилия": QLineEdit(),
            "Имя": QLineEdit(),
            "Отчество": QLineEdit(),
            "Номер телефона": QLineEdit(),
            "Серия паспорта": QLineEdit(),
            "Номер паспорта": QLineEdit(),
        }

        # Добавление полей на форму
        row = 0
        for label, field in self.fields.items():
            layout.addWidget(QLabel(label + ":"), row, 0)
            layout.addWidget(field, row, 1)
            row += 1

        # Кнопки
        self.button_add = QPushButton("Добавить")
        self.button_add.clicked.connect(self.on_add)
        self.button_cancel = QPushButton("Назад")
        self.button_cancel.clicked.connect(self.reject)

        layout.addWidget(self.error_label, row, 0, 1, 2) # Вывод ошибок
        layout.addWidget(self.button_add, row + 1, 0)
        layout.addWidget(self.button_cancel, row + 1, 1)

        self.setLayout(layout)

    def on_add(self):
        errors = []
        for label, field in self.fields.items():
            if not field.text():
                errors.append(f"Поле '{label}' не заполнено.")

        if errors:
            self.error_label.setText("\n".join(errors))
            return

        # Сбор данных
        data = {label: field.text() for label, field in self.fields.items()}

        try:
            cursor = self.mydb.cursor()
            cursor.execute("SELECT MAX(id_menedger) FROM kursovik.менеджер")
            result = cursor.fetchone()
            max_id = result[0] if result[0] is not None else 0  # Обработка случая пустой таблицы
            next_id = max_id + 1
            sql = "INSERT INTO kursovik.менеджер (id_menedger, surname, name, midle_name, phone_number, pasp_ser, pasp_numb) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (
            next_id, data[0], data[1], data[2], data[3], data[4], data[5])  # Обратите внимание на f-строки убраны
            cursor.execute(sql, val)
            self.mydb.commit()
            QMessageBox.information(self, "Успех", "Данные успешно добавлены!")
            self.accept()
        except mysql.connector.Error as err:
            self.error_label.setText(f"Ошибка добавления данных: {err}")
            self.mydb.rollback()  # Очень важно откатить транзакцию при ошибке
        except Exception as e:
            self.error_label.setText(f"Ошибка добавления данных: {e}")
        finally:
            if cursor:
                cursor.close()


class Workers(QWidget, Functions):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Менеджеры")
        self.setMinimumSize(QSize(800, 600))
        self.mydb = None #Инициализируем, потом нужно подключиться

        # Текстовое поле для вывода списка
        self.list_output = QTextEdit()
        self.list_output.setReadOnly(True)

        # Текстовое поле для вывода ошибок
        self.error_output = QTextEdit()
        self.error_output.setReadOnly(True)
        self.error_output.setStyleSheet("background-color: #ffdddd;")

        # Кнопки
        self.button_delete = QPushButton("Удалить")
        self.button_delete.clicked.connect(self.on_delete)

        self.button_add = QPushButton("Добавить")
        self.button_add.clicked.connect(self.on_add)

        self.button_update_data = QPushButton("Обновить данные")
        self.button_update_data.clicked.connect(self.on_update_data)

        self.button_update = QPushButton("Смотреть")
        self.button_update.clicked.connect(self.on_update)

        # Расположение элементов в окне
        hbox_buttons = QHBoxLayout()
        hbox_buttons.addWidget(self.button_delete)
        hbox_buttons.addWidget(self.button_add)
        hbox_buttons.addWidget(self.button_update_data)
        hbox_buttons.addWidget(self.button_update)

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("Список:"))
        vbox.addWidget(self.list_output)
        vbox.addWidget(QLabel("Ошибки:"))
        vbox.addWidget(self.error_output)
        vbox.addLayout(hbox_buttons)

        self.setLayout(vbox)

    def on_delete(self):
        pass

    def on_add(self):
        dialog = AddWorkerDialog(self)
        dialog.mydb = self.mydb
        if dialog.exec_() == QDialog.Accepted:
            self.on_update() # Обновляем список после добавления

    def on_update_data(self):
        pass

    def on_update(self):
        self.list_output.clear()
        self.error_output.clear()
        request = "SELECT * FROM kursovik.менеджер"
        if request:
            try:
                df = pd.read_sql(request, con=self.mydb).to_string()
                self.list_output.setText(df)
            except Exception as e:
                self.error_output.setText(f"Ошибка при отправке запроса: {e}")
        else:
            self.error_output.setText("Поле запроса пустое")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    registration_window = RegistrationWindow()
    admin_window = AdminWindow()
    menedger_window = MenedgerWindow()
    request_window = RequestWindow()
    worker_window = Workers()
    registration_window.adminwindow = admin_window
    registration_window.menedgerwindow = menedger_window
    admin_window.registrationwindow = registration_window
    admin_window.menedgerwindow = menedger_window
    admin_window.requestwindow = request_window
    admin_window.workers = worker_window
    menedger_window.registrationwindow = registration_window
    registration_window.show()
    sys.exit(app.exec_())