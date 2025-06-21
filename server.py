import socket
import qrcode
import os


def generate_qr(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qr.png')


def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключен клиент: {client_address}")

        message = client_socket.recv(1024).decode('utf-8')
        print(f"Сообщение от клиента: {message}")
        generate_qr(message)

        if os.path.isfile('qr.png'):
            with open('qr.png', 'rb') as file:
                while True:
                    image_data = file.read(1024)
                    if not image_data:
                        break
                    client_socket.send(image_data)
            print("Изображение отправлено.")

        client_socket.close()


if __name__ == "__main__":
    start_server()
