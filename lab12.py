import socket
import threading
import sys

def send_datagram(sock, message, address):
    try:
        sock.sendto(message.encode(), address)
    except Exception as e:
        print(f"Error sending datagram: {e}")
        sys.exit(1)

def recv_datagram(sock, buf_size):
    try:
        data, addr = sock.recvfrom(buf_size)
        return data.decode(), addr
    except Exception as e:
        print(f"Error receiving datagram: {e}")
        sys.exit(1)

def server_thread():
    host = '0.0.0.0'
    port = 8888
    buf_size = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Server is listening on port {port}...")

        while True:
            data, client_address = recv_datagram(server_socket, buf_size)
            print(f"Received message: {data}")
            response = input("Enter response: ")
            send_datagram(server_socket, response, client_address)

def client_thread():
    server_ip = input("Enter server IP address: ")
    port = 8888
    buf_size = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        server_address = (server_ip, port)

        while True:
            message = input("Enter message to send: ")
            send_datagram(client_socket, message, server_address)

            data, _ = recv_datagram(client_socket, buf_size)
            print(f"Received response: {data}")

def main():
    if len(sys.argv) != 2:
        print("Please specify 'server' or 'client' as an argument.")
        sys.exit(1)

    role = sys.argv[1].lower()

    if role == "server":
        server_thread()
    elif role == "client":
        client_thread()
    else:
        print("Invalid argument. Use 'server' or 'client'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
