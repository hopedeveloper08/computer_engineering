import socket
import threading


HOST = '127.0.0.1'
PORT = 6666


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    username = input("Enter your username: ")
    client_socket.send(username.encode())

    id_ = client_socket.recv(1024).decode()
    print(f"Welcome {username}\nYour id is {id_}\nEnter your messages...\n")

    threading.Thread(target=receive_message, args=(client_socket,)).start()
    threading.Thread(target=send_message, args=(client_socket,)).start()


def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message.startswith("/direct"):
                parts = message.split()
                parts.pop(0)
                message = ' '.join(parts)
                print("[Direct] Admin:", message)

        except Exception as e:
            print("Error receiving message:", e)
            break


def send_message(client_socket):
    while True:
        try:
            message = input()
            client_socket.send(message.encode())

        except Exception as e:
            print("Error receiving message:", e)
            break


if __name__ == "__main__":
    main()
