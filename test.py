import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QListWidget,
                             QListWidgetItem, QPushButton, QLabel)
from PyQt6.QtGui import QIcon


class ListWidgetExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget Example")

        self.list_widget = QListWidget()
        self.list_widget.itemDoubleClicked.connect(self.item_double_clicked) # Обработка двойного клика

        # Добавление элементов с текстом и иконкой
        item1 = QListWidgetItem(QIcon('icon.png'), "Первый элемент") # Замените 'icon.png' на путь к вашему файлу
        item2 = QListWidgetItem("Второй элемент")
        item3 = QListWidgetItem(QIcon('icon.png'), "Третий элемент")
        self.list_widget.addItem(item1)
        self.list_widget.addItem(item2)
        self.list_widget.addItem(item3)


        button_add = QPushButton("Добавить элемент")
        button_add.clicked.connect(self.add_item)

        button_remove = QPushButton("Удалить выбранный элемент")
        button_remove.clicked.connect(self.remove_item)

        label_selected = QLabel("Выбранный элемент:")

        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(button_add)
        layout.addWidget(button_remove)
        layout.addWidget(label_selected)
        self.setLayout(layout)

        self.selected_label = label_selected # Сохраняем ссылку на label, чтобы обновлять текст

    def add_item(self):
        new_item = QListWidgetItem(f"Новый элемент {self.list_widget.count() + 1}")
        self.list_widget.addItem(new_item)

    def remove_item(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            row = self.list_widget.row(selected_item)
            self.list_widget.takeItem(row)
            self.update_selected_label()

    def item_double_clicked(self, item):
        self.selected_label.setText(f"Двойной клик по: {item.text()}")

    def update_selected_label(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            self.selected_label.setText(f"Выбранный элемент: {selected_item.text()}")
        else:
            self.selected_label.setText("Выбранный элемент:")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ListWidgetExample()
    window.show()
    sys.exit(app.exec())

"""   def refresh_f(self):
       try:
           connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987', database='Kursovik')
           with connection:
               with connection.cursor() as cursor:
                   text = ""
                   cursor.execute("SELECT * FROM kursovik.менеджер")
                   result = cursor.fetchall()
                   for rows in result:
                       for elements in rows:
                           text += str(elements) + " "
                       text += '\n'
           self.ui.list_workers.setText(text)
       except Exception as e:
           print(f"Ошибка при отправке запроса: {e}")
class UpdateMenedger(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Update_Menedger()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.update)
    def update(self):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='@Klay5274987',
                                         database='Kursovik')
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM `kursovik`.`менеджер` WHERE (`id_menedger` = " + self.ui.id.toPlainText() + ");")
                    connection.commit()
        except Exception as e:
            print(f"Ошибка при отправке запроса: {e}")
"""