import socket

HOST = '0.0.0.0'
PORT = 30000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"robot listens form port: {PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"Connection achieved to visual processing: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received command: {data.decode('utf-8').strip()}")
