from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit,
    QFileDialog, QInputDialog, QMessageBox
)

from .ui.MainWindowUi import Ui_MainWindow
from core import FileHandler


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._fileHandler = None

        self.setupUi(self)
        self._initSignals()
        self.newDocument()

    def _initSignals(self):
        """Связывает сигналсы виджетов со слотами."""
        self.actionNew.triggered.connect(self.newDocument)
        self.actionOpen.triggered.connect(self.openDocument)
        self.actionSave.triggered.connect(self.saveDocument)
        self.actionSaveAs.triggered.connect(self.saveDocumentAs)
        self.actionAboutQt.triggered.connect(QApplication.aboutQt)
        QApplication.clipboard().dataChanged.connect(self._clipboardDataChangedHandler)

    def _clipboardDataChangedHandler(self):
        """Обрабатывает изменения в данных буфера обмена."""
        enabled = self.sender().text() != ''
        self.actionPaste.setEnabled(enabled)

    def _getPassword(self):
        """Запрашивает и возвращает пароль у пользователя, иначе None."""
        d = QInputDialog(self)
        d.setLabelText('Enter password')
        d.setTextEchoMode(QLineEdit.Password)

        if d.exec_():
            return d.textValue() or None

        return None

    def setWindowTitle(self, title):
        """Задает новый заголовок окна."""
        if self.windowTitle():
            appTitle = self.windowTitle().rsplit(' - ', 1).pop()
            title = f'{title} - {appTitle}'
        super().setWindowTitle(title)

    def closeEvent(self, event):
        """Событие закрытия окна/виджета."""
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def maybeSave(self):
        """Проверяет, если документ был изменен, то предлагает его сохранить."""
        if not self.textEdit.document().isModified():
            return True

        ret = QMessageBox.warning(
            self,
            'The document has been modified',
            'Do you want to save your changes?',
            QMessageBox.Discard | QMessageBox.Cancel | QMessageBox.Save
        )

        if ret == QMessageBox.Save:
            return self.saveDocument()

        if ret == QMessageBox.Cancel:
            return False

        return True

    def newDocument(self):
        """Создает новый документ."""
        if self.maybeSave():
            self.textEdit.clear()
            self.setWindowTitle('Untitled')
            self._fileHandler = None

    def loadDocument(self, filename):
        """Загружает документ из файла."""
        if FileHandler.isEncrypted(filename):
            self._fileHandler = FileHandler(filename, self._getPassword())
        else:
            self._fileHandler = FileHandler(filename)

        data, err = self._fileHandler.load()

        if err:
            QMessageBox.warning(self, 'Warning', err)
        else:
            self.textEdit.setPlainText(data)
            self.setWindowTitle(filename)

    def openDocument(self):
        """Открыть указанный документ."""
        if self.maybeSave():
            filename, _ = QFileDialog.getOpenFileName(self, 'Open file', QDir.homePath())

            if filename:
                self.loadDocument(filename)

    def saveDocument(self):
        """Сохраняет текущий документ в файл."""
        if self._fileHandler is None:
            return self.saveDocumentAs()
        return self.saveDocumentToFile(self._fileHandler)

    def saveDocumentAs(self):
        """Сохраняет текущий документ под указанным именем в файл."""
        filename, _ = QFileDialog.getSaveFileName(self, 'Save as', QDir.homePath())
        saved = False

        if filename:
            self._fileHandler = FileHandler(filename, self._getPassword())
            saved = self.saveDocumentToFile(self._fileHandler)
            self.setWindowTitle(filename)

        return saved

    def saveDocumentToFile(self, fileHandler):
        """Сохраняет документ в указанный файл."""
        data = self.textEdit.toPlainText()
        saved, err = fileHandler.save(data)

        if err:
            QMessageBox.warning(self, 'Warning', err)
        else:
            self.textEdit.document().setModified(False)

        return saved
