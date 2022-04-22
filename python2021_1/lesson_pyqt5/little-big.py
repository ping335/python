"""
QtCore
QtGui
QtWidgets
QtNetwork

QSql
QWebKit
QWebKitWidgets

QGuiApplication содержит основной цикл событий,
где все события из оконной системы и других источников
обрабатываются и отправляются.
Он также обрабатывает инициализацию и финализацию приложения
и обеспечивает управление сеансами.
Кроме того, QGuiApplication обрабатывает
большинство системных и прикладных настроек.

Для любого приложения с графическим интерфейсом, использующего Qt,
существует точно один объект QGuiApplication,
независимо от того, имеет ли приложение 0, 1, 2 или более окон
в любой момент времени.

Для приложений Qt без GUI используйте взамен QCoreApplication,
так как он не зависит от модуля Qt GUI.

Для приложений Qt на основе QWidget используйте вместо этого QApplication,
поскольку он предоставляет некоторые функциональные возможности,
необходимые для создания экземпляров QWidget.

QApplication.exec_()
    Входит в главный цикл обработки событий и ждёт до тех пор,
    пока не будет вызвана exit(), затем возвращает значение,
    которое было установлено в exit()
    (которое равно 0, если exit() вызвана через quit()).

    Эту функцию необходимо вызвать, чтобы начать обработку событий.
    Главный цикл обработки событий
    принимает события от оконной системы и отправляет их виджетам приложения.

    Метод exec_ () имеет подчеркивание потому,
    что exec является ключевым словом в python 2.
"""

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class LittleBig(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__increment = True

        self.initUi()
        self.initSignals()

    def initUi(self):
        self.resize(400, 300)

        self.setMinimumSize(300, 200) # self.minimumSize()
        self.setMaximumSize(600, 400)

        # self.btn = QPushButton()
        # self.btn = QPushButton(self)
        self.btn = QPushButton('We will push the button', self)

        self.setCentralWidget(self.btn)

    def initSignals(self):
        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        """Обработчик сигнала - в Qt называется слот"""
        if self.__increment:
            self.resize(self.width() + 10, self.height() + 10)
        else:
            self.resize(self.width() - 10, self.height() - 10)

        if self.width() <= self.minimumWidth():
            self.__increment = True

        if self.width() >= self.maximumWidth():
            self.__increment = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LittleBig()
    w.show()
    sys.exit(app.exec_())
