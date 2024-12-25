import os
import time
from openpyxl import load_workbook
import pandas as pd
import sys
import pymysql
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QDialog, QTableWidget, \
    QTableWidgetItem, QLabel, QListWidgetItem
from logIn import Ui_LogIn
from docxtpl import DocxTemplate
from AdminMenu import Ui_Form as Ui_AdminMenu
from Request import Ui_Form as Ui_Request
from MenedgerMenu import Ui_Form as Ui_Menedger
from AccounterMenu import Ui_Form as Ui_Accounter
from ListWorkers import Ui_Form as Ui_ListWorkers
from AppendMenedger import Ui_Form as Ui_Append_Menedger
from DeleteMenedger import Ui_Form as Ui_Delete_Menedger
from ListArendodatel import Ui_Form as Ui_List_Arendodatel
from ListDocs import Ui_Form as Ui_List_Docs
from SearchOnMetro import Ui_Form as Ui_SearchOnMetro
from ListApartments import Ui_Form as  Ui_List_Apartments
from AppendPact import Ui_Form as Ui_AppendPact
from DeleteArendator import Ui_Form as Ui_Delete_Arendator
from ListArendator import Ui_Form as Ui_List_Arendator
from AppendArendator import Ui_Form as Ui_Append_Arendator
from SearchApartment import Ui_Form as Ui_Search_Apartment
import matplotlib.pyplot as plt
admin_users = {'root': "@Klay5274987"}
accounter_users = {'accounter' : 'acc1'}
menedger_users = {'menedger' : "men1"}
USER = ""
class WarningDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.WindowType.Window)
        self.setWindowTitle("Предупреждение")
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.resize(800, 600)
        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_ok = QPushButton("OK")
        self.button_ok.clicked.connect(self.accept)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_ok)
        self.setLayout(layout)
        self.move(QApplication.primaryScreen().geometry().center() - self.rect().center())
    def setText(self, text):
        self.label.setText(text)
