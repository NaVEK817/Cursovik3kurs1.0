import sys
import matplotlib
matplotlib.use('QtAgg') # Важно! Указывает Matplotlib использовать бэкенд QtAgg
import matplotlib.pyplot as plt
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111) # Создаём один подграфик
        super().__init__(fig)
        self.setParent(parent)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Гистограмма в PyQt6")

        # Создаём данные (замените на ваши данные)
        data = {'Value': [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7]}
        df = pd.DataFrame(data)

        # Создаём холст для графика
        sc = MplCanvas(self, width=5, height=4, dpi=100)

        # Строим гистограмму на холсте
        df['Value'].plot.hist(ax=sc.axes, bins=7) # bins - количество столбиков
        sc.axes.set_xlabel("Значение")
        sc.axes.set_ylabel("Частота")
        sc.axes.set_title("Гистограмма")


        layout = QVBoxLayout()
        layout.addWidget(sc)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
