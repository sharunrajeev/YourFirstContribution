import socket
from threading import Thread


def receive():
    while True:
        msg = client_socket.recv(BUFSIZ).decode("utf8")
        if msg == "{quit}":
            client_socket.close()
            break
        if not msg:
            break
        print(msg)


def send():
    while True:
        msg = input()
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            break


HOST = "127.0.0.1"
PORT = 5002

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket.socket()
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
send_thread = Thread(target=send)
receive_thread.start()
send_thread.start()
receive_thread.join()
send_thread.join()