class Registration(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LogIn()
        self.ui.setupUi(self)
        self.ui.registerButton.clicked.connect(self.checked_user)
    def open_admin(self):
        admin = Admin(self)
        admin.show()
        self.hide()
    def open_menedger(self):
        menedger = Menedger(self)
        menedger.show()
        self.hide()
    def open_accounter(self):
        accounter = Accounter(self)
        accounter.show()
        self.hide()
    def checked_user(self):
        username = self.ui.usernameLineEdit.text()
        global USER
        USER = self.ui.usernameLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        if not username or not password:
            self.ui.errorLabel.setText("Заполните все поля!")
            return
        if username in admin_users.keys() and password in admin_users.values():
            self.open_admin()
        elif username in menedger_users.keys() and password in menedger_users.values():
            self.open_menedger()
        elif username in accounter_users.keys() and password in accounter_users.values():
            self.open_accounter()
        else:
            self.ui.errorLabel.setText("Неправильный логин или пароль.")
class Admin(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AdminMenu()
        self.ui.setupUi(self)
        self.ui.free_req.clicked.connect(self.open_request)
        self.ui.disconnect.clicked.connect(self.disconnect_f)
        self.ui.menu_acc.clicked.connect(self.open_accounter)
        self.ui.menu_menedger.clicked.connect(self.open_menedger)
        self.ui.list_menedgers.clicked.connect(self.open_list_workers)
    def open_list_workers(self):
        wind = ListWorkers(self)
        wind.show()
        self.hide()
    def open_menedger(self):
        menedger = Menedger(self)
        menedger.show()
        self.hide()
    def open_accounter(self):
        accounter = Accounter(self)
        accounter.show()
        self.hide()
    def open_request(self):
        requestw = Request(self)
        requestw.show()
        self.hide()
    def disconnect_f(self):
        backw = Registration(self)
        backw.show()
        self.hide()
class Request(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Request()
        self.ui.setupUi(self)
        self.ui.back_button.clicked.connect(self.open_admin)
        self.ui.send_button.clicked.connect(self.request_f)
    def open_admin(self):
        admin = Admin(self)
        admin.show()
        self.hide()
    def request_f(self):
        self.ui.result_line.clear()
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            if self.ui.request_line.toPlainText()[0] == 'S' or self.ui.request_line.toPlainText()[0] == 's':
                with connection:
                    with connection.cursor() as cursor:
                        text = ""
                        cursor.execute(self.ui.request_line.toPlainText())
                        result = cursor.fetchall()
                        for rows in result:
                            for elements in rows:
                                text += str(elements) + " "
                            text += '\n'
                self.ui.result_line.setText(text)
            else:
                with connection:
                    with connection.cursor() as cursor:
                        cursor.execute(self.ui.request_line.toPlainText())
                    connection.commit()
                self.ui.result_line.setText('Ваш запрос успешно выполнен')
        except Exception as e:
            self.ui.error_line.setText(f"Ошибка при отправке запроса: {e}")
class Menedger(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Menedger()
        self.ui.setupUi(self)
        self.ui.filter_apartmenrs.clicked.connect(self.filter_apartment_f)
        self.ui.append_arendator.clicked.connect(self.append_arendator_f)
        self.ui.disconnect.clicked.connect(self.disconnect_f)
        self.ui.delete_arendator.clicked.connect(self.delete_arendator_f)
        self.ui.allert_arendator.clicked.connect(self.allert)
        self.ui.append_pact.clicked.connect(self.append_pact_f)
        self.ui.list_apartment.clicked.connect(self.list_apartment_f)
        self.ui.look_metro.clicked.connect(self.look_metro_f)
        self.ui.list_pacts.clicked.connect(self.list_pacts_f)
        self.ui.list_arendodatel.clicked.connect(self.list_arendodatel_f)
        self.ui.list_arendator.clicked.connect(self.list_arendator_f)
    def filter_apartment_f(self):
        searchApartment = SearchApartment(self)
        searchApartment.show()
    def append_arendator_f(self):
        append_arendator = AppendArendator(self)
        append_arendator.show()
    def list_arendator_f(self):
        list_arendator = ListArendator(self)
        list_arendator.show()
    def list_arendodatel_f(self):
        list_arendodatel = ListArendodatel(self)
        list_arendodatel.show()
    def list_pacts_f(self):
        list_docs = ListDocs(self)
        list_docs.show()
    def look_metro_f(self):
        search_on_metro = SearchOnMetro(self)
        search_on_metro.show()
    def list_apartment_f(self):
        list_apartments = ListApartments(self)
        list_apartments.show()
    def append_pact_f(self):
        append_pact = AppendPact(self)
        append_pact.show()
    def allert(self):
        try:
            mydb = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='@Klay5274987',
                database='Kursovik'
            )
            query = '''SELECT CONCAT(mn.surname, " ", mn.name, " ", mn.midle_name) as FIO_Menedger,
            CONCAT(ator.surname, " ", ator.name, " ", ator.midle_name) as FIO_Arendator,
            sd.id_number_deal, sd.end_time, ator.id_tenant as ID
            FROM kursovik.сделка sd
            JOIN kursovik.арендатор ator
            ON sd.tenat_deal_id = ator.id_tenant
            JOIN kursovik.менеджер mn
            ON ator.menedger_tenat_id = mn.id_menedger
            WHERE TIMESTAMPDIFF(MONTH, CURRENT_DATE(), sd.end_time) = 0
            ORDER BY FIO_Menedger, FIO_Arendator'''
            df = pd.read_sql(query, con=mydb)
            for i in range(len(df)):
                doc = DocxTemplate("Предупреждение_шаблон.docx")
                context = {
                    'FIO_Menedger': df['FIO_Menedger'][i],
                    'FIO_Arendator': df['FIO_Arendator'][i],
                    'id_number_deal': df['id_number_deal'][i],
                    'end_time': df['end_time'][i]
                }
                doc.render(context)
                doc.save(f"Предупреждение_{df['ID'][i]}.docx")
            mydb.close()
            warningw = WarningDialog(self)
            warningw.setText(f"Предупреждение(я) выслано(ы)")
            warningw.show()
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке предупреждений: {e}")
            warningw.show()
    def delete_arendator_f(self):
        delete_arendator = DeleteArendator(self)
        delete_arendator.show()
    def disconnect_f(self):
        if USER != "root":
            backw = Registration(self)
        else:
            backw = Admin(self)
        backw.show()
        self.close()
class SearchApartment(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Search_Apartment()
        self.ui.setupUi(self)
        self.print_table(None, None, None, None, None, None, None)
        self.ui.look.clicked.connect(self.searching)
    def ftr(self, line):
        if line == "":
            return None
        else:
            return line
    def searching(self):
        self.print_table(self.ftr(self.ui.min_sq.text()),self.ftr(self.ui.max_sq.text()), self.ftr(self.ui.min_cost.text()), self.ftr(self.ui.max_cost.text()),
                         self.ftr(self.ui.communication.currentText()), self.ftr(self.ui.renov.currentText()), self.ftr(self.ui.proximaty.text()))
    def print_table(self, min_sq, max_sq, min_cost, max_cost, com, ren, prox):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.callproc('Search_Apartment3', [min_sq, max_sq, min_cost, max_cost, com, ren, prox])
                    maxid = len(cursor.fetchall())
                    print(maxid)
                    self.ui.tableWidget.setRowCount(maxid)
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.callproc('Search_Apartment3', [min_sq, max_sq, min_cost, max_cost, com, ren, prox])
                    result = cursor.fetchall()
                    index = 0
                    for rows in result:
                        for i in range(5):
                            self.ui.tableWidget.setItem(index, i, QTableWidgetItem(str(rows[i])))
                        index += 1
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
class AppendArendator(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Append_Arendator()
        self.ui.setupUi(self)
        self.ui.insert.clicked.connect(self.insert)
    def insert(self):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987', database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(id_tenant) FROM kursovik.арендатор")
                    maxid = int(cursor.fetchall()[0][0]) + 1

            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                                 database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO kursovik.арендатор "
                                   "(id_tenant, surname, name, midle_name, pasp_ser, pasp_numb, phone_numb, franchise_tenat_id, menedger_tenat_id, INN)" +
                                   "VALUES ("+ str(maxid) + ",'" +
                                   self.ui.line_surname.text() + "','" +
                                   self.ui.linename.text() +  "','" +
                                   self.ui.linemidle_name.text() + "','" +
                                   self.ui.linepaspser.text() + "','" +
                                   self.ui.linepaspnumb.text() + "'," +
                                   self.ui.lineidfranch.text() + "," +
                                    "1,'" +
                                   self.ui.lineINN.text() + "');")
                    connection.commit()
            warningw = WarningDialog(self)
            warningw.setText(f"Добавление произошло успешно")
            warningw.show()
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
class ListArendodatel(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_List_Arendodatel()
        self.ui.setupUi(self)
        self.print_table()
    def print_table(self):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT MAX(id_renter) FROM kursovik.арендодатель")
                    maxid = int(cursor.fetchall()[0][0])
                    self.ui.tableWidget.setRowCount(maxid)
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM kursovik.арендодатель")
                    result = cursor.fetchall()
                    index = 0
                    for rows in result:
                        for i in range(6):
                            self.ui.tableWidget.setItem(index, i, QTableWidgetItem(str(rows[i])))
                        index += 1
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
class ListDocs(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_List_Docs()
        self.ui.setupUi(self)
        self.print_table()
        self.ui.listWidget.itemDoubleClicked.connect(self.open_docx)
    def print_table(self):
        try:
            project_path = os.path.dirname(os.path.abspath(__file__))  # Путь к папке проекта
            docx_files = [f for f in os.listdir(project_path) if f.endswith('.docx')]
            for file in docx_files:
                item = QListWidgetItem(os.path.splitext(file)[0])  # Добавляем имя без расширения
                self.ui.listWidget.addItem(item)
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при работе с файлами: {e}")
            warningw.show()
    def open_docx(self, item):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            word_file_path = os.path.join(script_dir, item.text() + ".docx")
            os.startfile(word_file_path)
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при работе с файлами: {e}")
            warningw.show()
class SearchOnMetro(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SearchOnMetro()
        self.ui.setupUi(self)
        self.print_table(None, None)
        self.ui.look.clicked.connect(self.look_f)
    def print_table(self, metro_name, metro_line):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.callproc('Search_On_Metro1', [metro_name, metro_line])
                    maxid = len(cursor.fetchall())
                    print(maxid)
                    self.ui.tableWidget.setRowCount(maxid)
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.callproc('Search_On_Metro1', [metro_name, metro_line])
                    result = cursor.fetchall()
                    index = 0
                    for rows in result:
                        for i in range(5):
                            self.ui.tableWidget.setItem(index, i, QTableWidgetItem(str(rows[i])))
                        index += 1
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
    def look_f(self):
        metro_name = self.ui.linestation.text()
        if metro_name =='':
            metro_name = None
        metro_line = self.ui.lineline.text()
        if metro_line =='':
            metro_line = None
        self.print_table(metro_name, metro_line)
class AppendPact(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AppendPact()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.append_pact)
    def append_pact(self):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(id_number_deal) FROM kursovik.сделка")
                    maxid = int(cursor.fetchall()[0][0]) + 1

            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    print(str(maxid) + ",'" +
                                   self.ui.date_deal.text() + "','" +
                                   self.ui.start_time.text() + " 00:00:00','" +
                                   self.ui.end_time.text() + " 00:00:00'," +
                                   self.ui.id_arendator.text() + "," +
                                   self.ui.id_apartment.text() + ",'" +
                                   self.ui.lineEdit_4.text() + "');")
                    cursor.execute("INSERT INTO kursovik.сделка "
                                   "(id_number_deal, date_deal, start_time, end_time, tenat_deal_id, apartment_deal_id, mounth_pay)" +
                                   "VALUES (" + str(maxid) + ",'" +
                                   self.ui.date_deal.text() + "','" +
                                   self.ui.start_time.text() + " 00:00:00','" +
                                   self.ui.end_time.text() + " 00:00:00'," +
                                   self.ui.id_arendator.text() + "," +
                                   self.ui.id_apartment.text() + "," +
                                   self.ui.lineEdit_4.text() + ");")
                    connection.commit()
            mydb = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='@Klay5274987',
                database='Kursovik'
            )
            query = f'''SELECT sd.id_number_deal as rent_number, sd.date_deal, 
            CONCAT(ardtel.surname, " ", ardtel.name, " ", ardtel.midle_name) as FIO_Arendodatel,
            ardtel.phone_number as phone_number_arednodatel,
            ardtel.INN as INN_Arendodatel,
            CONCAT(ardtor.surname, " ", ardtor.name, " ", ardtor.midle_name) as FIO_Arendator,
            ardtor.phone_numb as phone_number_arendator,
            ardtor.INN as INN_Arendator,
            pom.adress, pom.square,
            sd.start_time, sd.end_time, 
            sd.mounth_pay FROM kursovik.сделка sd
            JOIN kursovik.помещение pom
            ON sd.tenat_deal_id = pom.id_apartment
            JOIN kursovik.арендодатель ardtel
            ON pom.renter_apartment_id = ardtel.id_renter
            JOIN kursovik.арендатор ardtor
            ON sd.tenat_deal_id = ardtor.id_tenant
            WHERE sd.id_number_deal = {maxid}'''
            df = pd.read_sql(query, con=mydb)
            doc = DocxTemplate("Договор_аренды_ПСН_шаблон.docx")
            context = {
                'rent_number': df['rent_number'][0],
                'FIO_Arendodatel': df['FIO_Arendodatel'][0],
                'INN_Arendodatel': df['INN_Arendodatel'][0],
                'phone_number_arednodatel': df['phone_number_arednodatel'][0],
                'FIO_Arendator': df['FIO_Arendator'][0],
                'INN_Arendator': df['INN_Arendator'][0],
                'phone_number_arendator': df['phone_number_arendator'][0],
                'start_time': df['start_time'][0],
                'end_time': df['end_time'][0],
                'adress': df['adress'][0],
                'square': df['square'][0],
                'mounth_pay': df['mounth_pay'][0],
                'date_deal': df['date_deal'][0]
            }
            doc.render(context)
            doc.save(f"Договор_аренды_ПСН_{df['rent_number'][0]}.docx")
            mydb.close()
            warningw = WarningDialog(self)
            warningw.setText(f"Запрос выполнен успешно")
            warningw.show()
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
class DeleteArendator(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Delete_Arendator()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.delete)
    def delete(self):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM `kursovik`.`арендатор` WHERE (`id_tenant` = " + self.ui.lineEdit.text() + ");")
                    connection.commit()
                    warningw = WarningDialog(self)
                    warningw.setText(f"Арендатор успешно удалён")
                    warningw.show()
                    self.close()
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
class Accounter(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Accounter()
        self.ui.setupUi(self)
        self.list_men = ["Все менеджеры"]
        self.df = self.get_df()
        dpor = self.df.drop_duplicates(subset=['FIO'])
        for i in range(len(dpor)):
            self.ui.menedger.addItem(dpor['FIO'][i])
        self.print_graph( 0, 0, self.list_men)
        self.ui.disconnect.clicked.connect(self.disconnect_f)
        self.ui.account.clicked.connect(self.calculate_f)
        self.ui.print_file.clicked.connect(self.print_excel)
        self.ui.menedger.itemSelectionChanged.connect(self.onSelectionChanged)
        self.ui.open_file.clicked.connect(self.open_file_f)
    def open_file_f(self):
        listExcel = ListExcel(self)
        listExcel.show()
    def get_df(self):
        mydb = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='@Klay5274987',
            database='Kursovik'
        )
        query = '''CALL PAYROLL_MENEDGER()'''
        df = pd.read_sql(query, con=mydb)
        mydb.close()
        return df
    def print_excel(self):
        unicnumb = ""
        dpor = self.df.drop_duplicates(subset=['FIO'])
        for i in range(len(dpor)):
            unicnumb += dpor['FIO'][i]
        self.export_dataframe_to_excel(self.df, self.get_title() +unicnumb+ '.xlsx')
    def onSelectionChanged(self):
        selected_items = []
        for item in self.ui.menedger.selectedItems():
            selected_items.append(item.text())
        self.list_men = selected_items
    def df_filter(self, df, month, year, menedger):
        if month != 0:
            filter_month = df[(df['month'] == month)].copy()
        else:
            filter_month = df.copy()
        if year != 0:
            filter_year = filter_month[(filter_month['year'] == year)].copy()
        else:
            filter_year = filter_month.copy()
        if "Все менеджеры" not in menedger:
            filter_menedger = filter_year[(filter_year['FIO'].isin(menedger))].copy()
        else:
            filter_menedger = filter_year.copy()
        return filter_menedger.groupby('FIO')['pay_for_month'].mean().reset_index()
    def get_title(self):
        m = self.ui.month.currentText()
        y = self.ui.year.currentText()
        return "Отчётность о средней получке за " + m + ' ' + y
    def print_graph(self, month, year, menedger):
        try:
            df = self.get_df()
            ed = self.df_filter(df, month, year, menedger)
            plt.xticks(fontsize=6, rotation=45)
            plt.bar(ed['FIO'], ed['pay_for_month'])
            plt.title(self.get_title())
            plt.tight_layout()
            plt.subplots_adjust(bottom=0.3)
            plt.savefig("my_graph.png")
            plt.close()
            pixmap = QPixmap("my_graph.png")
            self.ui.graph.setPixmap(pixmap)
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
    def export_dataframe_to_excel(self, df, output_filepath):
        try:
            workbook = load_workbook("шаблон.xlsx")
            sheet = workbook.active
            for row in df.values.tolist():
                sheet.append(row)
            workbook.save(output_filepath)
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
    def calculate_f(self):
        try:
            month = {
                'Все месяца' : 0,
                'Январь': 1,
                'Февраль': 2,
                'Март': 3,
                'Апрель': 4,
                'Май': 5,
                'Июнь': 6,
                'Июль': 7,
                'Август': 8,
                'Сентябрь': 9,
                'Октябрь': 10,
                'Ноябрь': 11,
                'Декабрь': 12
            }
            m = self.ui.month.currentText()
            y = self.ui.year.currentText()
            self.print_graph(month[m], int(y), self.list_men)
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
    def disconnect_f(self):
        if USER != "root":
            backw = Registration(self)
        else:
            backw = Admin(self)
        backw.show()
        self.close()
class ListApartments(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_List_Apartments()
        self.ui.setupUi(self)
        self.print_table()
    def print_table(self):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(id_apartment) FROM kursovik.помещение WHERE id_apartment NOT IN (SELECT apartment_deal_id FROM kursovik.сделка)")
                    maxid = int(cursor.fetchall()[0][0])
                    self.ui.tableWidget.setRowCount(maxid)
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM kursovik.помещение WHERE id_apartment NOT IN (SELECT apartment_deal_id FROM kursovik.сделка)")
                    result = cursor.fetchall()
                    index = 0
                    for rows in result:
                        for i in range(9):
                            self.ui.tableWidget.setItem(index, i, QTableWidgetItem(str(rows[i])))
                        index += 1
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
class ListArendator(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_List_Arendator()
        self.ui.setupUi(self)
        self.print_table()
        self.ui.tableWidget.itemChanged.connect(self.item_changed)
    def item_changed(self, item):
        row = self.ui.tableWidget.row(item)
        col = self.ui.tableWidget.column(item)
        self.ui.tableWidget.setItem(row, col, item)
        key = self.ui.tableWidget.horizontalHeaderItem(col).text()
        id = self.ui.tableWidget.item(row, 0).text()
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987', database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE kursovik.арендатор SET " + key + " = '" + item.text() + "' WHERE id_tenant"  + ' = ' + str(id) + ";")
                    connection.commit()
                    warningw = WarningDialog(self)
                    warningw.setText(f"Арендатор успешно обновлён")
                    warningw.show()
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
    def print_table(self):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(id_tenant) FROM kursovik.арендатор")
                    maxid = int(cursor.fetchall()[0][0])
                    self.ui.tableWidget.setRowCount(maxid)
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM kursovik.арендатор")
                    result = cursor.fetchall()
                    index = 0
                    for rows in result:
                        for i in range(10):
                            self.ui.tableWidget.setItem(index, i, QTableWidgetItem(str(rows[i])))
                        index += 1
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
class ListWorkers(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ListWorkers()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.open_admin)
        self.ui.insert.clicked.connect(self.insert_f)
        self.ui.delete_2.clicked.connect(self.delete)
        self.ui.tableWidget.itemChanged.connect(self.item_changed)
        self.print_table()
    def print_table(self):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT MAX(id_menedger) FROM kursovik.менеджер")
                    maxid = int(cursor.fetchall()[0][0])
                    self.ui.tableWidget.setRowCount(maxid)
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM kursovik.менеджер")
                    result = cursor.fetchall()
                    index = 0
                    for rows in result:
                        for i in range(7):
                            self.ui.tableWidget.setItem(index, i, QTableWidgetItem(str(rows[i])))
                        index += 1
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
    def open_admin(self):
        admin = Admin(self)
        admin.show()
        self.hide()
    def item_changed(self, item):
        row = self.ui.tableWidget.row(item)
        col = self.ui.tableWidget.column(item)
        self.ui.tableWidget.setItem(row, col, item)
        key = self.ui.tableWidget.horizontalHeaderItem(col).text()
        dict = {
            "Идентификатор" : "id_menedger",
            "Фамилия" : "surname",
            "Имя": "name",
            "Отчество": "midle_name",
            "Номер телефона": "phone_number",
            "Серия паспорта": "pasp_ser",
            "Номер паспорта": "pasp_numb"
        }
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987', database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE kursovik.менеджер SET " + str(dict[key]) + " = '" + item.text() + "' WHERE id_menedger"  + ' = ' + str(row+1) + ";")
                    connection.commit()
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
    def delete(self):
        delete_menedgerw = DeleteMenedger(self)
        delete_menedgerw.show()
    def insert_f(self):
        insert_menedgerw = AppendMenedger(self)
        insert_menedgerw.show()
class DeleteMenedger(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Delete_Menedger()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.delete)
    def delete(self):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987', database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM `kursovik`.`менеджер` WHERE (`id_menedger` = " + self.ui.lineEdit.text() + ");")
                    connection.commit()
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
        lw = ListWorkers(self)
        lw.show()
        self.close()
class AppendMenedger(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Append_Menedger()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.send)
    def send(self):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987', database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT MAX(id_menedger) FROM kursovik.менеджер")
                    maxid = int(cursor.fetchall()[0][0]) + 1

            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                                 database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO kursovik.менеджер "
                                   "(id_menedger, surname, name, midle_name, "
                                   "phone_number, pasp_ser, pasp_numb)" +
                                   "VALUES ("+ str(maxid) + ",'" +
                                   self.ui.surname.text() + "','" +
                                   self.ui.name.text() +  "','" +
                                   self.ui.midle_name.text() + "','" +
                                   self.ui.phone_numb.text() + "','" +
                                   self.ui.pasp_ser.text() + "','" +
                                   self.ui.pasp_numb.text() + "');")
                    connection.commit()
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при отправке запроса: {e}")
            warningw.show()
        lw = ListWorkers(self)
        lw.show()
        self.close()
class ListExcel(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_List_Docs()
        self.ui.setupUi(self)
        self.print_table()
        self.ui.listWidget.itemDoubleClicked.connect(self.open_docx)
    def print_table(self):
        try:
            project_path = os.path.dirname(os.path.abspath(__file__))  # Путь к папке проекта
            docx_files = [f for f in os.listdir(project_path) if f.endswith('.xlsx')]
            for file in docx_files:
                item = QListWidgetItem(os.path.splitext(file)[0])  # Добавляем имя без расширения
                self.ui.listWidget.addItem(item)
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при работе с файлами: {e}")
            warningw.show()
    def open_docx(self, item):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            word_file_path = os.path.join(script_dir, item.text() + ".xlsx")
            os.startfile(word_file_path)
        except Exception as e:
            warningw = WarningDialog(self)
            warningw.setText(f"Ошибка при работе с файлами: {e}")
            warningw.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    start = Registration()
    start.show()
    sys.exit(app.exec())