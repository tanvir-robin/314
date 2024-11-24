import socket
import time

def tcp_client(host, port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.settimeout(1.0)  # Set a timeout for ACK

    with open(file_path, "rb") as f:
        while True:
            data = f.read(100)
            if not data:
                break
            while True:
                client_socket.sendall(data)
                try:
                    ack = client_socket.recv(3)
                    if ack == b"ACK":
                        break
                except socket.timeout:
                    print("Timeout. Resending data...")
                    continue  # Retry sending the same data chunk

    client_socket.close()
    print("File sent successfully.")

tcp_client('127.0.0.1', 65432, "abc.txt")
