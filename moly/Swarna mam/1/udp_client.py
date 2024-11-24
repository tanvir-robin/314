import socket
import time


def udp_client(host, port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    with open(file_path, "rb") as f:
        for line in f:
            client_socket.sendto(line.strip(), (host, port))
            time.sleep(0.01)  # Small delay to avoid overwhelming the server

    client_socket.close()
    print("File sent successfully.")

udp_client('127.0.0.1', 65433, "abc.txt")
