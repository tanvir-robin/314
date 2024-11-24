import socket

def tcp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("TCP server listening on port", port)

    while True:
        conn, addr = server_socket.accept()
        print("Connected by", addr)
        with open("received_file_tcp.txt", "wb") as f:
            while True:
                data = conn.recv(100)
                if not data:
                    break
                f.write(data)
                conn.sendall(b"ACK")
        conn.close()
        print("File received successfully.")

tcp_server('127.0.0.1', 65432)
