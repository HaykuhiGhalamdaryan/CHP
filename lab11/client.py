import socket

BUFLEN = 1024

def main():
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 8888

    server_ip = input(f"Enter server IP (default {SERVER_IP}): ") or SERVER_IP
    try:
        server_port = int(input(f"Enter server port (default {SERVER_PORT}): ") or SERVER_PORT)
    except ValueError:
        print("Invalid port number. Using default.")
        server_port = SERVER_PORT

    server_address = (server_ip, server_port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        try:
            message = input("\nEnter message: ").strip()
            if not message:
                print("Empty message. Please try again.")
                continue

            client_socket.sendto(message.encode('utf-8'), server_address)
            print(f"Sending message: {message}")

            response, _ = client_socket.recvfrom(BUFLEN)
            print(f"Received from server: {response.decode('utf-8')}")
        except KeyboardInterrupt:
            print("\nClient shutting down.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
