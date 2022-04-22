import json
import sys
from urllib.request import urlopen # requests

from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QDoubleSpinBox, QPushButton, QComboBox,
    QVBoxLayout
)


# print(Qt.Key_Return, Qt.Key_Enter)


class Course(QObject):
    CBR_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__courses = None

    def courses(self):
        if self.__courses is None:
            with urlopen(self.CBR_URL) as r:
                self.__courses = json.loads(r.read())
        return self.__courses

    def get(self, isoCode):
        courses = self.courses()

        if isoCode in courses['Valute']:
            return courses['Valute'][isoCode]['Value']

        return None


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__course = Course()

        self.initUi()
        self.initSignals()
        self.initLayouts()

    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)

        self.resultLabel = QLabel('Сумма в долларах', self)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевести', self)
        self.clearBtn = QPushButton('Очистить', self)

    def initSignals(self):
        self.convertBtn.clicked.connect(self.convert)

    def initLayouts(self):
        self.w = QWidget(self)

        self.mainLayout = QVBoxLayout(self.w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.clearBtn)

        self.setCentralWidget(self.w)

    def convert(self):
        value = self.srcAmount.value()

        if value:
            self.resultAmount.setValue(value / self.__course.get('USD'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
