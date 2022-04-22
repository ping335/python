from datetime import datetime
import os
import socket
import threading


def run_in_thread(func):
    """Исполняет задекорированную функцию в дочернем потоке."""
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        # thread = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        thread.run()
    return wrapper


def log(msg):
    """Логирует сообщение на экран."""
    template = '[{:%Y-%m-%d %H:%M:%S}] {}'
    print(template.format(datetime.now(), msg))


def recv_all(sock, chunk_size=1024):
    """Возвращает все данные, отправленные в сокет."""
    buffer = b''
    finished = False
    
    while not finished:
        chunk = sock.recv(chunk_size)
        buffer += chunk
        
        if not chunk or len(chunk) < chunk_size:
            """Пустая строка - сигнал о том, что соединение закрыто"""
            finished = True
    
    return buffer


@run_in_thread
def connection_handler(conn, addr):
    """Обработчик входящего соединения."""
    log(f'New connection {addr}')
    data = recv_all(conn).decode()
    data = data[::-1]
    conn.sendall(data.encode())
    conn.close()


def make_server(host='localhost', port=8000, backlog=2):
    """Создает сервер и запускает его на прослушку входящих соединений."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Связать сокет с IP-адресом и портом
        sock.bind((host, port))
        # Объявить о желании принимать соединения. Слушает порт и ждет когда будет установлено соединение
        sock.listen(backlog)
        
        log('The server is running and waiting for incoming requests...')
        log(f'-> Address: {host}:{port}')
        log(f'-> Ctrl+C or Ctrl+Pause for Windows to exit')
        
        while 1:
            try:
                # Принять запрос на установку соединения
                # conn, addr = sock.accept()
                # connection_handler(conn, addr)
                connection_handler(*sock.accept())
            except KeyboardInterrupt:
                log('Server stopped by user.')
                break


def make_client(host='localhost', port=8000):
    """Создает клиент."""
    while 1:
        try:
            message = input('Enter message: ')
            
            if message:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect((host, port))
                    sock.sendall(message.encode())
                    answer = recv_all(sock).decode()
                    print('->', answer)
        except socket.error as err:
            print(err)
        except (KeyboardInterrupt, EOFError):
            print('\nGood bye!')
            break











