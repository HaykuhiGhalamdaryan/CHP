import socket

BUFLEN = 1024
PORT = 8888

def handle_client(server_socket):
    while True:
        try:
            data, client_address = server_socket.recvfrom(BUFLEN)
            if data:
                print(f"Received packet from {client_address[0]}:{client_address[1]}")
                print(f"Data: {data.decode('utf-8')}")

                prompt = "Enter message: "
                server_socket.sendto(prompt.encode('utf-8'), client_address)
        except KeyboardInterrupt:
            print("\nServer shutting down.")
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', PORT))

    print(f"Server is running on port {PORT}...")
    handle_client(server_socket)

if __name__ == "__main__":
    main()
