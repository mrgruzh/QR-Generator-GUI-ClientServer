
import socket
import sys
import os

def start_client(message, host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
    except Exception as e:
        print(f"Не удалось подключиться к серверу {host}:{port}: {e}")
        sys.exit(1)
    print(f"Подключен к серверу {host}:{port}")

    try:
        client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"Не удалось отправить сообщение серверу {host}:{port}: {e}")
        sys.exit(1)

    with open('client/qr.png', 'wb') as file:
        while True:
            image_data = client_socket.recv(1024)
            if not image_data:
                break
            file.write(image_data)

    print("Изображение получено и сохранено.")
    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('Ошибка: нет аргументов, должен быть один')
        sys.exit(1)
    message = sys.argv[1]
    start_client(message)
