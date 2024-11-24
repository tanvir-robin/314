import socket

def udp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print("UDP server listening on port", port)

    with open("abc.txt", "wb") as f:
        while True:
            data, addr = server_socket.recvfrom(1024)
            if not data:
                break
            f.write(data + b"\n")

udp_server('127.0.0.1', 65433)
