import socket
import threading


HOST = '127.0.0.1'
PORT = 6666
id_counter = 1
client_sockets = dict()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("Server is listening on ", f"{HOST}:{PORT}")

    threading.Thread(target=command_handler).start()
    print("for send message to the client Usage: /direct <client_id> <message>\n\n")

    while True:
        client_socket, address = server_socket.accept()
        client_id, username = register_client(client_socket)

        print(f"New connection from {address}\nusername: {username}\nid: {client_id}\n\n")

        threading.Thread(target=receive_message_handler, args=(client_socket, username, client_id)).start()


def register_client(client_socket):
    username = client_socket.recv(1024).decode()

    global id_counter
    client_id = id_counter
    id_counter += 1

    message = str(client_id)
    client_socket.send(message.encode())

    client_sockets[client_id] = client_socket

    return client_id, username


def receive_message_handler(client_socket, username, client_id):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(f"{username} (ID: {client_id}): {message}")

        except Exception as e:
            print("Error receiving message:", e)
            break


def command_handler():
    while True:
        try:
            command = input()

            if command.startswith("/direct"):
                send_direct_message(command)
            else:
                print("command not recognized!")

        except ValueError:
            print("Invalid client ID...")

        except Exception as e:
            print("Error receiving message:", e)
            break


def send_direct_message(command):
    parts = command.split()
    if len(parts) < 3:
        print("Invalid command format. Usage: /direct <client_id> <message>")
        return

    id_ = int(parts.pop(1))
    message = ' '.join(parts)
    client_sockets[id_].send(message.encode())


if __name__ == "__main__":
    main()
