import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget,
                             QTableWidgetItem)
from PyQt6.QtCore import Qt


class TableWidgetWithChangeDetection(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget Change Detection")

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Столбец 1", "Столбец 2", "Столбец 3"])
        self.table_widget.itemChanged.connect(self.item_changed) # Подключаем сигнал

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

        #Пример заполнения таблицы
        self.add_initial_data()


    def add_initial_data(self):
        data = [
            ["Значение 1.1", "Значение 1.2", "Значение 1.3"],
            ["Значение 2.1", "Значение 2.2", "Значение 2.3"],
            ["Значение 3.1", "Значение 3.2", "Значение 3.3"]
        ]
        for row, row_data in enumerate(data):
            self.table_widget.insertRow(row)
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(value)
                self.table_widget.setItem(row, col, item)

    def item_changed(self, item):
        row = self.table_widget.row(item)
        col = self.table_widget.column(item)
        new_value = item.text()
        print(f"Ячейка изменена: строка {row}, столбец {col}, новое значение: {new_value}")
        #print(self.table_widget.itemAtPosition(row, col))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableWidgetWithChangeDetection()
    window.show()
    sys.exit(app.exec())
