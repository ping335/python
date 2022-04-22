from itertools import cycle

from PyQt5.QtCore import QObject, QFile, QTextStream, QDataStream


class Encoder(QObject):
    """Использует алгоритм XOR-шифрования."""

    def __init__(self, secretKey, parent=None):
        super().__init__(parent)
        self._secretKey = secretKey

    def _iterKey(self):
        for i in cycle(self._secretKey):
            yield ord(i)

    def _encrypt(self, data):
        """
        data это:
        1. список ASCII-кодов символов исходного текста (шифрование)
        2. список XOR-сумм (дешифрование)
        """
        for i, key_code in zip(data, self._iterKey()):
            yield i ^ key_code

    def encode(self, s):
        result = self._encrypt(ord(i) for i in s)
        return ' '.join(str(i) for i in result).encode()

    def decode(self, s):
        data = (int(i) for i in s.decode().split())
        result = self._encrypt(data)
        return ''.join(chr(i) for i in result)


class FileHandler(QObject):
    MAGIC_NUMBERS = 0xdc0666dc

    def __init__(self, filename, secretKey=None, parent=None):
        super().__init__(parent)

        self._filename = filename
        self._secretKey = secretKey

    def load(self):
        """Открывает файл, читает и возвращает содержимое."""
        f = QFile(self._filename)

        if not f.open(QFile.ReadOnly):
            return None, f.errorString()

        if self._secretKey is None:
            data = QTextStream(f).readAll()
        else:
            stream = QDataStream(f)
            stream.readUInt32()

            encoder = Encoder(self._secretKey, self)
            data = encoder.decode(stream.readString()) # читаем файл до конца и получаем тип данных str

        f.close()

        return data, None

    def save(self, data):
        """Сохраняет файл и возвращает результат выполнения операции."""
        f = QFile(self._filename)

        if not f.open(QFile.WriteOnly):
            return False, f.errorString()

        if self._secretKey is None:
            stream = QTextStream(f)
            stream << data
        else:
            stream = QDataStream(f)
            stream.writeUInt32(self.MAGIC_NUMBERS)

            encoder = Encoder(self._secretKey, self)
            stream.writeString(encoder.encode(data))

        f.close()

        return True, None

    @classmethod
    def isEncrypted(cls, filename):
        """Возвращает истину, если файл зашифрован нашим алгоритмом, иначе ложь."""
        f = QFile(filename)
        result = False

        if f.open(QFile.ReadOnly):
            stream = QDataStream(f)
            result = stream.readUInt32() == cls.MAGIC_NUMBERS
            f.close()

        return result
